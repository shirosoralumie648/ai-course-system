<template>
  <div class="info-card" :class="variant">
    <div v-if="title" class="info-card-title">
      <span v-if="icon" class="info-card-icon">{{ icon }}</span>
      {{ title }}
    </div>
    <div class="info-card-body"><slot /></div>
  </div>
</template>

<script setup>
defineProps({
  title: { type: String, default: '' },
  icon: { type: String, default: '' },
  variant: { type: String, default: 'default' } // default, tip, warning, danger
})
</script>

<style scoped>
.info-card {
  margin: 16px 0; padding: 16px 20px; border-radius: 8px;
  border-left: 4px solid var(--vp-c-brand);
  background-color: var(--vp-c-bg-soft);
}
.info-card.tip { border-left-color: #42d392; background-color: rgba(66, 211, 146, 0.06); }
.info-card.warning { border-left-color: #e7c000; background-color: rgba(231, 192, 0, 0.06); }
.info-card.danger { border-left-color: #cc0000; background-color: rgba(204, 0, 0, 0.06); }
.info-card-title { font-weight: 700; margin-bottom: 8px; display: flex; align-items: center; gap: 6px; }
.info-card-icon { font-size: 1.1em; }
.info-card-body { font-size: 0.95em; line-height: 1.6; }
</style>
