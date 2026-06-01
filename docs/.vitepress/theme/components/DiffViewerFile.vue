<template>
  <div class="diff-viewer-file">
    <slot />
  </div>
</template>

<script setup>
defineProps({
  path: { type: String, default: '' }
})
</script>

<style scoped>
.diff-viewer-file {
  /* 样式由父组件 DiffViewer 控制 */
}
</style>
