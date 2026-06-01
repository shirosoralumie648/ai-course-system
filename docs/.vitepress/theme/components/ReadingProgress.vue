<template>
  <div class="reading-progress" v-if="visible" :style="positionStyle"
       @mousedown="startDrag" @touchstart.prevent="startDrag">
    <svg class="progress-ring" viewBox="0 0 56 56">
      <circle class="progress-ring-bg" cx="28" cy="28" r="24" />
      <circle class="progress-ring-circle" cx="28" cy="28" r="24"
        :style="{ strokeDashoffset: circumference - (progress / 100) * circumference }" />
    </svg>
    <div class="progress-content">
      <Transition name="fade" mode="out-in">
        <span v-if="showArrow" class="progress-arrow" @click.stop="scrollToTop">↑</span>
        <span v-else class="progress-text">{{ Math.round(progress) }}%</span>
      </Transition>
    </div>
  </div>
</template>

<script setup>
import { ref, computed, onMounted, onUnmounted } from 'vue'

const visible = ref(false)
const progress = ref(0)
const showArrow = ref(false)
const dragging = ref(false)
const posX = ref(24)
const posY = ref(24)
let hideTimer = null

const circumference = 2 * Math.PI * 24

const positionStyle = computed(() => ({
  right: `${posX.value}px`,
  bottom: `${posY.value}px`
}))

function updateProgress() {
  const scrollTop = window.scrollY
  const docHeight = document.documentElement.scrollHeight - window.innerHeight
  progress.value = docHeight > 0 ? (scrollTop / docHeight) * 100 : 0
  visible.value = scrollTop > 200

  showArrow.value = false
  clearTimeout(hideTimer)
  hideTimer = setTimeout(() => {
    if (progress.value > 5) showArrow.value = true
  }, 1500)
}

function scrollToTop() {
  window.scrollTo({ top: 0, behavior: 'smooth' })
}

function startDrag(e) {
  dragging.value = true
  const startY = e.clientY || e.touches?.[0]?.clientY
  const startScroll = window.scrollY
  const docHeight = document.documentElement.scrollHeight - window.innerHeight

  function onMove(ev) {
    const currentY = ev.clientY || ev.touches?.[0]?.clientY
    const delta = startY - currentY
    const scrollDelta = (delta / 3) * (docHeight / 100)
    window.scrollTo(0, startScroll + scrollDelta)
  }

  function onEnd() {
    dragging.value = false
    document.removeEventListener('mousemove', onMove)
    document.removeEventListener('mouseup', onEnd)
    document.removeEventListener('touchmove', onMove)
    document.removeEventListener('touchend', onEnd)
  }

  document.addEventListener('mousemove', onMove)
  document.addEventListener('mouseup', onEnd)
  document.addEventListener('touchmove', onMove)
  document.addEventListener('touchend', onEnd)
}

onMounted(() => {
  window.addEventListener('scroll', updateProgress, { passive: true })
  updateProgress()
})

onUnmounted(() => {
  window.removeEventListener('scroll', updateProgress)
  clearTimeout(hideTimer)
})
</script>

<style scoped>
.reading-progress {
  position: fixed;
  z-index: 100;
  width: 52px;
  height: 52px;
  cursor: grab;
  user-select: none;
  transition: opacity 0.3s;
}
.reading-progress:active { cursor: grabbing; }

.progress-ring {
  width: 100%;
  height: 100%;
  transform: rotate(-90deg);
}
.progress-ring-bg {
  fill: none;
  stroke: var(--vp-c-default-soft);
  stroke-width: 4;
}
.progress-ring-circle {
  fill: none;
  stroke: var(--vp-c-brand-1);
  stroke-width: 4;
  stroke-linecap: round;
  transition: stroke-dashoffset 0.15s ease-out;
  stroke-dasharray: v-bind(circumference);
}

.progress-content {
  position: absolute;
  inset: 0;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 12px;
  font-weight: 600;
  color: var(--vp-c-brand-1);
}
.progress-arrow {
  font-size: 18px;
  animation: bounce 1s ease-in-out infinite;
  cursor: pointer;
}
@keyframes bounce {
  0%, 100% { transform: translateY(0); }
  50% { transform: translateY(-3px); }
}

.fade-enter-active, .fade-leave-active { transition: opacity 0.2s; }
.fade-enter-from, .fade-leave-to { opacity: 0; }
</style>
