<template>
  <div class="risk-matrix">
    <div class="matrix-title" v-if="title">{{ title }}</div>
    <div class="matrix-grid">
      <div class="matrix-y-label">
        <span>影响程度</span>
        <div class="y-labels">
          <span>高</span>
          <span>中</span>
          <span>低</span>
        </div>
      </div>
      <div class="matrix-cells">
        <div v-for="row in 3" :key="row" class="matrix-row">
          <div v-for="col in 3" :key="col" class="matrix-cell"
               :class="getCellClass(row, col)"
               @click="selectCell(row, col)">
            <div v-for="(risk, i) in getRisksInCell(row, col)" :key="i"
                 class="risk-dot" :title="risk.name">
              {{ risk.icon || '⚠' }}
            </div>
          </div>
        </div>
        <div class="matrix-x-label">
          <span>低</span>
          <span>中</span>
          <span>高</span>
          <span class="x-label-text">发生概率</span>
        </div>
      </div>
    </div>

    <div class="risk-legend" v-if="risks.length > 0">
      <div v-for="(risk, i) in risks" :key="i" class="legend-item"
           :class="{ active: selectedRisk === i }"
           @click="selectedRisk = i">
        <span class="legend-icon" :style="{ background: risk.color || '#ef4444' }">{{ risk.icon || '⚠' }}</span>
        <div class="legend-info">
          <div class="legend-name">{{ risk.name }}</div>
          <div class="legend-desc">{{ risk.description }}</div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'

const props = defineProps({
  title: { type: String, default: '风险矩阵' },
  risks: {
    type: Array,
    default: () => []
  }
})

const selectedRisk = ref(null)

function getCellClass(row, col) {
  const level = (3 - row) * 3 + col
  if (level <= 3) return 'low'
  if (level <= 6) return 'medium'
  return 'high'
}

function getRisksInCell(row, col) {
  return props.risks.filter(r => {
    const rRow = 3 - Math.floor((r.impact - 1) / 1)
    const rCol = r.probability
    return rRow === row && rCol === col
  })
}

function selectCell(row, col) {
  // Could emit events for interactive risk placement
}
</script>

<style scoped>
.risk-matrix {
  margin: 24px 0;
  padding: 24px;
  border: 1px solid var(--vp-c-default-3);
  border-radius: 12px;
  background: var(--vp-c-bg);
}
.matrix-title {
  font-size: 16px;
  font-weight: 700;
  margin-bottom: 20px;
  color: var(--vp-c-text-1);
}

.matrix-grid {
  display: flex;
  gap: 12px;
}

.matrix-y-label {
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  padding: 0 8px;
  font-size: 12px;
  font-weight: 600;
  color: var(--vp-c-text-2);
  writing-mode: vertical-lr;
  text-orientation: mixed;
  transform: rotate(180deg);
}
.y-labels {
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  flex: 1;
  writing-mode: horizontal-tb;
  transform: rotate(180deg);
  font-weight: 400;
  color: var(--vp-c-text-3);
}

.matrix-cells {
  flex: 1;
  max-width: 360px;
}

.matrix-row {
  display: flex;
  gap: 4px;
  margin-bottom: 4px;
}

.matrix-cell {
  flex: 1;
  aspect-ratio: 1.6;
  border-radius: 8px;
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  justify-content: center;
  gap: 4px;
  padding: 8px;
  cursor: pointer;
  transition: all 0.2s;
  min-height: 60px;
}
.matrix-cell:hover { transform: scale(1.02); }
.matrix-cell.low { background: #dcfce7; border: 1px solid #bbf7d0; }
.matrix-cell.medium { background: #fef3c7; border: 1px solid #fde68a; }
.matrix-cell.high { background: #fee2e2; border: 1px solid #fecaca; }

.risk-dot {
  font-size: 18px;
  cursor: help;
  transition: transform 0.2s;
}
.risk-dot:hover { transform: scale(1.3); }

.matrix-x-label {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding-top: 8px;
  font-size: 12px;
  color: var(--vp-c-text-3);
}
.x-label-text {
  font-weight: 600;
  color: var(--vp-c-text-2);
}

.risk-legend {
  margin-top: 20px;
  display: flex;
  flex-direction: column;
  gap: 8px;
}
.legend-item {
  display: flex;
  align-items: center;
  gap: 12px;
  padding: 10px 14px;
  border-radius: 8px;
  border: 1px solid var(--vp-c-default-3);
  cursor: pointer;
  transition: all 0.2s;
}
.legend-item:hover, .legend-item.active {
  border-color: var(--vp-c-brand-1);
  background: var(--vp-c-brand-soft);
}

.legend-icon {
  width: 28px;
  height: 28px;
  border-radius: 6px;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 14px;
  flex-shrink: 0;
}
.legend-name {
  font-size: 13px;
  font-weight: 600;
  color: var(--vp-c-text-1);
}
.legend-desc {
  font-size: 12px;
  color: var(--vp-c-text-3);
}
</style>
