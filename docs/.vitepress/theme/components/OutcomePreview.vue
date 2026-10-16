<template>
  <section class="course-module outcome-preview">
    <p class="module-kicker">本周产出物预览</p>
    <ul>
      <li v-for="(item, index) in items" :key="index">
        <strong>{{ item.title }}</strong>
        <span>{{ item.detail }}</span>
      </li>
    </ul>
  </section>
</template>

<script setup>
defineProps({
  items: { type: Array, default: () => [] }
})
</script>

<style scoped>
ul { list-style: none; margin: 0; padding: 0; display: grid; gap: 10px; }
li { display: grid; gap: 2px; }
span { color: var(--vp-c-text-2); font-size: 14px; line-height: 1.55; }
</style>
