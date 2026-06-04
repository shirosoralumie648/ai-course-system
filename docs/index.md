---
layout: home
hero:
  name: AI Course System
  text: 从想法到 AI 产品
  tagline: 面向高校和训练营的 AI 课程体系，用 AI IDE、全栈开发和 Agent 工程交付真实作品
  actions:
    - theme: brand
      text: 课程 A：产品原型
      link: /course-a/
    - theme: alt
      text: 课程 B：AI 全栈
      link: /course-b/
    - theme: alt
      text: 我是教师/助教
      link: /shared/
features:
  - icon: 🎮
    title: 课程 A：产品原型 + Claude Code
    details: 面向非计算机专业学生。从小游戏热身开始，学习 AI IDE、Claude Code、需求验证、原型搭建和 Agent 协作。16 周课程。
    link: /course-a/
  - icon: 🧩
    title: 课程 B：AI 全栈开发实战
    details: 面向有编程基础的学生。覆盖前端、组件库、数据库、AI 接口、支付部署、RAG、跨平台和 Agent 工程。16 周课程。
    link: /course-b/
  - icon: 📚
    title: 共享资源
    details: 安装指南、工具对比、伦理安全材料。所有课程共用的基础资源。
    link: /shared/
---

<style>
:root {
  --vp-home-hero-name-color: transparent;
  --vp-home-hero-name-background: linear-gradient(135deg, #3451b2 0%, #5b7cf7 100%);
  --vp-home-hero-image-background-image: linear-gradient(135deg, rgba(53,81,178,0.12) 0%, rgba(91,124,247,0.12) 100%);
}
</style>

<div style="max-width: 900px; margin: 0 auto; padding: 40px 24px 0;">

## 你想学什么？

<div style="text-align: center; margin-bottom: 32px; font-size: 18px; color: var(--vp-c-text-2);">
  <TextType :text="['用 AI IDE 做出第一个产品', '让 Claude Code 参与工程流程', '把 AI 接入真实应用', '用 RAG 构建知识库产品']" :typing-speed="80" :pause-duration="2000" :loop="true" />
</div>

<AnimatedFeatureCards :cards="[
  {
    icon: '🎮',
    gradient: 'linear-gradient(135deg, #667eea 0%, #764ba2 100%)',
    tag: '课程 A',
    title: '产品原型 + Claude Code',
    description: '16 周课程。面向非计算机专业学生，从 AI IDE 入门、需求验证、原型搭建到 Workflow、Skills、MCP 和 Agent Teams。',
    link: '/course-a/',
    linkText: '查看课程 A'
  },
  {
    icon: '🧩',
    gradient: 'linear-gradient(135deg, #f093fb 0%, #f5576c 100%)',
    tag: '课程 B',
    title: 'AI 全栈开发实战',
    description: '16 周课程。完成前端、数据库、AI 接口、支付部署、Dify、RAG、跨平台和 Agent 工程实践。',
    link: '/course-b/',
    linkText: '查看课程 B'
  },
  {
    icon: '📚',
    gradient: 'linear-gradient(135deg, #4facfe 0%, #00f2fe 100%)',
    tag: '共享',
    title: '工具与资源',
    description: '安装指南、工具对比、伦理安全材料。所有课程共用的基础资源。',
    link: '/shared/',
    linkText: '查看资源'
  }
]" />

</div>
