<template>
  <div class="feature-cards">
    <div v-for="(card, i) in cards" :key="i"
         class="feature-card"
         :class="{ visible: visibleCards[i] }"
         :ref="el => setCardRef(el, i)">
      <div class="card-icon" :style="{ background: card.gradient }">
        <span>{{ card.icon }}</span>
      </div>
      <div class="card-body">
        <div class="card-tag" v-if="card.tag">{{ card.tag }}</div>
        <h3 class="card-title">{{ card.title }}</h3>
        <p class="card-desc">{{ card.description }}</p>
        <a v-if="card.link" :href="withBase(card.link)" class="card-link">
          {{ card.linkText || '了解更多' }} →
        </a>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, onUnmounted } from 'vue'
import { withBase } from 'vitepress'

defineProps({
  cards: {
    type: Array,
    default: () => []
  }
})

const visibleCards = ref([])
const cardRefs = ref([])
let observer = null

function setCardRef(el, i) {
  if (el) cardRefs.value[i] = el
}

onMounted(() => {
  observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      const idx = cardRefs.value.indexOf(entry.target)
      if (idx !== -1 && entry.isIntersecting) {
        setTimeout(() => {
          visibleCards.value[idx] = true
        }, idx * 120)
      }
    })
  }, { threshold: 0.15 })

  cardRefs.value.forEach(el => {
    if (el) observer.observe(el)
  })
})

onUnmounted(() => {
  observer?.disconnect()
})
</script>

<style scoped>
.feature-cards {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
  gap: 20px;
  margin: 32px 0;
}

.feature-card {
  border: 1px solid var(--vp-c-default-3);
  border-radius: 12px;
  padding: 24px;
  background: var(--vp-c-bg);
  opacity: 0;
  transform: translateY(24px);
  transition: all 0.5s cubic-bezier(0.25, 1, 0.5, 1);
}
.feature-card.visible {
  opacity: 1;
  transform: translateY(0);
}
.feature-card:hover {
  border-color: var(--vp-c-brand-1);
  box-shadow: 0 4px 20px rgba(0,0,0,0.06);
  transform: translateY(-2px);
}

.card-icon {
  width: 48px;
  height: 48px;
  border-radius: 12px;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 24px;
  margin-bottom: 16px;
}

.card-tag {
  display: inline-block;
  font-size: 11px;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 1px;
  color: var(--vp-c-brand-1);
  margin-bottom: 8px;
}

.card-title {
  font-size: 17px;
  font-weight: 700;
  margin: 0 0 8px;
  color: var(--vp-c-text-1);
}

.card-desc {
  font-size: 14px;
  line-height: 1.6;
  color: var(--vp-c-text-2);
  margin: 0 0 12px;
}

.card-link {
  font-size: 13px;
  font-weight: 600;
  color: var(--vp-c-brand-1);
  text-decoration: none;
  transition: color 0.2s;
}
.card-link:hover { color: var(--vp-c-brand-2); }
</style>
