import { defineConfig } from 'vitepress'

const base = process.env.BASE || '/'

export default defineConfig({
  title: 'AI Course System',
  description: '面向高校和训练营的 AI 课程体系',
  base,
  lang: 'zh-CN',
  markdown: {
    config(md) {
      const defaultFence = md.renderer.rules.fence

      md.renderer.rules.fence = (tokens, idx, options, env, self) => {
        const token = tokens[idx]
        const info = token.info ? token.info.trim() : ''
        const lang = info.split(/\s+/)[0]

        if (lang === 'mermaid') {
          return `<MermaidChart code="${encodeURIComponent(token.content.trim())}" />`
        }

        return defaultFence
          ? defaultFence(tokens, idx, options, env, self)
          : self.renderToken(tokens, idx, options)
      }
    }
  },
  themeConfig: {
    nav: [
      { text: '首页', link: '/' },
      { text: '课程 A', link: '/course-a/' },
      { text: '课程 B', link: '/course-b/' },
      { text: '共享资源', link: '/shared/' }
    ],
    sidebar: {
      '/course-a/': [
        {
          text: '课程 A：产品原型 + Claude Code 高级技能',
          items: [
            { text: '课程介绍', link: '/course-a/' },
            { text: '教学日历', link: '/course-a/teaching-calendar' },
            { text: '每周教程', items: [
              { text: 'Week 01：游戏热身', link: '/course-a/week-01' },
              { text: 'Week 02：AI IDE 入门', link: '/course-a/week-02' },
              { text: 'Week 03：Claude Code 快速上手', link: '/course-a/week-03' },
              { text: 'Week 04：找到好创意', link: '/course-a/week-04' },
              { text: 'Week 05：验证创意', link: '/course-a/week-05' },
              { text: 'Week 06：搭建产品原型', link: '/course-a/week-06' },
              { text: 'Week 07：接入 AI 能力', link: '/course-a/week-07' },
              { text: 'Week 08：完整项目实践', link: '/course-a/week-08' },
              { text: 'Week 09：Workflow', link: '/course-a/week-09' },
              { text: 'Week 10：Skills 指南', link: '/course-a/week-10' },
              { text: 'Week 11：MCP 服务器', link: '/course-a/week-11' },
              { text: 'Week 12：Superpowers', link: '/course-a/week-12' },
              { text: 'Week 13：Spec Coding', link: '/course-a/week-13' },
              { text: 'Week 14：长运行任务', link: '/course-a/week-14' },
              { text: 'Week 15：Claude Agent SDK', link: '/course-a/week-15' },
              { text: 'Week 16：Agent Teams', link: '/course-a/week-16' }
            ]},
            { text: '实验报告', items: [
              { text: 'Lab 01：Prompt 对比实验', link: '/course-a/labs/lab-01' },
              { text: 'Lab 02：AI 辅助写作修订', link: '/course-a/labs/lab-02' },
              { text: 'Lab 03：个人 AI 工作流', link: '/course-a/labs/lab-03' }
            ]},
            { text: '期末项目', link: '/course-a/final-project' },
            { text: '评分标准', link: '/course-a/rubric' }
          ]
        }
      ],
      '/course-b/': [
        {
          text: '课程 B：AI 全栈开发实战',
          items: [
            { text: '课程介绍', link: '/course-b/' },
            { text: '教学日历', link: '/course-b/teaching-calendar' },
            { text: '每周教程', items: [
              { text: 'Week 01：从设计到代码', link: '/course-b/week-01' },
              { text: 'Week 02：组件库与多产品 UI', link: '/course-b/week-02' },
              { text: 'Week 03：Figma 与设计资产', link: '/course-b/week-03' },
              { text: 'Week 04：现代 CLI 与 Git', link: '/course-b/week-04' },
              { text: 'Week 05：数据库与 Supabase', link: '/course-b/week-05' },
              { text: 'Week 06：接入 AI 接口', link: '/course-b/week-06' },
              { text: 'Week 07：支付与部署', link: '/course-b/week-07' },
              { text: 'Week 08：Dify 知识库', link: '/course-b/week-08' },
              { text: 'Week 09：RAG 入门', link: '/course-b/week-09' },
              { text: 'Week 10：高级 RAG', link: '/course-b/week-10' },
              { text: 'Week 11：跨平台开发', link: '/course-b/week-11' },
              { text: 'Week 12：小程序入门', link: '/course-b/week-12' },
              { text: 'Week 13：小程序后端', link: '/course-b/week-13' },
              { text: 'Week 14：综合项目', link: '/course-b/final-project' }
            ]},
            { text: '实验', items: [
              { text: 'Lab 01：Claude Code Bugfix', link: '/course-b/labs/lab-01' },
              { text: 'Lab 02：Codex Code Change', link: '/course-b/labs/lab-02' },
              { text: 'Lab 03：Project Rules', link: '/course-b/labs/lab-03' },
              { text: 'Lab 04：Code Review Skill', link: '/course-b/labs/lab-04' }
            ]},
            { text: '模板', items: [
              { text: 'CLAUDE.md 模板', link: '/course-b/templates/CLAUDE' },
              { text: 'AGENTS.md 模板', link: '/course-b/templates/AGENTS' },
              { text: 'SKILL.md 模板', link: '/course-b/templates/SKILL' }
            ]},
            { text: '期末项目', link: '/course-b/final-project' },
            { text: '评分标准', link: '/course-b/rubric' }
          ]
        }
      ],
      '/shared/': [
        {
          text: '共享资源',
          items: [
            { text: '安装指南', link: '/shared/' },
            { text: 'Claude Code 安装', link: '/shared/claude-code' },
            { text: 'Codex CLI 安装', link: '/shared/codex-cli' },
            { text: 'Git 与 GitHub', link: '/shared/git-github' },
            { text: '工具对比', link: '/shared/tool-comparison' },
            { text: '图片需求清单', link: '/shared/image-requirements' }
          ]
        }
      ]
    },
    outline: {
      level: [2, 3],
      label: '本页目录'
    },
    docFooter: {
      prev: '上一节',
      next: '下一节'
    },
    socialLinks: [
      { icon: 'github', link: 'https://github.com/shirosoralumie648/ai-course-system' }
    ]
  }
})
