<template>
  <div class="ai-chat-message-wrapper">
    <slot></slot>
  </div>
</template>

<script setup>
defineProps({
  role: { type: String, required: true },
  variant: { type: String, default: '' }
})
</script>

<style scoped>
.ai-chat-message-wrapper {
  display: contents;
}
</style>
