<template>
  <section class="course-module">
    <p class="module-kicker">步骤清单</p>
    <ul>
      <li v-for="(item, index) in items" :key="index">
        <label>
          <input v-model="checked[index]" type="checkbox" @change="persist" />
          <span>{{ item }}</span>
        </label>
      </li>
    </ul>
    <p class="progress">已勾选 {{ done }} / {{ items.length }}。勾选只存在这台浏览器里。</p>
  </section>
</template>

<script setup>
import { computed, onMounted, reactive } from 'vue'

const props = defineProps({
  items: { type: Array, default: () => [] },
  storageKey: { type: String, default: '' }
})

const checked = reactive([])

const done = computed(() => checked.filter(Boolean).length)

function persist() {
  if (!props.storageKey || typeof localStorage === 'undefined') return
  localStorage.setItem(props.storageKey, JSON.stringify(checked))
}

onMounted(() => {
  const blank = props.items.map(() => false)
  if (!props.storageKey || typeof localStorage === 'undefined') {
    checked.splice(0, checked.length, ...blank)
    return
  }
  try {
    const saved = JSON.parse(localStorage.getItem(props.storageKey) || '[]')
    checked.splice(0, checked.length, ...blank.map((value, index) => Boolean(saved[index])))
  } catch {
    checked.splice(0, checked.length, ...blank)
  }
})
</script>

<style scoped>
ul { list-style: none; margin: 0; padding: 0; display: grid; gap: 8px; }
label { display: flex; gap: 8px; align-items: flex-start; line-height: 1.5; }
input { margin-top: 4px; }
.progress { margin: 10px 0 0; font-size: 13px; color: var(--vp-c-text-2); }
</style>
