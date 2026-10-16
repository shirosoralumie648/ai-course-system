<template>
  <section class="course-module">
    <p class="module-kicker">动手试一试</p>
    <p class="hint">{{ hint }}</p>
    <pre><code>{{ command }}</code></pre>
    <p class="module-kicker expected">期望输出</p>
    <pre><code><slot /></code></pre>
  </section>
</template>

<script setup>
defineProps({
  command: { type: String, required: true },
  hint: { type: String, default: '在本地终端运行。输出应和下面这段一致。' }
})
</script>

<style scoped>
.hint { margin: 0; font-size: 14px; color: var(--vp-c-text-2); }
.expected { margin-top: 12px; }
pre { white-space: pre-wrap; }
</style>
