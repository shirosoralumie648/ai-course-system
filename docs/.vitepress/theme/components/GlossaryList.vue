<template>
  <section class="course-module">
    <p class="module-kicker">术语</p>
    <dl>
      <template v-for="(item, index) in terms" :key="index">
        <dt>{{ item.term }}</dt>
        <dd>{{ item.def }}</dd>
      </template>
    </dl>
  </section>
</template>

<script setup>
defineProps({
  terms: { type: Array, default: () => [] }
})
</script>

<style scoped>
dl { margin: 0; display: grid; grid-template-columns: 9em 1fr; gap: 8px 12px; }
dt { font-weight: 700; }
dd { margin: 0; color: var(--vp-c-text-2); line-height: 1.5; }
@media (max-width: 640px) {
  dl { grid-template-columns: 1fr; }
}
</style>
