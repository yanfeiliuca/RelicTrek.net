# 全站标准化计划

## 目标
以Terraria中英文页面布局为标准模板，全站所有游戏所有物品页面核查并修复。

## Terraria标准模板特征
1. `<nav class="top-nav">` — 顶部导航
2. `<button class="menu-toggle">` — 汉堡菜单
3. `<a href="../" class="logo">RelicTrek</a>` — Logo
4. `<input type="search">` — 搜索框
5. `<div class="lang-switch">` — 语言切换(EN/中文按钮)
6. `<div class="nav-links">` — Blog/Games/About导航
7. `<div class="ticker-bar">` — 滚动标语
8. `<div class="main-layout">` — 主布局
9. `<aside class="left-sidebar">` — 左侧游戏导航
10. `<main class="content-area">` — 内容区域
11. `<aside class="right-sidebar">` — 右侧信息
12. `<footer class="site-footer">` — 页脚

## 老格式特征(需修改)
- `<nav class="nav">` 不是 `<nav class="top-nav">`
- `<div class="nav-logo">` 不是 `<a class="logo">`
- `<div class="news-ticker">` 或 `<div class="ticker">` 不是 `ticker-bar`
- `<div class="container">` 不是 `main-layout`
- 标签页导航 (Overview/Acquisition...)
- Item Info / QUICK INFO 面板

## 执行阶段

### Stage 1: 扫描识别 (并行)
- 13个游戏各派一个子代理扫描EN+ZH物品页面
- 识别老格式页面和语言切换链接错误
- 输出：问题页面清单

### Stage 2: 修复 (并行)
- 按游戏分组修复老格式页面
- 每个子代理处理一个游戏
- 标准模板替换 + 语言切换链接修复

### Stage 3: 验证
- 全站重新扫描确认
