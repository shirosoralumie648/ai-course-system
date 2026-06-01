<template>
  <div class="progress-tracker">
    <div class="tracker-title" v-if="title">{{ title }}</div>
    <div class="tracker-items">
      <div v-for="(item, i) in items" :key="i"
           class="tracker-item" :class="{ done: item.done, current: i === currentIndex }">
        <div class="item-marker">
          <div class="marker-circle" :class="{ done: item.done, current: i === currentIndex }">
            <svg v-if="item.done" width="14" height="14" viewBox="0 0 24 24" fill="none">
              <path d="M20 6L9 17l-5-5" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>
            </svg>
            <span v-else>{{ i + 1 }}</span>
          </div>
          <div v-if="i < items.length - 1" class="marker-line" :class="{ done: item.done }"></div>
        </div>
        <div class="item-content">
          <div class="item-title">{{ item.title }}</div>
          <div class="item-desc" v-if="item.description">{{ item.description }}</div>
          <div class="item-status" v-if="item.done">
            <span class="status-badge done">已完成</span>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { computed } from 'vue'

const props = defineProps({
  title: { type: String, default: '' },
  items: {
    type: Array,
    default: () => []
  }
})

const currentIndex = computed(() => {
  const idx = props.items.findIndex(item => !item.done)
  return idx === -1 ? props.items.length - 1 : idx
})
</script>

<style scoped>
.progress-tracker {
  margin: 24px 0;
  padding: 24px;
  border: 1px solid var(--vp-c-default-3);
  border-radius: 12px;
  background: var(--vp-c-bg);
}
.tracker-title {
  font-size: 16px;
  font-weight: 700;
  margin-bottom: 20px;
  color: var(--vp-c-text-1);
}

.tracker-items {
  display: flex;
  flex-direction: column;
}

.tracker-item {
  display: flex;
  gap: 16px;
}

.item-marker {
  display: flex;
  flex-direction: column;
  align-items: center;
  flex-shrink: 0;
}

.marker-circle {
  width: 32px;
  height: 32px;
  border-radius: 50%;
  border: 2px solid var(--vp-c-default-3);
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 13px;
  font-weight: 700;
  color: var(--vp-c-text-3);
  background: var(--vp-c-bg);
  transition: all 0.3s ease;
}
.marker-circle.done {
  background: #22c55e;
  border-color: #22c55e;
  color: white;
}
.marker-circle.current {
  border-color: var(--vp-c-brand-1);
  color: var(--vp-c-brand-1);
  box-shadow: 0 0 0 3px var(--vp-c-brand-soft);
}

.marker-line {
  width: 2px;
  flex: 1;
  min-height: 24px;
  background: var(--vp-c-default-3);
  margin: 4px 0;
  transition: background 0.3s;
}
.marker-line.done { background: #22c55e; }

.item-content {
  flex: 1;
  padding-bottom: 20px;
}
.tracker-item:last-child .item-content { padding-bottom: 0; }

.item-title {
  font-size: 14px;
  font-weight: 600;
  color: var(--vp-c-text-1);
}
.tracker-item.done .item-title { color: var(--vp-c-text-2); }

.item-desc {
  font-size: 13px;
  color: var(--vp-c-text-3);
  margin-top: 4px;
  line-height: 1.5;
}

.status-badge {
  display: inline-block;
  font-size: 11px;
  font-weight: 700;
  padding: 2px 8px;
  border-radius: 4px;
  margin-top: 6px;
}
.status-badge.done {
  background: #dcfce7;
  color: #16a34a;
}
</style>
