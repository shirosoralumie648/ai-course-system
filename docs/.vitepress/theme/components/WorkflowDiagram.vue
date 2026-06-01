<template>
  <div class="workflow-diagram">
    <div class="workflow-title" v-if="title">{{ title }}</div>
    <div class="workflow-steps">
      <div v-for="(step, i) in steps" :key="i"
           class="workflow-step"
           :class="[step.type, { active: activeStep === i }]"
           @click="activeStep = i">
        <div class="step-number">{{ i + 1 }}</div>
        <div class="step-content">
          <div class="step-name">{{ step.name }}</div>
          <div class="step-desc">{{ step.description }}</div>
        </div>
        <div class="step-badge" :class="step.type">{{ badgeLabel(step.type) }}</div>
      </div>
      <div v-if="i < steps.length - 1" v-for="(_, i) in steps.length - 1" :key="'arrow-' + i" class="workflow-arrow">
        <svg width="24" height="24" viewBox="0 0 24 24" fill="none">
          <path d="M12 5v14M19 12l-7 7-7-7" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
        </svg>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'

const props = defineProps({
  title: { type: String, default: '' },
  steps: {
    type: Array,
    default: () => []
  }
})

const activeStep = ref(0)

function badgeLabel(type) {
  const map = { ai: 'AI 独立', assist: 'AI 辅助', human: '人工完成' }
  return map[type] || type
}
</script>

<style scoped>
.workflow-diagram {
  margin: 24px 0;
  padding: 24px;
  border: 1px solid var(--vp-c-default-3);
  border-radius: 12px;
  background: var(--vp-c-bg);
}
.workflow-title {
  font-size: 16px;
  font-weight: 700;
  margin-bottom: 20px;
  color: var(--vp-c-text-1);
}

.workflow-steps {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 0;
}

.workflow-step {
  display: flex;
  align-items: center;
  gap: 14px;
  padding: 14px 18px;
  border-radius: 10px;
  border: 2px solid var(--vp-c-default-3);
  background: var(--vp-c-bg);
  cursor: pointer;
  transition: all 0.25s ease;
  width: 100%;
  max-width: 420px;
}
.workflow-step:hover {
  border-color: var(--vp-c-brand-1);
  box-shadow: 0 2px 12px rgba(0,0,0,0.06);
}
.workflow-step.active {
  border-color: var(--vp-c-brand-1);
  background: var(--vp-c-brand-soft);
}

.workflow-step.ai { border-left: 4px solid #8b5cf6; }
.workflow-step.assist { border-left: 4px solid #f59e0b; }
.workflow-step.human { border-left: 4px solid #22c55e; }
.workflow-step.ai.active { background: #f5f3ff; }
.workflow-step.assist.active { background: #fffbeb; }
.workflow-step.human.active { background: #f0fdf4; }

.step-number {
  width: 32px;
  height: 32px;
  border-radius: 50%;
  background: var(--vp-c-default-soft);
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 14px;
  font-weight: 700;
  color: var(--vp-c-text-1);
  flex-shrink: 0;
}
.workflow-step.active .step-number {
  background: var(--vp-c-brand-1);
  color: white;
}

.step-content { flex: 1; min-width: 0; }
.step-name {
  font-size: 14px;
  font-weight: 600;
  color: var(--vp-c-text-1);
}
.step-desc {
  font-size: 12px;
  color: var(--vp-c-text-3);
  margin-top: 2px;
}

.step-badge {
  font-size: 11px;
  font-weight: 700;
  padding: 3px 8px;
  border-radius: 4px;
  flex-shrink: 0;
}
.step-badge.ai { background: #ede9fe; color: #7c3aed; }
.step-badge.assist { background: #fef3c7; color: #d97706; }
.step-badge.human { background: #dcfce7; color: #16a34a; }

.workflow-arrow {
  color: var(--vp-c-text-3);
  padding: 4px 0;
  opacity: 0.5;
}
</style>
