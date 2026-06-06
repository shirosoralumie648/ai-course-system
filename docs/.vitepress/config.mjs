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
      { text: '课程 C', link: '/course-c/' },
      { text: '共享资源', link: '/shared/' }
    ],
    sidebar: {
      '/course-a/': [
        {
          text: '课程 A：产品原型 + Claude Code 高级技能',
          items: [
            { text: '课程介绍', link: '/course-a/' },
            { text: '教学日历', link: '/course-a/teaching-calendar' },
            { text: 'Reference 融入方案', link: '/course-a/reference-integration' },
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
            { text: '逐周实验', items: [
              { text: 'Lab 01：AI 原生游戏热身', link: '/course-a/labs/lab-01' },
              { text: 'Lab 02：AI IDE 本地项目', link: '/course-a/labs/lab-02' },
              { text: 'Lab 03：Claude Code 快速上手', link: '/course-a/labs/lab-03' },
              { text: 'Lab 04：需求发现', link: '/course-a/labs/lab-04' },
              { text: 'Lab 05：创意验证', link: '/course-a/labs/lab-05' },
              { text: 'Lab 06：单页产品原型', link: '/course-a/labs/lab-06' },
              { text: 'Lab 07：真实 AI 能力接入', link: '/course-a/labs/lab-07' },
              { text: 'Lab 08：完整原型迭代', link: '/course-a/labs/lab-08' },
              { text: 'Lab 09：Workflow 工作流', link: '/course-a/labs/lab-09' },
              { text: 'Lab 10：自定义 Skill', link: '/course-a/labs/lab-10' },
              { text: 'Lab 11：MCP 使用场景', link: '/course-a/labs/lab-11' },
              { text: 'Lab 12：Superpowers 流程', link: '/course-a/labs/lab-12' },
              { text: 'Lab 13：Spec Coding', link: '/course-a/labs/lab-13' },
              { text: 'Lab 14：长运行任务', link: '/course-a/labs/lab-14' },
              { text: 'Lab 15：Agent SDK 设计', link: '/course-a/labs/lab-15' },
              { text: 'Lab 16：Agent Teams', link: '/course-a/labs/lab-16' }
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
            { text: 'Reference 融入方案', link: '/course-b/reference-integration' },
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
              { text: 'Week 10：高级 RAG 与企业知识库', link: '/course-b/week-10' },
              { text: 'Week 11：跨平台 PWA', link: '/course-b/week-11' },
              { text: 'Week 12：小程序入门', link: '/course-b/week-12' },
              { text: 'Week 13：小程序后端', link: '/course-b/week-13' },
              { text: 'Week 14：跨平台整合', link: '/course-b/week-14' },
              { text: 'Week 15：Agent 工程', link: '/course-b/week-15' },
              { text: 'Week 16：期末评审', link: '/course-b/week-16' }
            ]},
            { text: '实验', items: [
              { text: 'Lab 01：设计到代码', link: '/course-b/labs/lab-01' },
              { text: 'Lab 02：组件库与设计 token', link: '/course-b/labs/lab-02' },
              { text: 'Lab 03：设计资产生成', link: '/course-b/labs/lab-03' },
              { text: 'Lab 04：CLI、Git 与 AI 工程流', link: '/course-b/labs/lab-04' },
              { text: 'Lab 05：Supabase 数据库', link: '/course-b/labs/lab-05' },
              { text: 'Lab 06：AI 后端接口', link: '/course-b/labs/lab-06' },
              { text: 'Lab 07：支付与部署', link: '/course-b/labs/lab-07' },
              { text: 'Lab 08：Dify 知识库', link: '/course-b/labs/lab-08' },
              { text: 'Lab 09：最小 RAG', link: '/course-b/labs/lab-09' },
              { text: 'Lab 10：企业知识库评测', link: '/course-b/labs/lab-10' },
              { text: 'Lab 11：PWA 跨平台', link: '/course-b/labs/lab-11' },
              { text: 'Lab 12：小程序前端', link: '/course-b/labs/lab-12' },
              { text: 'Lab 13：小程序后端', link: '/course-b/labs/lab-13' },
              { text: 'Lab 14：跨平台最小实现', link: '/course-b/labs/lab-14' },
              { text: 'Lab 15：Agent 工程规则', link: '/course-b/labs/lab-15' },
              { text: 'Lab 16：期末技术评审', link: '/course-b/labs/lab-16' }
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
      '/course-c/': [
        {
          text: '课程 C：企业 AI 运营系统',
          items: [
            { text: '课程介绍', link: '/course-c/' },
            { text: '教学日历', link: '/course-c/teaching-calendar' },
            { text: 'Reference 融入方案', link: '/course-c/reference-integration' },
            { text: '每周教程', items: [
              { text: 'Week 01：企业 AI 运营系统', link: '/course-c/week-01' },
              { text: 'Week 02：市场调研与行业分析', link: '/course-c/week-02' },
              { text: 'Week 03：产品定位与原型表达', link: '/course-c/week-03' },
              { text: 'Week 04：品牌推广与内容资产', link: '/course-c/week-04' },
              { text: 'Week 05：销售线索与渠道开拓', link: '/course-c/week-05' },
              { text: 'Week 06：客户关系维护', link: '/course-c/week-06' },
              { text: 'Week 07：数据分析与管理仪表盘', link: '/course-c/week-07' }
            ]},
            { text: '逐周实验', items: [
              { text: 'Lab 01：岗位 AI 助理包骨架', link: '/course-c/labs/lab-01' },
              { text: 'Lab 02：市场研究来源审计', link: '/course-c/labs/lab-02' },
              { text: 'Lab 03：产品定位与原型提示词', link: '/course-c/labs/lab-03' },
              { text: 'Lab 04：品牌活动素材包', link: '/course-c/labs/lab-04' },
              { text: 'Lab 05：客户分层与外联序列', link: '/course-c/labs/lab-05' },
              { text: 'Lab 06：会议纪要转 CRM', link: '/course-c/labs/lab-06' },
              { text: 'Lab 07：仪表盘字段与指标审计', link: '/course-c/labs/lab-07' }
            ]},
            { text: '模板与样例', items: [
              { text: '模板总览', link: '/course-c/templates/' },
              { text: '岗位 AI 助理包', link: '/course-c/templates/role-ai-assistant-pack' },
              { text: '工作流 SOP', link: '/course-c/templates/workflow-sop' },
              { text: '提示词库', link: '/course-c/templates/prompt-library' },
              { text: '合规检查清单', link: '/course-c/templates/compliance-checklist' },
              { text: '审计日志', link: '/course-c/templates/audit-log' },
              { text: 'ROI 报告', link: '/course-c/templates/roi-report' },
              { text: '合成样例包', link: '/course-c/examples/' },
              { text: '虚构公司画像', link: '/course-c/examples/virtual-company-profile' },
              { text: '合同纠纷样例', link: '/course-c/examples/sample-contract-dispute' }
            ]},
            { text: '期末项目', link: '/course-c/final-project' },
            { text: '评分标准', link: '/course-c/rubric' }
          ]
        }
      ],
      '/shared/': [
        {
          text: '共享资源',
          items: [
            { text: '安装指南', link: '/shared/' },
            { text: '快速接入教程', link: '/shared/quick-start' },
            { text: 'Claude Code 安装', link: '/shared/claude-code' },
            { text: 'Codex CLI 安装', link: '/shared/codex-cli' },
            { text: 'Git 与 GitHub', link: '/shared/git-github' },
            { text: '工具对比', link: '/shared/tool-comparison' },
            { text: '参考项目读法', link: '/shared/reference-reading' },
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
