<template>
  <div class="diff-viewer-hunk">
    <slot />
  </div>
</template>

<script setup>
// 这是一个虚拟组件，用于在 markdown 中包裹 diff 代码块
</script>

<style scoped>
.diff-viewer-hunk {
  /* 样式由父组件控制 */
}
</style>
