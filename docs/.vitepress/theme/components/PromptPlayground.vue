<template>
  <div class="prompt-playground">
    <div class="playground-header">
      <span class="playground-icon">⚡</span>
      <span class="playground-title">{{ title }}</span>
    </div>

    <div class="playground-body">
      <div class="prompt-column">
        <div class="column-header">
          <span class="dot bad"></span>
          <span>{{ leftLabel }}</span>
        </div>
        <div class="prompt-box bad">
          <pre>{{ leftPrompt }}</pre>
        </div>
        <div class="output-box" v-if="leftOutput">
          <div class="output-label">AI 输出</div>
          <pre>{{ leftOutput }}</pre>
        </div>
      </div>

      <div class="vs-divider">
        <div class="vs-line"></div>
        <span class="vs-text">VS</span>
        <div class="vs-line"></div>
      </div>

      <div class="prompt-column">
        <div class="column-header">
          <span class="dot good"></span>
          <span>{{ rightLabel }}</span>
        </div>
        <div class="prompt-box good">
          <pre>{{ rightPrompt }}</pre>
        </div>
        <div class="output-box" v-if="rightOutput">
          <div class="output-label">AI 输出</div>
          <pre>{{ rightOutput }}</pre>
        </div>
      </div>
    </div>

    <div class="playground-footer" v-if="showAnalysis">
      <div class="analysis-title">对比分析</div>
      <div class="analysis-grid">
        <div v-for="(item, i) in analysis" :key="i" class="analysis-item">
          <div class="analysis-dimension">{{ item.dimension }}</div>
          <div class="analysis-bars">
            <div class="bar-wrapper">
              <div class="bar bad" :style="{ width: item.left + '%' }"></div>
              <span class="bar-value">{{ item.left }}</span>
            </div>
            <div class="bar-wrapper">
              <div class="bar good" :style="{ width: item.right + '%' }"></div>
              <span class="bar-value">{{ item.right }}</span>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
defineProps({
  title: { type: String, default: 'Prompt 对比' },
  leftLabel: { type: String, default: '模糊 Prompt' },
  rightLabel: { type: String, default: '结构化 Prompt' },
  leftPrompt: { type: String, required: true },
  rightPrompt: { type: String, required: true },
  leftOutput: { type: String, default: '' },
  rightOutput: { type: String, default: '' },
  showAnalysis: { type: Boolean, default: true },
  analysis: {
    type: Array,
    default: () => [
      { dimension: '具体性', left: 30, right: 85 },
      { dimension: '相关性', left: 40, right: 90 },
      { dimension: '可用性', left: 25, right: 80 }
    ]
  }
})
</script>

<style scoped>
.prompt-playground {
  border: 1px solid var(--vp-c-default-3);
  border-radius: 12px;
  overflow: hidden;
  margin: 24px 0;
  background: var(--vp-c-bg);
}

.playground-header {
  display: flex;
  align-items: center;
  gap: 8px;
  padding: 12px 20px;
  background: var(--vp-c-default-soft);
  border-bottom: 1px solid var(--vp-c-default-3);
  font-weight: 600;
  font-size: 15px;
}
.playground-icon { font-size: 18px; }

.playground-body {
  display: flex;
  gap: 0;
  padding: 20px;
}
@media (max-width: 768px) {
  .playground-body { flex-direction: column; }
}

.prompt-column { flex: 1; min-width: 0; }

.column-header {
  display: flex;
  align-items: center;
  gap: 8px;
  margin-bottom: 10px;
  font-size: 13px;
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 0.5px;
  color: var(--vp-c-text-2);
}

.dot {
  width: 10px;
  height: 10px;
  border-radius: 50%;
}
.dot.bad { background: #ef4444; }
.dot.good { background: #22c55e; }

.prompt-box {
  padding: 14px 16px;
  border-radius: 8px;
  font-size: 13px;
  line-height: 1.6;
}
.prompt-box.bad {
  background: #fef2f2;
  border: 1px solid #fecaca;
}
.prompt-box.good {
  background: #f0fdf4;
  border: 1px solid #bbf7d0;
}
.prompt-box pre {
  margin: 0;
  white-space: pre-wrap;
  word-break: break-word;
  font-family: var(--vp-font-family-base);
}

.output-box {
  margin-top: 10px;
  padding: 12px 16px;
  background: var(--vp-c-bg-soft);
  border-radius: 8px;
  font-size: 13px;
  line-height: 1.6;
  border: 1px solid var(--vp-c-default-3);
}
.output-label {
  font-size: 11px;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 1px;
  color: var(--vp-c-brand-1);
  margin-bottom: 6px;
}
.output-box pre {
  margin: 0;
  white-space: pre-wrap;
  word-break: break-word;
  font-family: var(--vp-font-family-base);
  color: var(--vp-c-text-2);
}

.vs-divider {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  padding: 0 16px;
  gap: 8px;
}
@media (max-width: 768px) {
  .vs-divider {
    flex-direction: row;
    padding: 12px 0;
  }
}
.vs-line {
  flex: 1;
  width: 1px;
  background: var(--vp-c-default-3);
}
@media (max-width: 768px) {
  .vs-line { width: auto; height: 1px; flex: 1; }
}
.vs-text {
  font-size: 12px;
  font-weight: 700;
  color: var(--vp-c-text-3);
  letter-spacing: 2px;
}

.playground-footer {
  padding: 16px 20px;
  border-top: 1px solid var(--vp-c-default-3);
  background: var(--vp-c-bg-soft);
}
.analysis-title {
  font-size: 13px;
  font-weight: 700;
  margin-bottom: 12px;
  color: var(--vp-c-text-1);
}
.analysis-grid {
  display: flex;
  flex-direction: column;
  gap: 10px;
}
.analysis-item {
  display: flex;
  align-items: center;
  gap: 12px;
}
.analysis-dimension {
  width: 70px;
  font-size: 12px;
  font-weight: 600;
  color: var(--vp-c-text-2);
  text-align: right;
  flex-shrink: 0;
}
.analysis-bars {
  flex: 1;
  display: flex;
  flex-direction: column;
  gap: 4px;
}
.bar-wrapper {
  display: flex;
  align-items: center;
  gap: 8px;
}
.bar {
  height: 8px;
  border-radius: 4px;
  transition: width 0.8s cubic-bezier(0.25, 1, 0.5, 1);
  min-width: 4px;
}
.bar.bad { background: #ef4444; }
.bar.good { background: #22c55e; }
.bar-value {
  font-size: 11px;
  font-weight: 600;
  color: var(--vp-c-text-3);
  width: 24px;
}
</style>
