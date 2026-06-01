# 第 11 周：跨平台开发进阶——PWA 让网页变成真正的 App

> **一个想法,未必只有一种活法。** 小哲已经能做出像样的网页了。但这周他第一次意识到：同一个产品,做成网站、小程序还是 App,命运完全不同。选错平台,写得再好也没人用。更重要的是,他发现有一种技术能让网页「装进手机」,离线也能用——这就是 PWA。

<ChapterIntroduction duration="2 课时(约 4 小时)" output="一个可安装到手机桌面、支持离线使用的 PWA 应用 + 平台选型决策表" prerequisite="能独立用 AI 辅助做出一个 Web 应用;理解前后端基本概念;会用 Vercel 部署站点" :tags="['PWA', '跨平台开发', '离线应用', 'Service Worker', 'Manifest', '平台选型']">

你会先学会一件比写代码更重要的事:**根据用户和场景,选对目标平台。** 然后跟着小哲深入 PWA 技术,把一个普通网页改造成可以安装、可以离线使用的「真正的 App」,并了解跨平台开发的完整路径。

</ChapterIntroduction>

<StepBar :active="0" :items="[
  { title: '① 小哲的新困惑', description: '网页做完了,然后呢' },
  { title: '② 认识平台全景', description: 'Web / 小程序 / App 各有命' },
  { title: '③ 学会选平台', description: '三个问题 + 决策表' },
  { title: '④ PWA 深度实战', description: '让网页变成可安装的 App' },
  { title: '⑤ 跨平台技术图谱', description: '从 PWA 到更多可能' }
]" />

---

## 1. 小哲的新困惑：网页做完了,然后呢

前几周小哲已经能用 AI 辅助做出一个完整的 Web 应用——一个「校园二手书」的小工具,注册、发布、搜索都跑得通。他兴冲冲地把链接发到班级群,结果只有两个人点开,还有人回了一句:「这能在微信里直接用吗?我懒得复制链接到浏览器。」

小哲愣住了。功能没问题,技术没问题,可产品就是没人用。问题出在哪?

::: warning 小哲的教训
他第一次意识到:**「能跑」和「有人用」是两件事。** 用户每天泡在微信里,你却让他们跳出去打开浏览器;用户想在地铁上随手记一笔,你做的却是个必须联网的网页。平台没选对,再好的代码也只是自嗨。
:::

这周要解决的就是这个问题:**当你有一个想法时,怎么判断它该做成网站、小程序,还是 App,然后用 AI 帮你真正把它落地。**

---

## 2. 认识战场：主流平台全景

在纠结「选哪个」之前,小哲先花了点时间搞清楚「有哪些」。他把面向普通用户的几类平台整理成一张表:

| 平台 | 一句话理解 | 强在哪 | 弱在哪 |
|---|---|---|---|
| **网站 / Web** | 浏览器里输入网址就能开 | 任何设备能访问、SEO 能被搜到、无需安装 | 必须联网、入口分散、留存差 |
| **PWA** | 网页加个「添加到主屏幕」就变 App | 一套代码多端通用、可离线使用、即时更新 | 很多人不知道能这么用、能力不如原生 |
| **微信小程序** | 微信里搜名字、扫码就能用的小应用 | 用户门槛极低、微信内可传播、获客成本低 | 功能受限、只能在微信里跑 |
| **iOS / Android 原生 App** | 应用商店下载安装的软件 | 性能最好、能深度调用硬件、可后台运行、推送可靠 | 开发成本高、要过审、iOS 还得有 Mac |

<InfoCard icon="💡" variant="tip">
**不要一上来就分技术路线**

新手最容易犯的错,是先纠结用 React 还是 Vue、用原生还是框架。但平台选型是**产品决策**,不是技术决策。先想清楚用户在哪、场景是什么,技术只是实现手段。小哲后来明白:选错平台,技术选得再对也白搭。
</InfoCard>

::: tip 还有更多「中间路线」
除了上面四类,还有跨端框架(React Native / Flutter / uni-app)、桌面程序(Electron / Qt)、浏览器插件、各家小程序(支付宝 / 抖音)等等。这周先聚焦最常用的 Web、PWA 和移动端三条线,其余等真正需要时再深入。
:::

---

## 3. 学会选平台：先问自己三个问题

小哲发现,与其背平台清单,不如学会一套提问的方法。每次有新想法,他都会先问自己三件事。

**问题一：你的用户在哪里?**
- 用户习惯在微信里完成操作吗? → 倾向小程序
- 用户需要随时随地、甚至离线使用吗? → 倾向 PWA 或移动端 App
- 用户需要通过搜索引擎找到你吗? → 倾向网站

**问题二：你的应用需要什么能力?**
- 要调用摄像头、GPS、健康数据这类硬件吗?
- 要后台持续运行、可靠推送吗?
- 要处理大量本地数据、离线可用吗?

**问题三：你的资源有多少?**
- 开发时间预算多少?
- 有没有 Mac 设备(做 iOS 必需)?
- 是否需要一次覆盖多个平台?

把这三个问题的答案拼起来,方向就清晰了。小哲整理出一张自己常用的速查表:

| 你的场景 | 推荐平台 | 原因 |
|---|---|---|
| 用户在微信里,想快速获客、社交传播 | 微信小程序 | 无需下载、群里一发就能用、获客成本低 |
| 工具类应用,需要离线使用、快速访问 | PWA | 可安装到桌面、离线可用、一套代码多端 |
| 需要后台记录 GPS 轨迹、读取健康数据 | iOS / Android 原生 | 直接调系统 API,性能与精度最优 |
| 高频快速记录(记账、打卡) | 原生 App 或 PWA | 启动快、体验流畅、推送可靠 |
| 想被搜索引擎搜到、做内容沉淀 | 网站 / 博客 | SEO 友好,长期可运营 |
| 想一套代码覆盖多端、快速迭代 | PWA / uni-app | 开发效率高,维护成本低 |

回到他那个「校园二手书」的例子:用户全在班级微信群里,用完即走,没人愿意为这个专门装 App。答案很清楚——**这本该是个微信小程序。**

但如果是一个「番茄钟专注工具」,用户需要随时打开、离线也能用、最好能装在桌面上一键启动,那 **PWA 就是最佳选择**。

::: warning 复杂业务常常是「组合拳」
不要执着于只选一个平台。一个在线教育产品,可能用**网站做获客和 SEO**、用**小程序做转化和触达**、再用**App 承载核心学习体验**。先想清楚每个平台各自负责什么,再分头落地。
:::

---

## 4. PWA 深度实战：让网页变成真正的 App

方向定了,小哲决定深入学习 PWA 技术。他发现这个技术特别适合「用 AI 快速验证想法」的场景——不用学 Swift 或 Kotlin,不用配置复杂的原生开发环境,就能做出一个可以装进手机、离线也能用的应用。

### 4.1 什么是 PWA?

**PWA(Progressive Web App)** 是一种特殊的网页,它通过 **Service Worker** 技术获得了「缓存并接管自己」的能力。

<AiChat title="小哲问 AI：PWA 和普通网站有什么区别?" :messages="[
  { role: 'user', content: '为什么普通网站不能离线,PWA 可以?' },
  { role: 'assistant', content: '普通网站每次打开都要从服务器下载 HTML、CSS、JS 文件,断网就彻底打不开。而 PWA 首次访问时会通过 Service Worker(一个运行在浏览器后台的 JS 脚本)把这些文件缓存到本地。之后即使断网,Service Worker 会直接从本地缓存读取文件,让页面正常显示。\n\n打个比方:普通网站像每次去图书馆借书(必须有网),PWA 像把书买回家放书架上(首次下载后,离线也能看)。' }
]" />

**PWA vs 普通网站 vs 原生 App**

| 特性 | 普通网站 | PWA | 原生 App |
|------|---------|-----|---------|
| **安装** | 不需要 | 可选(添加到桌面) | 必须从应用商店下载 |
| **离线使用** | ❌ 不能 | ✅ 能(缓存后) | ✅ 能 |
| **更新方式** | 自动刷新 | 自动/后台更新 | 用户手动更新 |
| **体积** | 无 | 几百 KB~几 MB | 几十 MB 以上 |
| **开发成本** | 低 | 低(一套代码) | 高(iOS/Android 分开) |

<InfoCard icon="🎯" variant="tip">
**PWA 的三大核心能力**

1. **可安装性(Installable)**：通过 Manifest 文件,用户可以把网页「添加到主屏幕」,像原生 App 一样启动
2. **离线可用(Offline-capable)**：通过 Service Worker 缓存资源,断网也能正常使用
3. **渐进增强(Progressive)**：在支持的浏览器上提供完整体验,在老旧浏览器上降级为普通网页
</InfoCard>

### 4.2 PWA 的技术组成

要把一个普通网页变成 PWA,需要三个关键文件:

**① Manifest 文件(manifest.json)**

这是 PWA 的「身份证」,告诉浏览器这个应用叫什么、图标是什么、用什么颜色主题:

```json
{
  "name": "番茄农场",
  "short_name": "番茄农场",
  "description": "专注种菜,收获成长",
  "start_url": "/",
  "display": "standalone",
  "theme_color": "#4CAF50",
  "background_color": "#ffffff",
  "icons": [
    {
      "src": "/icon-192.png",
      "sizes": "192x192",
      "type": "image/png"
    },
    {
      "src": "/icon-512.png",
      "sizes": "512x512",
      "type": "image/png"
    }
  ]
}
```

**② Service Worker(sw.js)**

这是 PWA 的「大脑」,运行在浏览器后台,负责拦截网络请求、缓存资源:

```javascript
// 安装阶段:缓存核心资源
self.addEventListener('install', (event) => {
  event.waitUntil(
    caches.open('v1').then((cache) => {
      return cache.addAll([
        '/',
        '/index.html',
        '/styles.css',
        '/app.js',
        '/icon-192.png'
      ])
    })
  )
})

// 请求阶段:优先从缓存读取
self.addEventListener('fetch', (event) => {
  event.respondWith(
    caches.match(event.request).then((response) => {
      return response || fetch(event.request)
    })
  )
})
```

**③ HTML 中的引用**

在 `index.html` 的 `<head>` 中引入 Manifest:

```html
<link rel="manifest" href="/manifest.json">
<meta name="theme-color" content="#4CAF50">
```

### 4.3 实战案例:番茄农场 PWA

小哲决定做一个「番茄农场」应用——结合番茄钟工作法和种菜游戏,专注 25 分钟就能获得积分,用积分买种子种菜。这个应用特别适合做成 PWA:

- **需要离线使用**:用户在地铁上、图书馆里也要能用
- **需要快速启动**:从桌面图标一键打开,不用每次输入网址
- **需要跨平台**:电脑、手机、平板都要能用

<StepBar :active="0" :items="[
  { title: '① 创建项目', description: '用 Vite 搭建 React 项目' },
  { title: '② 开发功能', description: 'AI 辅助实现番茄钟和种菜系统' },
  { title: '③ 配置 PWA', description: '添加 Manifest 和 Service Worker' },
  { title: '④ 测试离线', description: '验证断网后能否正常使用' },
  { title: '⑤ 部署上线', description: 'Vercel 部署并在手机安装' }
]" />

#### 步骤 1：创建项目骨架

小哲打开 AI 编程助手,输入第一条指令:

```
请帮我创建一个 React 项目,项目名叫 tomato-farm-pwa,用来做番茄农场应用。
需要支持 TypeScript,并且加上 PWA 功能(就是能让网页安装到手机桌面的那种)。
```

AI 会自动执行:

```bash
npm create vite@latest tomato-farm-pwa -- --template react-ts
cd tomato-farm-pwa
npm install
npm install vite-plugin-pwa -D
```

项目结构:

```
tomato-farm-pwa/
├── public/              # 静态资源(图标、SVG 素材)
├── src/
│   ├── App.tsx          # 主组件
│   ├── main.tsx         # 入口文件
│   └── App.css          # 样式
├── vite.config.ts       # Vite 配置(PWA 配置写这里)
└── package.json
```

#### 步骤 2：配置 PWA 插件

在 `vite.config.ts` 中配置 PWA:

**修改前:**

```ts
import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

export default defineConfig({
  plugins: [react()]
})
```

**修改后:**

```ts
import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'
import { VitePWA } from 'vite-plugin-pwa'

export default defineConfig({
  plugins: [
    react(),
    VitePWA({
      registerType: 'autoUpdate',
      manifest: {
        name: '番茄农场',
        short_name: '番茄农场',
        description: '专注种菜,收获成长',
        theme_color: '#4CAF50',
        background_color: '#ffffff',
        display: 'standalone',
        icons: [
          {
            src: '/icon-192.png',
            sizes: '192x192',
            type: 'image/png'
          },
          {
            src: '/icon-512.png',
            sizes: '512x512',
            type: 'image/png'
          }
        ]
      },
      workbox: {
        globPatterns: ['**/*.{js,css,html,ico,png,svg}']
      }
    })
  ]
})
```

**关键配置解读:**

- `registerType: 'autoUpdate'`:当你发布新版本时,用户下次打开会自动更新
- `display: 'standalone'`:安装后以独立窗口运行,没有浏览器地址栏
- `workbox.globPatterns`:告诉 Service Worker 要缓存哪些文件

#### 步骤 3：用 AI 开发核心功能

小哲向 AI 发出「总指令」:

```
请帮我写番茄农场应用的主页面,包含以下功能:

**番茄钟功能:**
- 一个 25 分钟的倒计时器,可以开始、暂停、重置
- 显示剩余时间和进度条
- 专注完成后给用户 10 个积分

**种菜功能:**
- 3 块菜地,最开始只有第 1 块能用,后面的要升级解锁
- 商店里可以买菜籽:胡萝卜 5 积分、番茄 10 积分、玉米 15 积分
- 买了种子种到地里,作物会慢慢长大,成熟后可以收获换积分

**等级系统:**
- 根据总积分升级:0-100 分是新手农民,100-300 分是熟练农民,300 分以上是农场大师
- 升级后解锁新的菜地和更高级的种子

**界面设计:**
- 顶部显示等级、积分和升级进度条
- 中间是番茄钟倒计时
- 下面是菜地网格
- 底部是商店按钮
- 整体用绿色主题,看起来清新可爱
- 要能适配手机屏幕

**数据保存:**
- 所有数据(积分、等级、菜地状态)都要保存到 localStorage,刷新页面不会丢失
```

<AiChat title="AI 的实现思路" :messages="[
  { role: 'assistant', content: '我会这样实现:\n\n1. **状态管理**:用 useState 管理积分、等级、菜地状态、番茄钟倒计时\n2. **番茄钟逻辑**:用 setInterval 实现倒计时,完成后触发积分增加\n3. **种菜系统**:每块地有状态(空闲/种植中/成熟),用 setTimeout 模拟作物生长\n4. **数据持久化**:用 useEffect 监听状态变化,自动保存到 localStorage\n5. **响应式布局**:用 CSS Grid 和 Flexbox,配合媒体查询适配手机\n\n现在开始修改 App.tsx...' }
]" />

AI 会生成完整的 `App.tsx` 代码。核心逻辑片段:

**修改前:**

```tsx
// 空白项目
function App() {
  return <div>Hello World</div>
}
```

**修改后:**

```tsx
function App() {
  const [timeLeft, setTimeLeft] = useState(25 * 60) // 25分钟
  const [isRunning, setIsRunning] = useState(false)
  const [points, setPoints] = useState(0)

  useEffect(() => {
    if (!isRunning) return

    const timer = setInterval(() => {
      setTimeLeft(prev => {
        if (prev <= 1) {
          setIsRunning(false)
          setPoints(p => p + 10) // 完成后奖励10积分
          return 25 * 60
        }
        return prev - 1
      })
    }, 1000)

    return () => clearInterval(timer)
  }, [isRunning])

  return (
    <div className="app">
      <div className="timer">
        {Math.floor(timeLeft / 60)}:{(timeLeft % 60).toString().padStart(2, '0')}
      </div>
      <button onClick={() => setIsRunning(!isRunning)}>
        {isRunning ? '暂停' : '开始'}
      </button>
    </div>
  )
}
```

#### 步骤 4：准备应用图标

PWA 需要图标才能被安装。让 AI 帮你生成:

```
请帮我生成两个应用图标,尺寸分别是 192x192 和 512x512。
背景用绿色渐变,中间画一个红色番茄,保存到 public 文件夹里,
文件名分别是 icon-192.png 和 icon-512.png。
```

或者用 Figma/Canva 自己设计一个,放到 `public/` 目录。

#### 步骤 5：本地测试

启动开发服务器:

```bash
npm run dev
```

打开浏览器访问 `http://localhost:5173`,你会看到番茄农场应用已经跑起来了。

<InfoCard icon="🔍" variant="tip">
**如何验证 PWA 配置是否生效?**

1. 打开 Chrome DevTools(F12)
2. 切换到「Application」标签
3. 左侧找到「Manifest」,检查图标、名称是否正确
4. 左侧找到「Service Workers」,检查是否已注册
5. 地址栏右侧应该出现「安装」图标(⊕)
</InfoCard>

#### 步骤 6：测试离线能力

这是 PWA 最关键的测试:

1. 在 Chrome DevTools 的「Network」标签中,勾选「Offline」
2. 刷新页面
3. 如果页面仍然能正常显示,说明 Service Worker 缓存生效了!

| 普通网站 | PWA 应用 |
| --- | --- |
| 断网后刷新会显示「无法访问此网站」 | 断网后刷新页面仍能正常显示 |
| 所有功能不可用 | 番茄钟和种菜系统继续运行 |
| 数据可能丢失 | 数据保存在 localStorage,不会丢失 |

### 4.4 部署到 Vercel 并在手机安装

PWA 必须在 HTTPS 环境下才能安装(localhost 除外)。小哲选择用 Vercel 部署:

**① 构建生产版本**

```bash
npm run build
```

这会在 `dist/` 目录生成优化后的文件,包括自动生成的 Service Worker。

**② 部署到 Vercel**

```bash
# 安装 Vercel CLI
npm i -g vercel

# 登录并部署
vercel
```

按提示操作,几分钟后你会得到一个 HTTPS 地址,比如 `https://tomato-farm-pwa.vercel.app`。

**③ 在手机上安装**

1. 用手机浏览器(Chrome/Safari)打开部署后的网址
2. 点击浏览器菜单中的「添加到主屏幕」
3. 确认后,桌面上会出现「番茄农场」图标
4. 点击图标启动,体验和原生 App 一样!

<InfoCard icon="📱" variant="success">
**恭喜!你已经完成了一个完整的 PWA 应用**

现在你可以:
- 从手机桌面一键启动应用
- 在地铁上离线使用(断网也能专注种菜)
- 自动获取更新(下次部署新版本,用户会自动更新)
- 跨平台使用(同一个应用在电脑、手机、平板都能装)
</InfoCard>

### 4.5 PWA 的进阶能力

完成基础版本后,小哲发现 PWA 还有很多进阶能力可以探索:

**① 推送通知(Push Notifications)**

可以在用户允许后发送通知,比如「你的番茄已经成熟了!」

```javascript
// 请求通知权限
Notification.requestPermission().then(permission => {
  if (permission === 'granted') {
    new Notification('番茄农场', {
      body: '你的番茄已经成熟,快来收获吧!',
      icon: '/icon-192.png'
    })
  }
})
```

**② 后台同步(Background Sync)**

当用户离线时操作的数据,可以在恢复网络后自动同步到服务器。

**③ 分享功能(Web Share API)**

让用户可以把应用分享给朋友:

```javascript
if (navigator.share) {
  navigator.share({
    title: '番茄农场',
    text: '我在用番茄农场专注学习,一起来种菜吧!',
    url: 'https://tomato-farm-pwa.vercel.app'
  })
}
```

**④ 安装提示(Install Prompt)**

主动引导用户安装应用:

```javascript
let deferredPrompt

window.addEventListener('beforeinstallprompt', (e) => {
  e.preventDefault()
  deferredPrompt = e
  
  // 显示自定义的安装按钮
  document.getElementById('install-btn').style.display = 'block'
})

document.getElementById('install-btn').addEventListener('click', () => {
  deferredPrompt.prompt()
  deferredPrompt.userChoice.then((choiceResult) => {
    if (choiceResult.outcome === 'accepted') {
      console.log('用户安装了应用')
    }
  })
})
```

<AiChat title="小哲问 AI：PWA 能完全替代原生 App 吗?" :messages="[
  { role: 'user', content: 'PWA 这么强大,是不是可以完全替代原生 App 了?' },
  { role: 'assistant', content: '不能完全替代,但能覆盖 80% 的场景。\n\n**PWA 适合的场景:**\n- 内容展示类(新闻、博客、文档)\n- 工具类(计算器、番茄钟、记账)\n- 轻量游戏(2D 小游戏)\n- 表单和数据录入\n\n**仍需原生 App 的场景:**\n- 需要深度硬件访问(蓝牙、NFC、AR)\n- 需要后台持续运行(健康追踪、定位)\n- 需要复杂的本地数据处理(大型游戏、视频编辑)\n- 需要应用商店的品牌背书\n\n**建议策略:**\n先用 PWA 快速验证想法,如果用户量起来了、需求变复杂了,再考虑做原生 App。很多成功产品都是这个路径,比如 Twitter Lite 就是先做 PWA,后来才补充原生 App。' }
]" />

---

## 5. 跨平台技术图谱：从 PWA 到更多可能

掌握了 PWA 后,小哲对跨平台开发有了更全面的认识。他整理了一张技术图谱:

### 5.1 跨平台方案对比

| 方案 | 技术栈 | 性能 | 开发成本 | 适用场景 |
|------|--------|------|---------|---------|
| **PWA** | HTML/CSS/JS | ⭐⭐⭐ | 最低 | 工具类、内容类、轻量应用 |
| **uni-app** | Vue | ⭐⭐⭐⭐ | 低 | 小程序 + H5 + App 一体化 |
| **React Native** | React | ⭐⭐⭐⭐ | 中 | 需要接近原生体验的 App |
| **Flutter** | Dart | ⭐⭐⭐⭐⭐ | 中 | 追求极致性能和一致体验 |
| **Electron** | HTML/CSS/JS | ⭐⭐⭐ | 低 | 桌面应用(VS Code 就是用它做的) |
| **原生开发** | Swift/Kotlin | ⭐⭐⭐⭐⭐ | 最高 | 需要深度系统集成 |

<InfoCard icon="🎯" variant="tip">
**小哲的选择策略**

1. **验证想法阶段**:优先 PWA,最快上线
2. **需要微信生态**:用 uni-app,一套代码发布小程序 + H5
3. **需要原生体验**:React Native(如果会 React) 或 Flutter(追求性能)
4. **需要桌面应用**:Electron,可以复用 Web 代码
5. **需要极致性能**:原生开发,但成本最高
</InfoCard>

### 5.2 小程序开发快速入门

如果小哲的「校园二手书」要做成微信小程序,流程是这样的:

**① 注册小程序账号**

访问 [微信公众平台](https://mp.weixin.qq.com/),注册小程序,获取 AppID。

**② 选择开发方式**

- **原生开发**:用微信开发者工具 + WXML/WXSS
- **uni-app**:用 Vue 语法,一套代码多端发布
- **Taro**:用 React 语法,也支持多端

**③ 用 AI 辅助开发**

```
请帮我创建一个 uni-app 小程序项目,实现校园二手书交易功能:
- 首页显示书籍列表,支持搜索
- 发布页可以上传书籍照片、填写书名、价格、描述
- 详情页显示书籍信息和卖家联系方式
- 用户需要微信登录才能发布和查看联系方式
- 数据存储用 Supabase
```

**④ 预览和发布**

用微信开发者工具扫码预览,测试通过后提交审核,一般 1-3 天通过。

### 5.3 移动端原生开发入门

如果需求超出了 PWA 和小程序的能力边界,就要考虑原生开发了。

**iOS 开发(Swift)**

- **必需工具**:Mac 电脑 + Xcode
- **学习曲线**:中等,Swift 语法相对友好
- **AI 辅助**:可以让 AI 生成 SwiftUI 代码

```
请帮我用 SwiftUI 创建一个简单的番茄钟 App:
- 显示 25 分钟倒计时
- 有开始、暂停、重置按钮
- 完成后播放提示音并发送本地通知
- 用 UserDefaults 保存完成次数
```

**Android 开发(Kotlin)**

- **必需工具**:Android Studio
- **学习曲线**:中等,Kotlin 比 Java 简洁很多
- **AI 辅助**:可以让 AI 生成 Jetpack Compose 代码

```
请帮我用 Jetpack Compose 创建一个番茄钟 Android App:
- Material Design 3 风格
- 使用 ViewModel 管理状态
- 用 Room 数据库保存历史记录
- 支持深色模式
```

| 方案 | 代码组织 | 代码量 | 维护成本 |
| --- | --- | --- | --- |
| PWA/跨平台 | 一套 `App.tsx` 同时适配 Web、iOS、Android | 约 300 行 | 低 |
| 原生开发 | iOS 使用 `ContentView.swift`,Android 使用 `MainActivity.kt` | 约 400 行 | 高,两套代码要同步更新 |

### 5.4 浏览器扩展开发

除了移动端,小哲还发现浏览器扩展也是一个有趣的方向——可以增强浏览器的能力。

**典型场景:**
- 网页内容提取(比如一键总结文章)
- 广告拦截
- 密码管理
- 翻译工具
- 开发者工具

**开发流程:**

```
请帮我创建一个 Chrome 浏览器扩展,功能是:
- 点击扩展图标后,在侧边栏显示当前网页的 AI 摘要
- 使用 Manifest V3
- 调用 OpenAI API 生成摘要
- 支持复制摘要到剪贴板
```

AI 会生成:
- `manifest.json`:扩展配置文件
- `background.js`:后台脚本
- `content.js`:注入到网页的脚本
- `sidepanel.html`:侧边栏界面

**发布:**
打包成 `.zip` 文件,提交到 [Chrome Web Store](https://chrome.google.com/webstore/devconsole)。

### 5.5 桌面应用开发(Electron)

如果要做桌面应用(Windows/Mac/Linux),Electron 是最流行的选择。

**为什么选 Electron?**
- 用 Web 技术(HTML/CSS/JS)开发桌面应用
- 一套代码跨三大桌面平台
- VS Code、Slack、Discord 都是用它做的

**快速上手:**

```
请帮我用 Electron 创建一个桌面版番茄钟应用:
- 窗口大小 400x600,不可调整大小
- 支持系统托盘,最小化到托盘
- 完成番茄钟后发送系统通知
- 支持全局快捷键(Ctrl+Shift+P)启动/暂停
- 数据保存到本地文件
```

**打包发布:**
用 `electron-builder` 打包成 `.exe`(Windows)、`.dmg`(Mac)、`.AppImage`(Linux)。

<InfoCard icon="💡" variant="tip">
**Electron 的优缺点**

**优点:**
- 开发效率高,可以复用 Web 代码
- 跨平台,一套代码三端发布
- 生态丰富,npm 包都能用

**缺点:**
- 体积大(最小也要 50MB+,因为内置了 Chromium)
- 内存占用高
- 性能不如原生应用

**适合场景:**
开发工具、办公软件、内容创作工具等对体积不敏感的应用。
</InfoCard>

---

## 6. 口袋开发：随时随地写代码

掌握了跨平台技术后,小哲发现还有一个有趣的方向:「口袋开发」——把开发环境装进手机。

### 6.1 什么是口袋开发?

传统开发必须坐在电脑前,但 AI 辅助编程让「瘦客户端架构」成为可能:

```
┌─────────────┐              ┌─────────────┐
│   手机      │   指令 ───►  │  电脑 / 云端 │
│  (控制端)   │   ◄─── 结果  │   (执行端)   │
│ 输入·查看·审查│              │ 运行·改码·访问│
└─────────────┘              └─────────────┘
```

**核心思想:**
- 手机只负责输入指令、查看输出、审查改动
- 真正的代码执行放在电脑或云端
- 通过 SSH、远程桌面或 Web IDE 连接

### 6.2 口袋开发的三种方案

**方案 A:手机 + 云端 IDE**

使用 GitHub Codespaces、Gitpod 等云端 IDE:
- 在手机浏览器打开 `github.dev`
- 直接在线编辑代码
- 云端自动运行和部署

**方案 B:手机 + 家里电脑(SSH)**

用 Termux(Android)或 iSH(iOS)通过 SSH 连接家里电脑:
```bash
# 手机上执行
ssh user@home-pc-ip
cd ~/projects/tomato-farm-pwa
npm run dev
```

**方案 C:手机 + AI 编程助手**

用 Claude、ChatGPT 的移动端 App:
- 描述需求,让 AI 生成代码
- 复制代码到 GitHub 或云端 IDE
- 在电脑上验证和部署

<AiChat title="小哲的口袋开发实践" :messages="[
  { role: 'user', content: '我在地铁上突然想到一个功能改进,但没带电脑,怎么办?' },
  { role: 'assistant', content: '你可以这样做:\n\n1. 打开手机上的 Claude App\n2. 描述你的改进想法:「请帮我给番茄农场加一个统计功能,显示本周完成了多少个番茄钟」\n3. AI 会生成代码,你复制保存到备忘录\n4. 回到电脑前,把代码粘贴到项目里,运行测试\n5. 如果有问题,继续和 AI 对话调整\n\n这样你在地铁上的 10 分钟就没浪费,回家直接能用!' }
]" />

::: warning 口袋开发的边界
越是「随手就能让 AI 改代码」,越要记住第 1 周的规则:**手机上发出的指令一样会真的改你的工程。** 危险操作(删文件、改依赖、碰密钥)依然要走人工确认,回到电脑前务必重新跑测试、审查 diff,再决定要不要提交。
:::

---

## 7. 小哲这周的转变

> 小哲重做完那个二手书应用,这次做成了 PWA,发到班级群后扫码就能装到手机桌面,当天就有十几个同学在用。他翻回自己第一版没人用的纯网页,突然想通了一件事。
>
> 他在笔记里写下:**「以前我以为做产品就是把功能写出来。现在我知道,第一步是先问『用户在哪、场景是什么』,再决定它该长成网站、PWA、小程序还是 App。选对平台,AI 才能帮我把它真正送到用户手里。」**
>
> 更重要的是,他掌握了 PWA 这个「性价比最高的跨平台方案」——不用学 Swift 或 Kotlin,不用配置复杂的原生环境,就能做出可以装进手机、离线也能用的应用。这让他的想法验证速度提升了 10 倍。

---

## 本周回顾

<ProgressTracker title="第 11 周学习进度" :items="[
  { title: '看懂了小哲的新困惑', description: '能跑 ≠ 有人用,平台选型是产品决策', done: false },
  { title: '认识了平台全景', description: 'Web / PWA / 小程序 / App 各自的强弱', done: false },
  { title: '学会了选平台的方法', description: '三个问题 + 场景决策表', done: false },
  { title: '深度掌握了 PWA 开发', description: 'Manifest + Service Worker + 离线能力 + 部署安装', done: false },
  { title: '了解了跨平台技术图谱', description: 'uni-app / React Native / Flutter / Electron / 原生开发', done: false },
  { title: '探索了口袋开发', description: '手机 + 云端 IDE / SSH / AI 助手', done: false }
]" />

**自测问题:**

1. 拿到一个产品想法时,你会用哪三个问题来判断它该上哪个平台?
2. PWA 的三大核心能力是什么?为什么 PWA 必须在 HTTPS 环境下才能安装?
3. Service Worker 在 PWA 中扮演什么角色?它是如何实现离线能力的?
4. 同样是「用完即走」的工具,为什么社区团购更适合小程序,而番茄钟更适合 PWA?
5. 如果你要做一个需要后台定位的跑步记录 App,为什么 PWA 不够用,必须上原生开发?

**实战作业:**

1. **必做**:完成番茄农场 PWA 的开发和部署,在手机上成功安装并测试离线功能
2. **选做 A**:给番茄农场加上推送通知功能,番茄成熟时提醒用户
3. **选做 B**:把你之前做过的一个 Web 应用改造成 PWA
4. **选做 C**:用 uni-app 把番茄农场改造成微信小程序版本

---

## 下周预告

下周是这门课的收官:**高级 Agent 工程技能 + 期末项目答辩。** 你会把前 11 周学到的——边界、验证、工作流、平台选型、跨端落地——整合成一套完整的工程能力,并亲手交付一个能讲清楚「做了什么、为什么这么做、怎么验证的」的期末项目。小哲也将带着他的番茄农场 PWA,走上答辩台。

---

## 附录:常见问题

### Q1:PWA 在 iOS 上的支持怎么样?

**A:**iOS 对 PWA 的支持一直比较保守,但从 iOS 16.4 开始有了明显改善:

- ✅ 支持添加到主屏幕
- ✅ 支持 Service Worker 和离线缓存
- ✅ 支持 Manifest 配置
- ❌ 不支持推送通知(这是最大的限制)
- ❌ 不支持后台同步

**建议:**如果你的应用严重依赖推送通知,iOS 上还是要做原生 App。但对于工具类、内容类应用,PWA 在 iOS 上已经够用了。

### Q2:PWA 能上架到应用商店吗?

**A:**可以!

- **Google Play**:支持 PWA 打包成 APK 上架(用 Trusted Web Activity 技术)
- **Microsoft Store**:直接支持 PWA 上架
- **App Store**:不直接支持,但可以用 Capacitor 或 Cordova 把 PWA 包装成原生 App 上架

工具推荐:
- [PWABuilder](https://www.pwabuilder.com/):一键把 PWA 打包成各平台的安装包
- [Capacitor](https://capacitorjs.com/):把 Web 应用包装成原生 App

### Q3:Service Worker 会不会影响性能?

**A:**不会,反而会提升性能:

- Service Worker 只在需要时启动,不会常驻内存
- 缓存策略可以让资源加载更快(从本地读取比从网络下载快得多)
- 可以配置「网络优先」或「缓存优先」策略,灵活控制

**最佳实践:**
- 静态资源(JS/CSS/图片)用「缓存优先」
- API 数据用「网络优先,失败时用缓存」
- 定期清理过期缓存

### Q4:PWA 的浏览器兼容性如何?

**A:**主流浏览器都支持,但程度不同:

| 浏览器 | Service Worker | Manifest | 安装提示 | 推送通知 |
|--------|---------------|----------|---------|---------|
| Chrome | ✅ | ✅ | ✅ | ✅ |
| Edge | ✅ | ✅ | ✅ | ✅ |
| Firefox | ✅ | ✅ | ✅ | ✅ |
| Safari | ✅ | ✅ | ✅ | ❌ |
| 微信浏览器 | ⚠️ 部分支持 | ❌ | ❌ | ❌ |

**建议:**
- 核心功能要做降级处理(检测浏览器能力)
- 用 `if ('serviceWorker' in navigator)` 判断是否支持
- 不支持的浏览器降级为普通网页

### Q5:如何调试 Service Worker?

**A:**Chrome DevTools 提供了完整的调试工具:

1. 打开 DevTools(F12)
2. 切换到「Application」标签
3. 左侧找到「Service Workers」
4. 可以看到:
   - Service Worker 的状态(激活/等待/停止)
   - 注册的作用域
   - 更新按钮(强制更新)
   - Unregister 按钮(注销)
5. 在「Cache Storage」中可以查看缓存的文件

**常用调试技巧:**
- 勾选「Update on reload」:每次刷新都更新 Service Worker
- 勾选「Bypass for network」:跳过 Service Worker,直接从网络加载
- 在「Console」中可以看到 Service Worker 的日志

### Q6:PWA 的更新策略是什么?

**A:**Service Worker 的更新是自动的,但有一些细节:

1. **检测更新**:浏览器会定期检查 Service Worker 文件是否变化
2. **下载新版本**:如果检测到变化,会在后台下载新的 Service Worker
3. **等待激活**:新版本会等待,直到所有旧版本的页面都关闭
4. **激活新版本**:用户下次打开应用时,新版本自动激活

**如何强制立即更新?**

```javascript
self.addEventListener('install', (event) => {
  self.skipWaiting() // 跳过等待,立即激活
})

self.addEventListener('activate', (event) => {
  event.waitUntil(clients.claim()) // 立即接管所有页面
})
```

**用户友好的更新提示:**

```javascript
// 检测到新版本时提示用户
navigator.serviceWorker.addEventListener('controllerchange', () => {
  if (confirm('发现新版本,是否刷新页面?')) {
    window.location.reload()
  }
})
```
