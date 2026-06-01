<template>
  <div class="ai-chat">
    <div class="chat-header">
      <div class="chat-avatar">🤖</div>
      <div class="chat-info">
        <div class="chat-name">{{ botName }}</div>
        <div class="chat-status">
          <span class="status-dot"></span>
          <span>{{ status }}</span>
        </div>
      </div>
    </div>

    <div class="chat-messages" ref="messagesRef">
      <div v-for="(msg, i) in displayMessages" :key="i"
           class="chat-message" :class="msg.role">
        <div class="message-avatar" v-if="msg.role === 'assistant'">🤖</div>
        <div class="message-bubble">
          <div class="message-content" v-html="formatContent(msg.content)"></div>
          <div class="message-meta" v-if="msg.meta">{{ msg.meta }}</div>
        </div>
        <div class="message-avatar" v-if="msg.role === 'user'">👤</div>
      </div>
      <div v-if="typing" class="chat-message assistant">
        <div class="message-avatar">🤖</div>
        <div class="message-bubble">
          <div class="typing-indicator">
            <span></span><span></span><span></span>
          </div>
        </div>
      </div>
    </div>

    <div class="chat-input" v-if="showInput">
      <input v-model="inputText" :placeholder="placeholder"
             @keyup.enter="sendMessage" :disabled="typing" />
      <button @click="sendMessage" :disabled="!inputText.trim() || typing">
        <svg width="18" height="18" viewBox="0 0 24 24" fill="none">
          <path d="M22 2L11 13M22 2l-7 20-4-9-9-4 20-7z" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
        </svg>
      </button>
    </div>
  </div>
</template>

<script setup>
import { ref, nextTick, watch } from 'vue'

const props = defineProps({
  botName: { type: String, default: 'AI 助手' },
  status: { type: String, default: '在线' },
  placeholder: { type: String, default: '输入消息...' },
  showInput: { type: Boolean, default: true },
  autoPlay: { type: Boolean, default: false },
  initialMessages: {
    type: Array,
    default: () => []
  },
  // 支持 messages 作为 initialMessages 的别名
  messages: {
    type: Array,
    default: () => []
  }
})

const emit = defineEmits(['send'])

// 合并 props 和 messages 属性
const displayMessages = ref([...(props.messages.length > 0 ? props.messages : props.initialMessages)])
const inputText = ref('')
const typing = ref(false)
const messagesRef = ref(null)

// 格式化内容，支持 \n 换行
function formatContent(content) {
  if (!content) return ''
  return content.replace(/\n/g, '<br>')
}

function scrollToBottom() {
  nextTick(() => {
    if (messagesRef.value) {
      messagesRef.value.scrollTop = messagesRef.value.scrollHeight
    }
  })
}

function sendMessage() {
  const text = inputText.value.trim()
  if (!text) return

  displayMessages.value.push({ role: 'user', content: text })
  inputText.value = ''
  scrollToBottom()
  emit('send', text)

  if (props.showInput) {
    typing.value = true
    setTimeout(() => {
      typing.value = false
    }, 1000)
  }
}

function addMessage(role, content, meta) {
  displayMessages.value.push({ role, content, meta })
  scrollToBottom()
}

function startTyping() { typing.value = true }
function stopTyping() { typing.value = false }

watch(() => [props.initialMessages, props.messages], ([initial, msgs]) => {
  displayMessages.value = [...(msgs.length > 0 ? msgs : initial)]
}, { deep: true })

defineExpose({ addMessage, startTyping, stopTyping })
</script>

<style scoped>
.ai-chat {
  border: 1px solid var(--vp-c-default-3);
  border-radius: 12px;
  overflow: hidden;
  margin: 20px 0;
  background: var(--vp-c-bg);
  max-width: 560px;
}

.chat-header {
  display: flex;
  align-items: center;
  gap: 12px;
  padding: 14px 18px;
  background: var(--vp-c-default-soft);
  border-bottom: 1px solid var(--vp-c-default-3);
}
.chat-avatar {
  width: 36px;
  height: 36px;
  border-radius: 50%;
  background: var(--vp-c-brand-soft);
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 18px;
}
.chat-name {
  font-size: 14px;
  font-weight: 700;
  color: var(--vp-c-text-1);
}
.chat-status {
  display: flex;
  align-items: center;
  gap: 5px;
  font-size: 12px;
  color: var(--vp-c-text-3);
}
.status-dot {
  width: 7px;
  height: 7px;
  border-radius: 50%;
  background: #22c55e;
}

.chat-messages {
  padding: 16px;
  max-height: 400px;
  overflow-y: auto;
  display: flex;
  flex-direction: column;
  gap: 12px;
}

.chat-message {
  display: flex;
  gap: 10px;
  align-items: flex-start;
  animation: messageIn 0.3s ease-out;
}
.chat-message.user { flex-direction: row-reverse; }

@keyframes messageIn {
  from { opacity: 0; transform: translateY(8px); }
  to { opacity: 1; transform: translateY(0); }
}

.message-avatar {
  width: 30px;
  height: 30px;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 14px;
  flex-shrink: 0;
  background: var(--vp-c-default-soft);
}

.message-bubble {
  max-width: 75%;
  padding: 10px 14px;
  border-radius: 12px;
  font-size: 13px;
  line-height: 1.6;
}
.chat-message.assistant .message-bubble {
  background: var(--vp-c-default-soft);
  color: var(--vp-c-text-1);
  border-bottom-left-radius: 4px;
}
.chat-message.user .message-bubble {
  background: var(--vp-c-brand-1);
  color: white;
  border-bottom-right-radius: 4px;
}

.message-meta {
  font-size: 11px;
  color: var(--vp-c-text-3);
  margin-top: 6px;
  font-style: italic;
}

.typing-indicator {
  display: flex;
  gap: 4px;
  padding: 4px 0;
}
.typing-indicator span {
  width: 7px;
  height: 7px;
  border-radius: 50%;
  background: var(--vp-c-text-3);
  animation: typing 1.4s infinite;
}
.typing-indicator span:nth-child(2) { animation-delay: 0.2s; }
.typing-indicator span:nth-child(3) { animation-delay: 0.4s; }
@keyframes typing {
  0%, 60%, 100% { transform: translateY(0); opacity: 0.4; }
  30% { transform: translateY(-4px); opacity: 1; }
}

.chat-input {
  display: flex;
  gap: 8px;
  padding: 12px 16px;
  border-top: 1px solid var(--vp-c-default-3);
}
.chat-input input {
  flex: 1;
  border: 1px solid var(--vp-c-default-3);
  border-radius: 8px;
  padding: 8px 14px;
  font-size: 13px;
  outline: none;
  background: var(--vp-c-bg);
  color: var(--vp-c-text-1);
  transition: border-color 0.2s;
}
.chat-input input:focus { border-color: var(--vp-c-brand-1); }
.chat-input button {
  width: 38px;
  height: 38px;
  border-radius: 8px;
  border: none;
  background: var(--vp-c-brand-1);
  color: white;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  transition: background 0.2s;
}
.chat-input button:hover { background: var(--vp-c-brand-2); }
.chat-input button:disabled { opacity: 0.5; cursor: not-allowed; }
</style>
