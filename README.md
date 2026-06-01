# AI Course System

面向高校和训练营的 AI 课程体系。当前仓库以 `docs/` VitePress 课程网站为发布主体，根目录保留教师备课材料、示例项目、评分表和共享资源。

正式站点：

- GitHub Pages: https://shirosoralumie648.github.io/ai-course-system/

## 当前入口

- 课程网站首页：`docs/index.md`
- 课程 A：`docs/course-a/index.md`
- 课程 B：`docs/course-b/index.md`
- 共享资源：`docs/shared/index.md`
- 站点配置：`docs/.vitepress/config.mjs`

本地预览：

```bash
cd docs
npm install
npm run dev -- --host 0.0.0.0
```

构建检查：

```bash
cd docs
npm run build
```

GitHub Pages 部署由 `.github/workflows/deploy-pages.yml` 自动执行。推送到 `main` 后，Actions 会以 `BASE=/ai-course-system/` 构建并发布 `docs/.vitepress/dist`。

## 课程结构

| 课程 | 当前定位 | 入口 |
| --- | --- | --- |
| 课程 A | 面向非计算机专业学生，用 AI IDE 和 Claude Code 做出第一个产品原型 | `docs/course-a/` |
| 课程 B | 面向有编程基础的学生，完成 AI 全栈开发、RAG、跨平台和 Agent 工程实践 | `docs/course-b/` |
| 共享资源 | 安装指南、工具对比、Git/GitHub、图片需求等公共材料 | `docs/shared/` |

## 仓库结构

```text
ai-course-system/
├── README.md                         # 项目入口
├── docs/                             # VitePress 课程网站源码
│   ├── .vitepress/                   # VitePress 配置与主题
│   ├── course-a/                     # 课程 A 网站内容
│   ├── course-b/                     # 课程 B 网站内容
│   └── shared/                       # 网站公共资源页
├── course-a-prompt-engineering/       # 课程 A 早期教师备课材料和 PPT 源材料
├── course-b-agentic-development/      # 课程 B 示例项目、模板、教师材料和实验支撑文件
├── shared/                           # 根目录公共安装和工具材料
├── assessment/                       # 通用评分表和互评表
└── .gitignore                        # 排除依赖、构建产物和本地归档
```

## 示例项目

课程 B 的部分实验会引用根目录示例项目：

- `course-b-agentic-development/examples/repo-01-small-bugfix/`
- `course-b-agentic-development/examples/repo-02-feature-development/`

这些示例项目需要保留在仓库中，否则 `docs/course-b/labs/` 中的实验命令会失效。

## 整理规则

已过时的规划、交付报告、参考分析、组件调试页、构建产物和本地执行计划不作为发布内容提交。它们已整理到 `.local-archive/outdated-docs/2026-06-01/`，并由 `.gitignore` 排除。

保留内容的判断标准：

- `docs/` 中当前站点需要的页面、图片、主题和配置。
- 课程实验明确引用的示例项目、模板和支撑材料。
- 教师备课仍可能用到的课程源材料、PPT、评分表和安装指南。

## 当前状态

当前版本可以作为课程网站初版和教学材料库继续迭代，但还不是正式 V1.0。后续发布前仍需要完成：

- 部署到正式 GitHub Pages 或其他静态站点。
- 抽查关键页面、图片和实验链接。
- 根据真实学生或助教试跑结果修订实验步骤。
- 对课件视觉、讲义深度和跨平台内容做教学验证。
