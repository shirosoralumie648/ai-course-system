<template>
  <span class="text-type" ref="containerRef">
    <span class="text-type__content" :style="{ color: currentColor || 'inherit' }">
      {{ displayedText }}
    </span>
    <span v-if="showCursor" class="text-type__cursor"
          :class="{ 'text-type__cursor--hidden': shouldHideCursor }"
          :style="cursorStyle">
      {{ cursorCharacter }}
    </span>
  </span>
</template>

<script setup>
import { ref, computed, onMounted, onUnmounted, watch } from 'vue'

const props = defineProps({
  text: { type: [String, Array], default: '' },
  typingSpeed: { type: Number, default: 80 },
  deletingSpeed: { type: Number, default: 40 },
  pauseDuration: { type: Number, default: 2000 },
  loop: { type: Boolean, default: true },
  showCursor: { type: Boolean, default: true },
  cursorCharacter: { type: String, default: '|' },
  cursorColor: { type: String, default: '' },
  textColors: { type: Array, default: () => [] },
  startOnVisible: { type: Boolean, default: true }
})

const displayedText = ref('')
const currentIndex = ref(0)
const isDeleting = ref(false)
const containerRef = ref(null)
const isVisible = ref(!props.startOnVisible)
let timer = null

const texts = computed(() => Array.isArray(props.text) ? props.text : [props.text])
const currentColor = computed(() => props.textColors.length > 0 ? props.textColors[currentIndex.value % props.textColors.length] : '')
const shouldHideCursor = computed(() => !props.loop && currentIndex.value >= texts.value.length && !isDeleting.value)
const cursorStyle = computed(() => props.cursorColor ? { color: props.cursorColor } : {})

function animate() {
  const current = texts.value[currentIndex.value] || ''

  if (!isDeleting.value) {
    displayedText.value = current.slice(0, displayedText.value.length + 1)

    if (displayedText.value === current) {
      if (currentIndex.value >= texts.value.length - 1 && !props.loop) {
        return
      }
      timer = setTimeout(() => { isDeleting.value = true; animate() }, props.pauseDuration)
      return
    }
    timer = setTimeout(animate, props.typingSpeed + Math.random() * 40)
  } else {
    displayedText.value = current.slice(0, displayedText.value.length - 1)

    if (displayedText.value === '') {
      isDeleting.value = false
      currentIndex.value = (currentIndex.value + 1) % texts.value.length
      timer = setTimeout(animate, 300)
      return
    }
    timer = setTimeout(animate, props.deletingSpeed)
  }
}

let observer = null
onMounted(() => {
  if (props.startOnVisible && containerRef.value) {
    observer = new IntersectionObserver(([entry]) => {
      if (entry.isIntersecting && !isVisible.value) {
        isVisible.value = true
        animate()
      }
    }, { threshold: 0.1 })
    observer.observe(containerRef.value)
  } else {
    animate()
  }
})

onUnmounted(() => {
  clearTimeout(timer)
  observer?.disconnect()
})
</script>

<style scoped>
.text-type {
  display: inline;
}
.text-type__cursor {
  display: inline-block;
  margin-left: 1px;
  font-weight: 300;
  animation: text-type-blink 0.7s infinite;
}
.text-type__cursor--hidden {
  display: none;
}
@keyframes text-type-blink {
  from { opacity: 1; }
  to { opacity: 0; }
}
</style>
