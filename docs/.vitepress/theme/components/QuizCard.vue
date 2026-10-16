<template>
  <section class="course-module">
    <p class="module-kicker">知识点小测</p>
    <p class="question">{{ question }}</p>
    <details>
      <summary>查看答案</summary>
      <div class="answer"><slot /></div>
    </details>
  </section>
</template>

<script setup>
defineProps({
  question: { type: String, required: true }
})
</script>

<style scoped>
.question { margin: 0 0 8px; font-weight: 650; line-height: 1.55; }
summary { cursor: pointer; color: var(--vp-c-brand); }
.answer { margin-top: 8px; line-height: 1.6; }
</style>
