<template>
  <div class="mermaid-chart">
    <div ref="canvas" class="mermaid-chart__canvas" />
    <div v-if="error" class="mermaid-chart__error">
      <strong>Mermaid 图渲染失败</strong>
      <span>{{ error }}</span>
      <pre>{{ source }}</pre>
    </div>
  </div>
</template>

<script setup>
import { computed, onBeforeUnmount, onMounted, ref, watch } from 'vue'

const props = defineProps({
  code: {
    type: String,
    required: true
  }
})

const canvas = ref(null)
const error = ref('')
const source = computed(() => {
  try {
    return decodeURIComponent(props.code).trim()
  } catch {
    return props.code.trim()
  }
})

let renderRun = 0
let disposed = false
let themeObserver

const getTheme = () =>
  document.documentElement.classList.contains('dark') ? 'dark' : 'default'

async function renderChart() {
  if (!canvas.value) return

  const currentRun = ++renderRun
  error.value = ''
  canvas.value.innerHTML = ''

  try {
    const { default: mermaid } = await import('mermaid')

    if (disposed || currentRun !== renderRun || !canvas.value) return

    mermaid.initialize({
      startOnLoad: false,
      securityLevel: 'strict',
      theme: getTheme()
    })

    const id = `mermaid-${Date.now()}-${currentRun}-${Math.random().toString(36).slice(2)}`
    const { svg, bindFunctions } = await mermaid.render(id, source.value)

    if (disposed || currentRun !== renderRun || !canvas.value) return

    canvas.value.innerHTML = svg
    bindFunctions?.(canvas.value)
  } catch (err) {
    if (!canvas.value) return
    canvas.value.innerHTML = ''
    error.value = err instanceof Error ? err.message : String(err)
  }
}

onMounted(() => {
  renderChart()

  themeObserver = new MutationObserver(() => {
    renderChart()
  })

  themeObserver.observe(document.documentElement, {
    attributes: true,
    attributeFilter: ['class']
  })
})

watch(() => props.code, renderChart)

onBeforeUnmount(() => {
  disposed = true
  themeObserver?.disconnect()
})
</script>
