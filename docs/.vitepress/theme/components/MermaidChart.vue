<template>
  <section class="lesson-diagram" :class="`lesson-diagram--${diagram.kind}`">
    <header class="diagram-hero">
      <div class="diagram-hero__mark">{{ diagram.mark }}</div>
      <div class="diagram-hero__copy">
        <p>{{ diagram.badge }}</p>
        <h3>{{ diagram.title }}</h3>
      </div>
      <span class="diagram-hero__count">{{ diagram.countLabel }}</span>
    </header>

    <div v-if="diagram.kind === 'sequence'" class="sequence-board">
      <div class="actor-row">
        <span
          v-for="actor in diagram.actors"
          :key="actor.id"
          class="actor-token"
          :style="{ '--actor-color': actor.accent }"
        >
          <span class="actor-token__dot" />
          {{ actor.label }}
        </span>
      </div>

      <ol class="sequence-timeline">
        <li
          v-for="(message, index) in diagram.messages"
          :key="`${message.from}-${message.to}-${index}`"
          class="sequence-event"
          :class="{
            'sequence-event--note': message.type === 'note',
            'sequence-event--return': message.type === 'return'
          }"
          :style="{ '--event-accent': message.accent }"
        >
          <div class="sequence-event__rail">
            <span>{{ String(index + 1).padStart(2, '0') }}</span>
          </div>
          <article class="sequence-event__card">
            <div class="sequence-event__route">
              <strong>{{ actorName(message.from) }}</strong>
              <span>{{ message.type === 'note' ? 'NOTE' : arrowFor(message) }}</span>
              <strong v-if="message.to">{{ actorName(message.to) }}</strong>
            </div>
            <p>{{ message.label }}</p>
          </article>
        </li>
      </ol>
    </div>

    <div v-else-if="diagram.kind === 'state'" class="state-board">
      <div class="state-grid">
        <article
          v-for="node in diagram.nodes"
          :key="node.id"
          class="state-card"
          :class="`state-card--${node.shape}`"
          :style="{ '--state-accent': node.accent }"
        >
          <span>{{ node.order }}</span>
          <strong>{{ node.label }}</strong>
        </article>
      </div>

      <ol class="transition-list">
        <li
          v-for="(edge, index) in diagram.edges"
          :key="`${edge.from}-${edge.to}-${index}`"
          class="transition-row"
        >
          <span>{{ nodeName(edge.from) }}</span>
          <small>{{ edge.label || '状态变化' }}</small>
          <span>{{ nodeName(edge.to) }}</span>
        </li>
      </ol>
    </div>

    <div v-else class="flow-board">
      <div class="flow-grid" :class="{ 'flow-grid--single': diagram.groups.length === 1 }">
        <section
          v-for="(group, groupIndex) in diagram.groups"
          :key="group.id"
          class="flow-stage"
          :style="{ '--stage-accent': accentFor(groupIndex) }"
        >
          <header class="flow-stage__header">
            <span>{{ String(groupIndex + 1).padStart(2, '0') }}</span>
            <strong>{{ group.label }}</strong>
          </header>

          <ol class="flow-stack">
            <li
              v-for="node in group.nodes"
              :key="node.id"
              class="flow-stack__item"
            >
              <div
                class="flow-card"
                :class="`flow-card--${node.shape}`"
                :style="{ '--node-accent': node.accent || accentFor(groupIndex) }"
              >
                <span class="flow-card__number">{{ node.order }}</span>
                <span class="flow-card__label">{{ node.label }}</span>
              </div>
              <div
                v-if="hasOutgoingInGroup(node, group)"
                class="flow-arrow"
                :title="arrowTitle(node, group)"
                aria-hidden="true"
              >
                <span class="flow-arrow__line"></span>
                <span class="flow-arrow__head"></span>
              </div>
            </li>
          </ol>
        </section>
      </div>

      <div v-if="diagram.edgeHighlights.length" class="route-panel">
        <div class="route-panel__title">关键路径</div>
        <div class="route-chips">
          <span
            v-for="(edge, index) in diagram.edgeHighlights"
            :key="`${edge.from}-${edge.to}-${index}`"
            class="route-chip"
          >
            <span>{{ nodeName(edge.from) }}</span>
            <small>{{ edge.label }}</small>
            <span>{{ nodeName(edge.to) }}</span>
          </span>
        </div>
      </div>
    </div>
  </section>
</template>

<script setup>
import { computed } from 'vue'

const props = defineProps({
  code: {
    type: String,
    required: true
  }
})

const accents = ['#2563eb', '#059669', '#d97706', '#dc2626', '#0891b2', '#7c3aed']

const source = computed(() => decodeMermaidCode(props.code))
const diagram = computed(() => parseDiagram(source.value))

function outgoingInGroup(node, group) {
  if (!node || !group) return []
  const ids = new Set(group.nodes.map((n) => n.id))
  const out = node.outgoing || node.edges?.outgoing || []
  return out.filter((edge) => ids.has(edge.to))
}

function hasOutgoingInGroup(node, group) {
  return outgoingInGroup(node, group).length > 0
}

function arrowTitle(node, group) {
  const targets = outgoingInGroup(node, group).map((edge) => nodeName(edge.to))
  return targets.length ? `${node.label || node.id} → ${targets.join('、')}` : ''
}

function decodeMermaidCode(value) {
  try {
    return decodeURIComponent(value).trim()
  } catch {
    return value.trim()
  }
}

function parseDiagram(text) {
  const lines = text
    .split('\n')
    .map((line) => line.trim())
    .filter((line) => line && !line.startsWith('%%'))

  const firstLine = lines[0] || ''

  if (/^sequenceDiagram\b/.test(firstLine)) {
    return parseSequence(lines)
  }

  if (/^stateDiagram(?:-v2)?\b/.test(firstLine)) {
    return parseState(lines)
  }

  return parseFlow(lines)
}

function parseSequence(lines) {
  const actors = new Map()
  const messages = []

  for (const rawLine of lines.slice(1)) {
    const line = rawLine.trim()

    if (/^(autonumber|rect\b|end\b)/.test(line)) {
      continue
    }

    const participant = line.match(/^(?:participant|actor)\s+(.+?)(?:\s+as\s+(.+))?$/u)
    if (participant) {
      const id = participant[1].trim()
      actors.set(id, cleanLabel(participant[2] || id))
      continue
    }

    const note = line.match(/^Note\s+(?:over|right of|left of)\s+(.+?):\s*(.+)$/u)
    if (note) {
      const target = note[1].split(',')[0].trim()
      ensureActor(actors, target)
      messages.push({
        type: 'note',
        from: target,
        to: '',
        label: cleanLabel(note[2]),
        accent: accentFor(messages.length)
      })
      continue
    }

    const message = line.match(/^(.+?)\s*([-.=x]+[>)]+)\s*(.+?)\s*:\s*(.+)$/u)
    if (message) {
      const from = message[1].trim()
      const operator = message[2]
      const to = message[3].trim()
      ensureActor(actors, from)
      ensureActor(actors, to)
      messages.push({
        type: operator.includes('--') ? 'return' : 'message',
        from,
        to,
        label: cleanLabel(message[4]),
        operator,
        accent: accentFor(messages.length)
      })
    }
  }

  return {
    kind: 'sequence',
    title: '时序流程',
    badge: 'Sequence',
    mark: 'SEQ',
    countLabel: `${messages.length} 个动作`,
    actors: [...actors.entries()].map(([id, label], index) => ({
      id,
      label,
      accent: accentFor(index)
    })),
    messages
  }
}

function parseState(lines) {
  const labels = new Map()
  const stateIds = new Set()
  const edges = []

  for (const rawLine of lines.slice(1)) {
    const line = rawLine.trim()
    const stateAlias = line.match(/^state\s+["'](.+?)["']\s+as\s+(.+)$/u)

    if (stateAlias) {
      labels.set(stateAlias[2].trim(), cleanLabel(stateAlias[1]))
      stateIds.add(stateAlias[2].trim())
      continue
    }

    const transition = line.match(/^(.+?)\s*-->\s*(.+?)(?:\s*:\s*(.+))?$/u)
    if (transition) {
      const from = normalizeStateId(transition[1])
      const to = normalizeStateId(transition[2])
      stateIds.add(from)
      stateIds.add(to)
      edges.push({
        from,
        to,
        label: cleanLabel(transition[3] || '')
      })
    }
  }

  const nodes = [...stateIds].map((id, index) => ({
    id,
    label: labels.get(id) || (id === '__terminal__' ? '开始 / 结束' : cleanLabel(id)),
    order: String(index + 1).padStart(2, '0'),
    shape: id === '__terminal__' ? 'terminal' : 'state',
    accent: accentFor(index)
  }))

  return {
    kind: 'state',
    title: '状态流转',
    badge: 'State',
    mark: 'ST',
    countLabel: `${nodes.length} 个状态`,
    nodes,
    edges
  }
}

function parseFlow(lines) {
  const nodes = new Map()
  const groups = new Map()
  const edges = []
  const styles = new Map()
  const mainGroup = ensureGroup(groups, 'main', '流程概览')
  let currentGroup = mainGroup.id

  for (const rawLine of lines.slice(1)) {
    const line = rawLine.trim()

    if (/^end\b/.test(line)) {
      currentGroup = mainGroup.id
      continue
    }

    const subgraph = line.match(/^subgraph\s+(.+)$/u)
    if (subgraph) {
      const group = parseGroup(subgraph[1], groups.size)
      groups.set(group.id, group)
      currentGroup = group.id
      continue
    }

    const style = line.match(/^style\s+([^\s]+)\s+(.+)$/u)
    if (style) {
      const fill = style[2].match(/fill\s*:\s*(#[0-9a-fA-F]{3,6})/)
      if (fill) styles.set(style[1], fill[1])
      continue
    }

    if (/^(classDef|class|linkStyle|click)\b/.test(line)) {
      continue
    }

    const edgeParts = splitEdge(line)
    if (edgeParts.nodes.length >= 2) {
      edgeParts.nodes.forEach((part) => addNode(nodes, groups, currentGroup, part, styles))
      for (let index = 0; index < edgeParts.nodes.length - 1; index += 1) {
        const from = parseNode(edgeParts.nodes[index]).id
        const to = parseNode(edgeParts.nodes[index + 1]).id
        if (from && to) {
          edges.push({ from, to, label: edgeParts.labels[index] || edgeParts.label || '' })
        }
      }
      continue
    }

    const standalone = parseNode(line)
    if (standalone.id) {
      addNode(nodes, groups, currentGroup, line, styles)
    }
  }

  for (const edge of edges) {
    const fromNode = nodes.get(edge.from)
    const toNode = nodes.get(edge.to)
    if (!fromNode || !toNode) continue
    if (toNode.groupId !== fromNode.groupId) {
      toNode.groupId = fromNode.groupId
    }
  }

  const groupedNodes = [...groups.values()]
    .map((group) => {
      const groupNodes = [...nodes.values()].filter((node) => node.groupId === group.id)
      const nodeEdges = new Map()
      for (const node of groupNodes) {
        nodeEdges.set(node.id, { incoming: [], outgoing: [] })
      }
      for (const edge of edges) {
        if (nodeEdges.has(edge.from)) nodeEdges.get(edge.from).outgoing.push(edge)
        if (nodeEdges.has(edge.to)) nodeEdges.get(edge.to).incoming.push(edge)
      }
      return {
        ...group,
        nodes: groupNodes.map((node, index) => ({
          ...node,
          order: String(index + 1).padStart(2, '0'),
          accent: styles.get(node.id) || node.accent || accentFor(index),
          incoming: nodeEdges.get(node.id)?.incoming || [],
          outgoing: nodeEdges.get(node.id)?.outgoing || []
        }))
      }
    })
    .filter((group) => group.nodes.length)

  const edgeHighlights = edges.filter((edge) => edge.label).slice(0, 12)

  const allNodes = groupedNodes.flatMap((group) => group.nodes)

  return {
    kind: 'flow',
    title: groupedNodes.length > 1 ? '分层流程图解' : '流程图解',
    badge: 'Flow',
    mark: 'MAP',
    countLabel: `${allNodes.length} 个节点`,
    groups: groupedNodes.length ? groupedNodes : [{ ...mainGroup, nodes: allNodes }],
    edges,
    edgeHighlights
  }
}

function ensureActor(actors, id) {
  if (!actors.has(id)) {
    actors.set(id, cleanLabel(id))
  }
}

function ensureGroup(groups, id, label) {
  if (!groups.has(id)) {
    groups.set(id, { id, label })
  }
  return groups.get(id)
}

function parseGroup(raw, index) {
  const parsed = parseNode(raw)
  const label = parsed.label && parsed.label !== parsed.id ? parsed.label : cleanLabel(raw)
  return {
    id: parsed.id || `group-${index}`,
    label
  }
}

function splitEdge(line) {
  const labels = []
  let normalized = line

  normalized = normalized.replace(/\s*-->\s*\|([^|]+)\|\s*/g, (_, label) => {
    labels.push(cleanLabel(label))
    return ' --> '
  })

  normalized = normalized.replace(/\s*--\s*([^->]+?)\s*-->\s*/g, (_, label) => {
    labels.push(cleanLabel(label))
    return ' --> '
  })

  normalized = normalized.replace(/\s*---\s*\|([^|]+)\|\s*/g, (_, label) => {
    labels.push(cleanLabel(label))
    return ' --- '
  })

  const nodes = normalized
    .split(/\s*(?:-->|---|==>|-.->)\s*/)
    .map((part) => part.trim())
    .filter(Boolean)

  return {
    nodes,
    labels,
    label: labels[0] || ''
  }
}

function addNode(nodes, groups, groupId, raw, styles) {
  const parsed = parseNode(raw)
  if (!parsed.id) return

  ensureGroup(groups, groupId, groupId)

  const existing = nodes.get(parsed.id)
  const parsedHasReadableLabel = parsed.label && parsed.label !== parsed.id

  nodes.set(parsed.id, {
    ...existing,
    ...parsed,
    label: parsedHasReadableLabel ? parsed.label : existing?.label || parsed.label || parsed.id,
    shape: parsed.shape !== 'card' ? parsed.shape : existing?.shape || parsed.shape || 'card',
    groupId: existing?.groupId || groupId,
    accent: styles.get(parsed.id) || existing?.accent || ''
  })
}

function parseNode(raw) {
  const text = raw.trim().replace(/,$/, '')
  const match = text.match(/^([^\s[\](){]+)\s*(.*)$/u)
  if (!match) return { id: '', label: '', shape: 'card' }

  const id = match[1].trim()
  const rest = match[2].trim()
  const label = extractNodeLabel(rest) || cleanLabel(id)

  return {
    id,
    label,
    shape: rest.startsWith('{') ? 'decision' : rest.startsWith('((') || rest.startsWith('[(') ? 'round' : 'card'
  }
}

function extractNodeLabel(rest) {
  if (!rest) return ''

  const wrappers = [
    /^\[\[(.*)\]\]$/s,
    /^\[\((.*)\)\]$/s,
    /^\[(.*)\]$/s,
    /^\{\{(.*)\}\}$/s,
    /^\{(.*)\}$/s,
    /^\(\((.*)\)\)$/s,
    /^\((.*)\)$/s
  ]

  for (const wrapper of wrappers) {
    const match = rest.match(wrapper)
    if (match) return cleanLabel(match[1])
  }

  return ''
}

function normalizeStateId(value) {
  const id = value.trim()
  return id === '[*]' ? '__terminal__' : id
}

function cleanLabel(value = '') {
  return stripQuotes(String(value))
    .replace(/<br\s*\/?>/gi, '\n')
    .replace(/\\n/g, '\n')
    .replace(/&nbsp;/g, ' ')
    .trim()
}

function stripQuotes(value = '') {
  return value.replace(/^["']|["']$/g, '').trim()
}

function accentFor(index) {
  return accents[index % accents.length]
}

function nodeName(id) {
  const current = diagram.value
  const nodes = current.nodes || current.groups?.flatMap((group) => group.nodes) || []
  const node = nodes.find((item) => item.id === id)
  return node?.label || id
}

function actorName(id) {
  const actor = diagram.value.actors?.find((item) => item.id === id)
  return actor?.label || id
}

function arrowFor(message) {
  return message.type === 'return' ? '↩' : '→'
}
</script>

<style scoped>
.lesson-diagram {
  position: relative;
  overflow: hidden;
  margin: 30px 0;
  padding: 18px;
  border: 1px solid color-mix(in srgb, var(--vp-c-brand-1) 18%, var(--vp-c-divider));
  border-radius: 8px;
  background:
    linear-gradient(90deg, color-mix(in srgb, var(--vp-c-divider) 38%, transparent) 1px, transparent 1px),
    linear-gradient(180deg, color-mix(in srgb, var(--vp-c-divider) 34%, transparent) 1px, transparent 1px),
    linear-gradient(180deg, color-mix(in srgb, var(--vp-c-brand-1) 7%, var(--vp-c-bg)) 0%, var(--vp-c-bg) 190px);
  background-size: 26px 26px, 26px 26px, 100% 100%;
  box-shadow: 0 18px 44px rgba(15, 23, 42, 0.08);
}

.dark .lesson-diagram {
  box-shadow: 0 20px 46px rgba(0, 0, 0, 0.28);
}

.lesson-diagram::before {
  position: absolute;
  inset: 0 0 auto;
  height: 4px;
  background: linear-gradient(90deg, #2563eb, #059669 32%, #d97706 68%, #dc2626);
  content: "";
}

.diagram-hero {
  position: relative;
  z-index: 1;
  display: grid;
  grid-template-columns: auto minmax(0, 1fr) auto;
  gap: 13px;
  align-items: center;
  margin-bottom: 18px;
}

.diagram-hero__mark {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  width: 46px;
  height: 46px;
  border: 1px solid color-mix(in srgb, var(--vp-c-brand-1) 32%, var(--vp-c-divider));
  border-radius: 8px;
  color: var(--vp-c-brand-1);
  background: color-mix(in srgb, var(--vp-c-brand-1) 10%, var(--vp-c-bg));
  font-size: 12px;
  font-weight: 900;
}

.diagram-hero__copy {
  min-width: 0;
}

.diagram-hero__copy p {
  margin: 0 0 3px;
  color: var(--vp-c-text-3);
  font-size: 12px;
  font-weight: 800;
  text-transform: uppercase;
}

.diagram-hero__copy h3 {
  margin: 0;
  color: var(--vp-c-text-1);
  font-size: 18px;
  line-height: 1.35;
}

.diagram-hero__count {
  justify-self: end;
  padding: 6px 10px;
  border: 1px solid var(--vp-c-divider);
  border-radius: 999px;
  color: var(--vp-c-text-2);
  background: color-mix(in srgb, var(--vp-c-bg) 90%, transparent);
  font-size: 12px;
  font-weight: 800;
  white-space: nowrap;
}

.flow-grid {
  position: relative;
  z-index: 1;
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(min(100%, 238px), 1fr));
  gap: 12px;
}

.flow-grid--single {
  grid-template-columns: minmax(0, 1fr);
}

.flow-stage {
  min-width: 0;
  border: 1px solid color-mix(in srgb, var(--stage-accent) 34%, var(--vp-c-divider));
  border-radius: 8px;
  background: color-mix(in srgb, var(--stage-accent) 6%, var(--vp-c-bg));
}

.flow-stage__header {
  display: flex;
  gap: 9px;
  align-items: center;
  padding: 10px 12px;
  border-bottom: 1px solid color-mix(in srgb, var(--stage-accent) 28%, var(--vp-c-divider));
  color: color-mix(in srgb, var(--stage-accent) 82%, var(--vp-c-text-1));
}

.flow-stage__header span {
  display: inline-flex;
  flex: 0 0 auto;
  align-items: center;
  justify-content: center;
  width: 26px;
  height: 26px;
  border-radius: 999px;
  color: white;
  background: var(--stage-accent);
  font-size: 11px;
  font-weight: 900;
}

.flow-stage__header strong {
  min-width: 0;
  font-size: 14px;
  line-height: 1.35;
  overflow-wrap: anywhere;
}

.flow-stack,
.sequence-timeline,
.transition-list {
  margin: 0;
  padding: 0;
  list-style: none;
}

.flow-stack {
  display: grid;
  gap: 8px;
  padding: 12px;
}

.flow-stack__item {
  display: flex;
  flex-direction: column;
  align-items: stretch;
  gap: 4px;
}

.flow-stack__item:last-child .flow-arrow {
  display: none;
}

.flow-arrow {
  display: flex;
  flex-direction: column;
  align-items: center;
  height: 22px;
  color: var(--stage-accent);
  opacity: 0.7;
}

.flow-arrow__line {
  width: 2px;
  height: 14px;
  background: currentColor;
  border-radius: 1px;
}

.flow-arrow__head {
  width: 0;
  height: 0;
  margin-top: 1px;
  border-left: 5px solid transparent;
  border-right: 5px solid transparent;
  border-top: 6px solid currentColor;
}

.flow-card {
  display: grid;
  grid-template-columns: auto minmax(0, 1fr);
  gap: 10px;
  align-items: center;
  min-height: 50px;
  padding: 10px 11px;
  border: 1px solid color-mix(in srgb, var(--node-accent) 34%, var(--vp-c-divider));
  border-radius: 8px;
  background: color-mix(in srgb, var(--vp-c-bg) 94%, var(--node-accent));
}

.flow-card--decision {
  border-style: dashed;
  background: color-mix(in srgb, #d97706 10%, var(--vp-c-bg));
}

.flow-card--round {
  background: color-mix(in srgb, #059669 9%, var(--vp-c-bg));
}

.flow-card__number,
.state-card span {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  width: 30px;
  height: 30px;
  border-radius: 999px;
  color: white;
  background: color-mix(in srgb, var(--node-accent) 58%, #111827);
  font-size: 11px;
  font-weight: 900;
  line-height: 1;
}

.flow-card__label {
  min-width: 0;
  color: var(--vp-c-text-1);
  font-size: 14px;
  font-weight: 750;
  line-height: 1.45;
  overflow-wrap: anywhere;
  white-space: pre-line;
}

.route-panel {
  position: relative;
  z-index: 1;
  margin-top: 12px;
  padding: 12px;
  border: 1px solid var(--vp-c-divider);
  border-radius: 8px;
  background: color-mix(in srgb, var(--vp-c-bg-soft) 78%, var(--vp-c-bg));
}

.route-panel__title {
  margin-bottom: 8px;
  color: var(--vp-c-text-2);
  font-size: 12px;
  font-weight: 900;
}

.route-chips {
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
}

.route-chip,
.transition-row {
  display: inline-flex;
  align-items: center;
  max-width: 100%;
  border: 1px solid var(--vp-c-divider);
  border-radius: 999px;
  background: var(--vp-c-bg);
  color: var(--vp-c-text-2);
  font-size: 12px;
  font-weight: 750;
}

.route-chip {
  gap: 7px;
  padding: 6px 9px;
}

.route-chip::after,
.transition-row::after {
  color: var(--vp-c-brand-1);
  content: "→";
  font-weight: 900;
}

.route-chip small,
.transition-row small {
  color: var(--vp-c-brand-1);
  font-size: 11px;
  font-weight: 900;
  white-space: pre-line;
}

.sequence-board {
  position: relative;
  z-index: 1;
  display: grid;
  gap: 14px;
}

.actor-row {
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
}

.actor-token {
  display: inline-flex;
  gap: 7px;
  align-items: center;
  padding: 6px 10px;
  border: 1px solid color-mix(in srgb, var(--actor-color) 34%, var(--vp-c-divider));
  border-radius: 999px;
  color: color-mix(in srgb, var(--actor-color) 80%, var(--vp-c-text-1));
  background: color-mix(in srgb, var(--actor-color) 8%, var(--vp-c-bg));
  font-size: 12px;
  font-weight: 850;
}

.actor-token__dot {
  width: 8px;
  height: 8px;
  border-radius: 999px;
  background: var(--actor-color);
}

.sequence-timeline {
  display: grid;
  gap: 0;
}

.sequence-event {
  display: grid;
  grid-template-columns: 48px minmax(0, 1fr);
  gap: 12px;
  min-width: 0;
}

.sequence-event__rail {
  position: relative;
  display: flex;
  justify-content: center;
}

.sequence-event__rail::before {
  position: absolute;
  top: 0;
  bottom: 0;
  width: 2px;
  background: color-mix(in srgb, var(--event-accent) 34%, var(--vp-c-divider));
  content: "";
}

.sequence-event:first-child .sequence-event__rail::before {
  top: 18px;
}

.sequence-event:last-child .sequence-event__rail::before {
  bottom: calc(100% - 18px);
}

.sequence-event__rail span {
  position: relative;
  z-index: 1;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  width: 36px;
  height: 36px;
  border: 3px solid var(--vp-c-bg);
  border-radius: 999px;
  color: white;
  background: var(--event-accent);
  font-size: 11px;
  font-weight: 900;
}

.sequence-event__card {
  margin-bottom: 10px;
  padding: 12px 13px;
  border: 1px solid color-mix(in srgb, var(--event-accent) 28%, var(--vp-c-divider));
  border-radius: 8px;
  background: color-mix(in srgb, var(--event-accent) 6%, var(--vp-c-bg));
}

.sequence-event--note .sequence-event__card {
  border-style: dashed;
  background: color-mix(in srgb, #d97706 10%, var(--vp-c-bg));
}

.sequence-event--return .sequence-event__card {
  background: color-mix(in srgb, #0891b2 8%, var(--vp-c-bg));
}

.sequence-event__route {
  display: flex;
  flex-wrap: wrap;
  gap: 7px;
  align-items: center;
  margin-bottom: 5px;
  color: var(--vp-c-text-2);
  font-size: 12px;
  line-height: 1.4;
}

.sequence-event__route strong {
  color: var(--vp-c-text-1);
  font-weight: 850;
}

.sequence-event__route span {
  color: var(--event-accent);
  font-size: 12px;
  font-weight: 900;
}

.sequence-event__card p {
  margin: 0;
  color: var(--vp-c-text-1);
  font-size: 14px;
  line-height: 1.6;
  overflow-wrap: anywhere;
  white-space: pre-line;
}

.state-board {
  position: relative;
  z-index: 1;
  display: grid;
  gap: 12px;
}

.state-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(min(100%, 190px), 1fr));
  gap: 10px;
}

.state-card {
  display: grid;
  grid-template-columns: auto minmax(0, 1fr);
  gap: 10px;
  align-items: center;
  min-height: 58px;
  padding: 12px;
  border: 1px solid color-mix(in srgb, var(--state-accent) 35%, var(--vp-c-divider));
  border-radius: 8px;
  background: color-mix(in srgb, var(--state-accent) 8%, var(--vp-c-bg));
}

.state-card span {
  background: color-mix(in srgb, var(--state-accent) 72%, #111827);
}

.state-card strong {
  min-width: 0;
  color: var(--vp-c-text-1);
  font-size: 14px;
  line-height: 1.45;
  overflow-wrap: anywhere;
  white-space: pre-line;
}

.state-card--terminal {
  border-style: dashed;
}

.transition-list {
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
}

.transition-row {
  gap: 8px;
  padding: 7px 10px;
}

@media (max-width: 640px) {
  .lesson-diagram {
    padding: 14px;
  }

  .diagram-hero {
    grid-template-columns: auto minmax(0, 1fr);
  }

  .diagram-hero__count {
    grid-column: 1 / -1;
    justify-self: start;
  }

  .sequence-event {
    grid-template-columns: 38px minmax(0, 1fr);
    gap: 9px;
  }

  .sequence-event__rail span {
    width: 32px;
    height: 32px;
    border-width: 2px;
  }
}
</style>
