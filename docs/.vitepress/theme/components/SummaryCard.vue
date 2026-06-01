<template>
  <div class="summary-card">
    <div class="summary-header">
      <div class="header-icon">📚</div>
      <div class="summary-title">{{ title }}</div>
    </div>
    <div class="summary-body">
      <div v-if="sections.length" class="sections-container">
        <div v-for="(section, i) in sections" :key="i" class="section-item">
          <div class="section-header">
            <span class="section-number">{{ section.number }}</span>
            <span class="section-title">{{ section.title }}</span>
          </div>
          <ul class="section-list">
            <li v-for="(item, j) in section.items" :key="j" class="list-item">
              <span class="item-marker">•</span>
              <span class="item-content" v-html="item" />
            </li>
          </ul>
        </div>
      </div>
      <div v-if="outputs.length" class="outputs-section">
        <div class="outputs-header">
          <span>📦</span>
          <span class="outputs-title">本章产出：</span>
        </div>
        <ul class="outputs-list">
          <li v-for="(output, i) in outputs" :key="i" class="output-item">
            <span class="output-marker">✓</span>
            <span class="output-content" v-html="output" />
          </li>
        </ul>
      </div>
    </div>
  </div>
</template>

<script setup>
defineProps({
  title: { type: String, default: '本章小结' },
  sections: { type: Array, default: () => [] },
  outputs: { type: Array, default: () => [] }
})
</script>

<style scoped>
.summary-card {
  margin: 14px 0;
  border-radius: 14px;
  background: linear-gradient(160deg, rgba(var(--vp-c-brand-rgb), 0.06) 0%, rgba(var(--vp-c-brand-rgb), 0.015) 40%, var(--vp-c-bg) 100%);
  border: 1px solid rgba(var(--vp-c-brand-rgb), 0.12);
  overflow: hidden;
  box-shadow: 0 8px 24px rgba(0, 0, 0, 0.06);
}
.summary-header {
  display: flex;
  align-items: center;
  gap: 10px;
  padding: 10px 14px;
  background: linear-gradient(120deg, rgba(var(--vp-c-brand-rgb), 0.16), rgba(var(--vp-c-brand-rgb), 0.04));
  border-bottom: 1px solid rgba(var(--vp-c-brand-rgb), 0.16);
}
.header-icon {
  width: 30px; height: 30px; border-radius: 10px;
  display: inline-flex; align-items: center; justify-content: center;
  font-size: 1.1em;
  background: rgba(var(--vp-c-brand-rgb), 0.18);
}
.summary-title { font-size: 1em; font-weight: 700; color: var(--vp-c-text-1); }
.summary-body { padding: 12px 14px 14px; }
.sections-container { display: flex; flex-direction: column; gap: 10px; }
.section-item {
  background: var(--vp-c-bg); border-radius: 12px; padding: 10px 12px;
  border: 1px solid rgba(var(--vp-c-brand-rgb), 0.12);
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.04);
}
.section-header { display: flex; align-items: center; gap: 8px; margin-bottom: 8px; }
.section-number {
  display: inline-flex; align-items: center; justify-content: center;
  min-width: 24px; height: 24px; padding: 0 7px;
  background: linear-gradient(135deg, var(--vp-c-brand), var(--vp-c-brand-dark));
  color: white; border-radius: 999px; font-size: 0.74em; font-weight: 700;
}
.section-title { font-size: 0.95em; font-weight: 700; color: var(--vp-c-text-1); }
.section-list { list-style: none; padding: 0; margin: 0; display: flex; flex-direction: column; gap: 4px; }
.list-item { display: flex; align-items: baseline; gap: 8px; padding: 3px 0; line-height: 1.45; }
.item-marker { color: var(--vp-c-brand); font-weight: 700; font-size: 0.9em; flex-shrink: 0; }
.item-content { color: var(--vp-c-text-1); font-size: 0.92em; line-height: 1.55; }
.outputs-section {
  margin-top: 12px; padding: 10px 12px 8px; border-radius: 12px;
  background: rgba(var(--vp-c-brand-rgb), 0.06);
  border: 1px dashed rgba(var(--vp-c-brand-rgb), 0.25);
}
.outputs-header { display: flex; align-items: center; gap: 6px; margin-bottom: 8px; }
.outputs-title { font-size: 0.9em; font-weight: 700; color: var(--vp-c-text-1); }
.outputs-list { list-style: none; padding: 0; margin: 0; display: flex; flex-direction: column; gap: 4px; }
.output-item { display: flex; align-items: baseline; gap: 8px; padding: 2px 0; }
.output-marker {
  color: #42d392; font-weight: 700; font-size: 0.85em; flex-shrink: 0;
  width: 18px; height: 18px; border-radius: 6px;
  display: inline-flex; align-items: center; justify-content: center;
  background: rgba(66, 211, 146, 0.12);
}
.output-content { color: var(--vp-c-text-1); font-size: 0.92em; line-height: 1.55; }
</style>
