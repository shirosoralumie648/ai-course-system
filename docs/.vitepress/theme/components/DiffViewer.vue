<template>
  <div class="diff-viewer">
    <div class="diff-header">
      <span class="diff-icon">📝</span>
      <span class="diff-title">{{ title }}</span>
      <div class="diff-stats">
        <span class="stat added">+{{ addedLines }}</span>
        <span class="stat removed">-{{ removedLines }}</span>
      </div>
    </div>
    <div class="diff-body">
      <div v-for="(line, i) in parsedLines" :key="i"
           class="diff-line" :class="line.type">
        <span class="line-number old">{{ line.oldNum || '' }}</span>
        <span class="line-number new">{{ line.newNum || '' }}</span>
        <span class="line-prefix">{{ line.prefix }}</span>
        <span class="line-content">{{ line.content }}</span>
      </div>
    </div>
  </div>
</template>

<script setup>
import { computed } from 'vue'

const props = defineProps({
  title: { type: String, default: '代码变更' },
  diff: { type: String, default: '' },
  // 支持 before/after 格式
  before: { type: Object, default: null },
  after: { type: Object, default: null },
  // 支持 oldCode/newCode 格式
  oldCode: { type: String, default: '' },
  newCode: { type: String, default: '' },
  language: { type: String, default: 'javascript' }
})

// 生成 diff 字符串
function generateDiff() {
  // 如果提供了 diff 属性，直接使用
  if (props.diff) return props.diff

  // 如果提供了 before/after 格式
  if (props.before && props.after) {
    const oldLines = props.before.code.split('\n')
    const newLines = props.after.code.split('\n')
    return generateDiffFromLines(oldLines, newLines)
  }

  // 如果提供了 oldCode/newCode 格式
  if (props.oldCode || props.newCode) {
    const oldLines = props.oldCode.split('\n')
    const newLines = props.newCode.split('\n')
    return generateDiffFromLines(oldLines, newLines)
  }

  return ''
}

// 简单的 diff 生成算法
function generateDiffFromLines(oldLines, newLines) {
  const result = [`@@ -1,${oldLines.length} +1,${newLines.length} @@`]
  const maxLen = Math.max(oldLines.length, newLines.length)

  for (let i = 0; i < maxLen; i++) {
    const oldLine = oldLines[i]
    const newLine = newLines[i]

    if (oldLine === newLine && oldLine !== undefined) {
      result.push(' ' + oldLine)
    } else {
      if (oldLine !== undefined) result.push('-' + oldLine)
      if (newLine !== undefined) result.push('+' + newLine)
    }
  }

  return result.join('\n')
}

const parsedLines = computed(() => {
  const diffText = generateDiff()
  if (!diffText) return []

  const lines = diffText.split('\n')
  const result = []
  let oldNum = 0
  let newNum = 0

  for (const line of lines) {
    if (line.startsWith('@@')) {
      const match = line.match(/@@ -(\d+),?\d* \+(\d+),?\d* @@/)
      if (match) {
        oldNum = parseInt(match[1])
        newNum = parseInt(match[2])
      }
      result.push({ type: 'hunk', content: line, prefix: '@', oldNum: '', newNum: '' })
    } else if (line.startsWith('+')) {
      result.push({ type: 'added', content: line.slice(1), prefix: '+', oldNum: '', newNum: newNum++ })
    } else if (line.startsWith('-')) {
      result.push({ type: 'removed', content: line.slice(1), prefix: '-', oldNum: oldNum++, newNum: '' })
    } else {
      result.push({ type: 'context', content: line.slice(1) || '', prefix: ' ', oldNum: oldNum++, newNum: newNum++ })
    }
  }
  return result
})

const addedLines = computed(() => parsedLines.value.filter(l => l.type === 'added').length)
const removedLines = computed(() => parsedLines.value.filter(l => l.type === 'removed').length)
</script>

<style scoped>
.diff-viewer {
  border: 1px solid var(--vp-c-default-3);
  border-radius: 10px;
  overflow: hidden;
  margin: 20px 0;
  font-family: var(--vp-font-family-mono);
}

.diff-header {
  display: flex;
  align-items: center;
  gap: 8px;
  padding: 10px 16px;
  background: var(--vp-c-default-soft);
  border-bottom: 1px solid var(--vp-c-default-3);
  font-size: 13px;
  font-weight: 600;
}
.diff-icon { font-size: 16px; }
.diff-title { flex: 1; }
.diff-stats { display: flex; gap: 10px; }
.stat { font-size: 12px; font-weight: 700; }
.stat.added { color: #22c55e; }
.stat.removed { color: #ef4444; }

.diff-body {
  overflow-x: auto;
  font-size: 13px;
  line-height: 1.6;
}

.diff-line {
  display: flex;
  padding: 0 12px;
  white-space: pre;
  min-height: 22px;
}
.diff-line.added {
  background: #dcfce7;
}
.diff-line.removed {
  background: #fee2e2;
}
.diff-line.hunk {
  background: var(--vp-c-brand-soft);
  color: var(--vp-c-text-3);
  font-size: 12px;
  padding: 4px 12px;
}

.line-number {
  width: 40px;
  text-align: right;
  padding-right: 8px;
  color: var(--vp-c-text-3);
  user-select: none;
  flex-shrink: 0;
  font-size: 12px;
}

.line-prefix {
  width: 16px;
  text-align: center;
  flex-shrink: 0;
  font-weight: 700;
}
.diff-line.added .line-prefix { color: #16a34a; }
.diff-line.removed .line-prefix { color: #dc2626; }

.line-content {
  flex: 1;
  padding-left: 4px;
  min-width: 0;
}
</style>
