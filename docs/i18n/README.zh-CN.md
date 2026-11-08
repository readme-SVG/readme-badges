# README 徽章

**可直接复制使用的徽章集合，以及让 GitHub README 更清晰的实用指南。**

[![License](https://img.shields.io/github/license/readme-SVG/readme-badges?style=flat-square)](../../LICENSE)
[![GitHub stars](https://img.shields.io/github/stars/readme-SVG/readme-badges?style=flat-square)](https://github.com/readme-SVG/readme-badges/stargazers)
[![Last commit](https://img.shields.io/github/last-commit/readme-SVG/readme-badges?style=flat-square)](https://github.com/readme-SVG/readme-badges/commits/main)
[![PRs welcome](https://img.shields.io/badge/PRs-welcome-brightgreen?style=flat-square)](../../CONTRIBUTING.md)

[English](../../README.md) · [Español](README.es.md) · [Português (Brasil)](README.pt-BR.md) · [Русский](README.ru.md) · **简体中文** · [日本語](README.ja.md)

浏览 **23 个分类中的 699 个静态徽章示例**，了解静态徽章与动态徽章的区别，并复制适用于发布版本、构建状态、软件包版本、文档和社区链接的模板。无需安装任何应用。

| 资源 | 内容 |
| --- | --- |
| [**徽章目录 →**](../BADGE_CATALOG.md) | 完整集合：编程语言、框架、云服务、AI、测试、安全、游戏、硬件、社交链接等 |
| [**徽章指南 →**](../BADGE_GUIDE.md) | 徽章类型、URL 语法、样式、标志、动态数据、自定义端点、个人资料图形及故障排查 |
| [**参与贡献 →**](../../CONTRIBUTING.md) | 添加徽章、修复标志、改进示例或更新翻译 |

> [!TIP]
> 先放一行真正有用的徽章，而不是堆满标志。版本、构建状态、许可证和文档链接通常比二十个技术标签更能帮助访问者了解项目。

## 目录

- [快速开始](#快速开始)
- [徽章类型](#徽章类型)
- [样式](#样式)
- [动态徽章模板](#动态徽章模板)
- [浏览完整目录](#浏览完整目录)
- [几个即用徽章](#几个即用徽章)
- [GitHub Markdown 提示框](#github-markdown-提示框)
- [GitHub 表情代码](#github-表情代码)
- [推荐做法](#推荐做法)
- [故障排查](#故障排查)
- [贡献与翻译](#贡献与翻译)
- [许可证](#许可证)

## 快速开始

徽章就是 Markdown 图片。将图片包在链接中，就可以点击跳转：

```markdown
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)

[![Documentation](https://img.shields.io/badge/docs-read-blue)](https://example.com/docs)
```

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)

1. 打开[目录](../BADGE_CATALOG.md)，找到徽章，然后通过 GitHub 的 **Raw** 原始文件视图复制 Markdown。
2. 粘贴到 README 中。个人资料 README 通常位于 `你的用户名/你的用户名` 仓库。
3. 修改标签、颜色、标志或目标链接。对于动态徽章，请按照[指南](../BADGE_GUIDE.md#4-dynamic-badges)替换 `OWNER`、`REPO` 等占位符。

Shields 的基本 URL 为 `https://img.shields.io/badge/LABEL-MESSAGE-COLOR`。将 `#` 编码为 `%23`，将字面连字符转义为 `--`，空格使用 `_` 或 `%20`。参阅[完整转义表](../BADGE_GUIDE.md#escaping-rules)。

## 徽章类型

“徽章类型”既可以指图片如何获取值，**也可以**指这个值表达什么。按实现方式主要分为以下几类：

| 类型 | 示例 | 是否自动更新？ |
| --- | --- | --- |
| **静态** | `Python`、`status: beta`、`PRs welcome` | 否——需要编辑 Markdown |
| **服务驱动动态** | GitHub 星标、npm 版本、CI 状态 | 是——服务商读取来源服务 |
| **动态数据** | 从你的 JSON API 读取版本 | 是——服务商读取你的数据 |
| **端点** | 你的服务器提供标签、消息和颜色 | 是——你负责维护 JSON 端点 |
| **生成式图形** | 统计卡片、横幅、贡献贪吃蛇 | 取决于生成器或工作流计划 |

常见用途包括发布版本、构建健康度、测试覆盖率、兼容性、许可证、下载量、社区、赞助和个人资料统计。[分类与配方](../BADGE_GUIDE.md#1-what-is-a-badge)说明了各种类型的适用场景。

> [!IMPORTANT]
> 静态徽章只是标签，不是验证结果。“安全”或“100% 已测试”不会因为显示为绿色就变成事实。需要证据时，请使用链接到实际结果的动态徽章。

## 样式

同一视觉分组内尽量使用同一种样式。在 Shields URL 后添加 `?style=STYLE`：

| 样式 | 预览 |
| --- | --- |
| `plastic` | ![Plastic](https://img.shields.io/badge/style-plastic-blue?style=plastic) |
| `flat` | ![Flat](https://img.shields.io/badge/style-flat-blue?style=flat) |
| `flat-square` | ![Flat square](https://img.shields.io/badge/style-flat--square-blue?style=flat-square) |
| `social` | ![Social](https://img.shields.io/badge/style-social-blue?style=social&logo=github) |
| `for-the-badge` | ![For the badge](https://img.shields.io/badge/style-for--the--badge-blue?style=for-the-badge) |

目录使用 `for-the-badge`。[指南](../BADGE_GUIDE.md#3-styles-colors-and-logos)还介绍了颜色、标志 slug、已移除的品牌图标以及明暗主题。

## 动态徽章模板

将 `OWNER/REPO` 替换为你的仓库。这些示例从 GitHub 获取更新，数字不是手动写死的。

```markdown
[![Release](https://img.shields.io/github/v/release/OWNER/REPO)](https://github.com/OWNER/REPO/releases)
[![License](https://img.shields.io/github/license/OWNER/REPO)](LICENSE)
[![CI](https://img.shields.io/github/actions/workflow/status/OWNER/REPO/ci.yml?branch=main)](https://github.com/OWNER/REPO/actions/workflows/ci.yml)
[![Open issues](https://img.shields.io/github/issues/OWNER/REPO)](https://github.com/OWNER/REPO/issues)
```

请将 `ci.yml` 替换为真实的工作流文件名。软件包版本可以尝试 `https://img.shields.io/npm/v/PACKAGE` 或 `https://img.shields.io/pypi/v/PACKAGE`。指南提供了 [GitHub 模板](../BADGE_GUIDE.md#5-github-badges)、[注册表与质量徽章](../BADGE_GUIDE.md#6-packages-builds-and-quality)以及[自定义 JSON 端点](../BADGE_GUIDE.md#8-custom-dynamic-and-endpoint-badges)。

## 浏览完整目录

全部 **699 个示例**都在 [**docs/BADGE_CATALOG.md**](../BADGE_CATALOG.md) 中，并附有可点击的目录。原有集合完整保留，并新增了 **224 个示例**。

| 领域 | 包含的分类 |
| --- | --- |
| 语言与应用 | 编程语言、前端、后端、跨平台应用 |
| 基础设施 | 数据库、云服务/DevOps、搜索/向量数据库、可观测性 |
| 现代开发 | AI 助手/智能体、测试/代码质量、安全/身份认证 |
| 专业栈 | 游戏开发、IoT/嵌入式硬件、区块链/Web3 |
| 产品与用户 | 工具/编辑器、浏览器/操作系统、数据科学、CMS/无代码、办公/商业、社交/联系 |
| 项目沟通 | 项目状态/社区、文档/出版、无障碍/本地化 |

这些都是静态标签。部分标志已从 Simple Icons 中移除，因此相应徽章有意使用可读文本，而不是损坏或不相关的图标。参阅[标志替代方案](../BADGE_GUIDE.md#named-logos-and-removed-brands)。

## 几个即用徽章

```markdown
![Maintained](https://img.shields.io/badge/Maintained-yes-brightgreen?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-beta-orange?style=for-the-badge)
![React](https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)
![GitHub Copilot](https://img.shields.io/badge/GitHub%20Copilot-000000?style=for-the-badge&logo=githubcopilot&logoColor=white)
```

![Maintained](https://img.shields.io/badge/Maintained-yes-brightgreen?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-beta-orange?style=for-the-badge)
![React](https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)
![GitHub Copilot](https://img.shields.io/badge/GitHub%20Copilot-000000?style=for-the-badge&logo=githubcopilot&logoColor=white)

想让社交徽章可以点击，请将图片包在你的个人主页或邀请链接中。个人资料统计、连续贡献、横幅和贡献贪吃蛇请参阅[生成式图形](../BADGE_GUIDE.md#9-generated-graphics-and-profile-tools)。

## GitHub Markdown 提示框

GitHub 支持五种提示框。每一行都要保留 `>`：

```markdown
> [!NOTE]
> Highlights information that users should take into account, even when skimming.

> [!TIP]
> Optional information to help a user be more successful.

> [!IMPORTANT]
> Crucial information necessary for users to succeed.

> [!WARNING]
> Critical content demanding immediate user attention due to potential risks.

> [!CAUTION]
> Negative potential consequences of an action.
```

> [!NOTE]
> 强调用户即使快速浏览也应留意的信息。

> [!TIP]
> 帮助用户取得更好结果的可选建议。

> [!IMPORTANT]
> 用户顺利完成任务所必需的关键信息。

> [!WARNING]
> 因潜在风险而需要用户立即关注的重要内容。

> [!CAUTION]
> 某项操作可能带来的负面后果。

## GitHub 表情代码

`:rocket:` 等短代码会在 GitHub 上显示为表情。下面保留了原有的 GitHub 特有示例；其他 Markdown 平台的支持情况可能不同。

| Emoji | Code |
| :---: | :--- |
| :bowtie: | `:bowtie:` |
| :neckbeard: | `:neckbeard:` |
| :octocat: | `:octocat:` |
| :shipit: | `:shipit:` |
| :trollface: | `:trollface:` |
| :fishsticks: | `:fishsticks:` |
| :suspect: | `:suspect:` |
| :hurtrealbad: | `:hurtrealbad:` |
| :feelsgood: | `:feelsgood:` |
| :goberserk: | `:goberserk:` |
| :finnadie: | `:finnadie:` |
| :rage1: | `:rage1:` |
| :rage2: | `:rage2:` |
| :rage3: | `:rage3:` |
| :rage4: | `:rage4:` |
| :godmode: | `:godmode:` |

一些常用代码：`:rocket:` :rocket:、`:white_check_mark:` :white_check_mark:、`:warning:` :warning:、`:bug:` :bug:、`:sparkles:` :sparkles:、`:books:` :books:、`:lock:` :lock:、`:construction:` :construction:、`:heart:` :heart:、`:tada:` :tada:、`:bulb:` :bulb:、`:memo:` :memo:。

## 推荐做法

- **保持相关。** 优先展示当前版本、支持的运行时或构建状态，而不是装饰性标志。
- **保持诚实。** 静态标签不能验证安全性、覆盖率或维护状态。
- **保持一致。** 每组使用同一种样式，并为每张图片提供描述性替代文本。
- **保持实用。** 将徽章链接到发布页、报告、文档或贡献说明。
- **保持易读。** 检查窄屏、明暗主题以及图片加载失败时的表现。
- **便于维护。** 如果动态元数据能减少手动修改，就优先使用；避免依赖许多互不相关的第三方服务。

## 故障排查

| 问题 | 首先检查 |
| --- | --- |
| 标志缺失 | Simple Icons slug 可能已更改，或品牌图标已被移除 |
| `invalid` / `not found` | 将 URL 与服务商当前徽章生成器进行比较 |
| 构建显示 `no status` | 检查工作流文件名、分支和触发事件 |
| 数字似乎未更新 | 来源、徽章服务商或 GitHub 图片代理可能使用了缓存 |
| 文本或颜色错误 | 检查 `#` → `%23` 以及字面 `-` → `--` 的转义 |

参阅[完整故障排查指南](../BADGE_GUIDE.md#11-troubleshooting)。本地文档检查命令为 `python3 scripts/check_docs.py`；它检查仓库结构，不保证第三方服务的可用性。

## 贡献与翻译

欢迎贡献新徽章、修复标志、改进示例和翻译。请阅读 [CONTRIBUTING.md](../../CONTRIBUTING.md)，遵守[行为准则](../../CODE_OF_CONDUCT.md)，并按照 [SECURITY.md](../../SECURITY.md) 报告漏洞。

英语是基准版本。本 README 已完整翻译为西班牙语、巴西葡萄牙语、俄语、简体中文和日语，可通过上方语言切换栏访问。共享目录和详细指南保持英文；品牌名称、URL 和代码示例在各语言中保持一致。修改共享内容时，请更新全部六个 README 文件。

## 许可证

[MIT](../../LICENSE)。徽章服务、品牌名称和标志归各自所有者所有；收录于此不代表认可或合作。
