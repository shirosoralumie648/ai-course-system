<template>
  <div class="chapter-intro">
    <div class="objective-section">
      <div class="objective-label">
        <span class="icon">🎯</span>
        <span class="title">学习目标</span>
      </div>
      <div class="content">
        <div v-if="tags.length" class="tags-container">
          <span v-for="(tag, i) in tags" :key="i" class="tag">{{ tag }}</span>
        </div>
        <div class="description"><slot /></div>
      </div>
    </div>
    <div v-if="duration || output" class="metrics-grid">
      <div v-if="duration" class="metric-card">
        <div class="card-icon">⏱️</div>
        <div class="card-content">
          <div class="card-label">预计时长</div>
          <div class="card-value">{{ duration }}</div>
        </div>
      </div>
      <div v-if="output" class="metric-card">
        <div class="card-icon">📦</div>
        <div class="card-content">
          <div class="card-label">核心产出</div>
          <div class="card-value">{{ output }}</div>
        </div>
      </div>
      <div v-if="prerequisite" class="metric-card">
        <div class="card-icon">📋</div>
        <div class="card-content">
          <div class="card-label">前置条件</div>
          <div class="card-value">{{ prerequisite }}</div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
defineProps({
  duration: { type: String, default: '' },
  output: { type: String, default: '' },
  prerequisite: { type: String, default: '' },
  tags: { type: Array, default: () => [] }
})
</script>

<style scoped>
.chapter-intro {
  margin: 16px 0;
  border-radius: 12px;
  background-color: var(--vp-c-bg-soft);
  border: 1px solid var(--vp-c-divider);
  overflow: hidden;
  box-shadow: 0 2px 12px rgba(0, 0, 0, 0.04);
}
.objective-section {
  padding: 16px 20px;
  background: linear-gradient(to right, rgba(var(--vp-c-brand-rgb), 0.05), transparent);
  border-bottom: 1px dashed var(--vp-c-divider);
}
.objective-label {
  display: flex;
  align-items: center;
  margin-bottom: 10px;
  color: var(--vp-c-brand);
}
.icon { font-size: 1.2em; margin-right: 6px; }
.title { font-size: 0.95em; font-weight: 700; text-transform: uppercase; letter-spacing: 0.5px; }
.tags-container { display: flex; flex-wrap: wrap; gap: 8px; margin-bottom: 10px; }
.tag {
  display: inline-flex;
  padding: 4px 10px;
  background-color: var(--vp-c-bg-alt);
  border: 1px solid var(--vp-c-divider);
  border-radius: 99px;
  font-size: 0.9em;
  font-weight: 600;
  color: var(--vp-c-text-1);
}
.description { font-size: 1em; line-height: 1.5; color: var(--vp-c-text-1); }
.metrics-grid {
  display: flex;
  flex-wrap: wrap;
  gap: 1px;
  background-color: var(--vp-c-divider);
  border-top: 1px solid var(--vp-c-divider);
}
.metric-card {
  flex: 1 1 200px;
  background-color: var(--vp-c-bg-soft);
  padding: 14px 18px;
  display: flex;
  align-items: flex-start;
  gap: 16px;
}
.card-icon { font-size: 1.4em; line-height: 1; padding-top: 2px; }
.card-content { flex: 1; display: flex; flex-direction: column; }
.card-label { font-size: 0.8em; color: var(--vp-c-text-2); margin-bottom: 4px; font-weight: 600; text-transform: uppercase; }
.card-value { font-size: 0.95em; line-height: 1.4; color: var(--vp-c-text-1); }
@media (max-width: 640px) {
  .metric-card { padding: 12px 16px; flex-basis: 100%; }
}
</style>
