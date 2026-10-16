<template>
  <figure class="course-module shot-placeholder">
    <p class="module-kicker">截图待补</p>
    <p class="tool">应展示：{{ tool }}</p>
    <p class="caption">{{ caption }}</p>
    <figcaption>这里不是产品截图。仓库里没有这次操作的真实界面，所以留空，避免画一张假的控制台。</figcaption>
  </figure>
</template>

<script setup>
defineProps({
  tool: { type: String, required: true },
  caption: { type: String, required: true }
})
</script>

<style scoped>
.shot-placeholder {
  border-style: dashed;
  min-height: 140px;
}
.tool { margin: 0; font-weight: 700; }
.caption { margin: 6px 0 0; line-height: 1.55; }
figcaption { margin-top: 10px; font-size: 13px; color: var(--vp-c-text-2); }
</style>
