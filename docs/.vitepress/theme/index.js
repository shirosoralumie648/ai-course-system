import DefaultTheme from 'vitepress/theme'
import ElementPlus from 'element-plus'
import 'element-plus/dist/index.css'
import './style.css'
import StepBar from './components/StepBar.vue'
import ChapterIntroduction from './components/ChapterIntroduction.vue'
import SummaryCard from './components/SummaryCard.vue'
import InfoCard from './components/InfoCard.vue'
import ReadingProgress from './components/ReadingProgress.vue'
import PromptPlayground from './components/PromptPlayground.vue'
import WorkflowDiagram from './components/WorkflowDiagram.vue'
import AnimatedFeatureCards from './components/AnimatedFeatureCards.vue'
import DiffViewer from './components/DiffViewer.vue'
import DiffViewerFile from './components/DiffViewerFile.vue'
import DiffViewerHunk from './components/DiffViewerHunk.vue'
import ProgressTracker from './components/ProgressTracker.vue'
import AiChat from './components/AiChat.vue'
import AiChatMessage from './components/AiChatMessage.vue'
import TextType from './components/TextType.vue'
import RiskMatrix from './components/RiskMatrix.vue'
import MermaidChart from './components/MermaidChart.vue'

export default {
  extends: DefaultTheme,
  enhanceApp({ app }) {
    app.use(ElementPlus)
    app.component('StepBar', StepBar)
    app.component('ChapterIntroduction', ChapterIntroduction)
    app.component('SummaryCard', SummaryCard)
    app.component('InfoCard', InfoCard)
    app.component('ReadingProgress', ReadingProgress)
    app.component('PromptPlayground', PromptPlayground)
    app.component('WorkflowDiagram', WorkflowDiagram)
    app.component('AnimatedFeatureCards', AnimatedFeatureCards)
    app.component('DiffViewer', DiffViewer)
    app.component('DiffViewerFile', DiffViewerFile)
    app.component('DiffViewerHunk', DiffViewerHunk)
    app.component('ProgressTracker', ProgressTracker)
    app.component('AiChat', AiChat)
    app.component('AiChatMessage', AiChatMessage)
    app.component('TextType', TextType)
    app.component('RiskMatrix', RiskMatrix)
    app.component('MermaidChart', MermaidChart)
  }
}
