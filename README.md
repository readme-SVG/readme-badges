# README Badges

**A copy-paste badge collection and a practical guide to making GitHub READMEs clearer.**

[![License](https://img.shields.io/github/license/readme-SVG/readme-badges?style=flat-square)](LICENSE)
[![GitHub stars](https://img.shields.io/github/stars/readme-SVG/readme-badges?style=flat-square)](https://github.com/readme-SVG/readme-badges/stargazers)
[![Last commit](https://img.shields.io/github/last-commit/readme-SVG/readme-badges?style=flat-square)](https://github.com/readme-SVG/readme-badges/commits/main)
[![PRs welcome](https://img.shields.io/badge/PRs-welcome-brightgreen?style=flat-square)](CONTRIBUTING.md)

**English** · [Español](docs/i18n/README.es.md) · [Português (Brasil)](docs/i18n/README.pt-BR.md) · [Русский](docs/i18n/README.ru.md) · [简体中文](docs/i18n/README.zh-CN.md) · [日本語](docs/i18n/README.ja.md)

Browse **699 static badge examples in 23 categories**, learn the difference between static and live badges, and copy working templates for releases, builds, package versions, documentation, and community links. No installation or badge-building app is required.

| Resource | What you will find |
| --- | --- |
| [**Badge catalog →**](docs/BADGE_CATALOG.md) | The complete collection: languages, frameworks, cloud, AI, testing, security, games, hardware, social links, and more |
| [**Badge guide →**](docs/BADGE_GUIDE.md) | Badge types, URL syntax, styles, logos, dynamic data, custom endpoints, profile graphics, and troubleshooting |
| [**Contributing →**](CONTRIBUTING.md) | Add a badge, fix a logo, improve an example, or update a translation |

> [!TIP]
> Start with one useful row of badges, not a wall of logos. A release, build status, license, and documentation link usually tell a visitor more than twenty technology labels.

## Contents

- [Quick start](#quick-start)
- [Badge types](#badge-types)
- [Styles](#styles)
- [Live badge templates](#live-badge-templates)
- [Browse the catalog](#browse-the-catalog)
- [A few ready-made badges](#a-few-ready-made-badges)
- [GitHub Markdown alerts](#github-markdown-alerts)
- [GitHub emoji codes](#github-emoji-codes)
- [Good defaults](#good-defaults)
- [Troubleshooting](#troubleshooting)
- [Contributing and translations](#contributing-and-translations)
- [License](#license)

## Quick start

A badge is a Markdown image. Wrap it in a link to make it clickable:

```markdown
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)

[![Documentation](https://img.shields.io/badge/docs-read-blue)](https://example.com/docs)
```

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)

1. Open the [catalog](docs/BADGE_CATALOG.md), find a badge, and use GitHub's **Raw** view to copy its Markdown.
2. Paste it into your README. For a profile README, the repository is usually `YOUR-USERNAME/YOUR-USERNAME`.
3. Change the label, color, logo, or destination link. For a live badge, replace `OWNER`, `REPO`, and other placeholders as explained in the [guide](docs/BADGE_GUIDE.md#4-dynamic-badges).

The basic Shields URL is `https://img.shields.io/badge/LABEL-MESSAGE-COLOR`. Encode `#` as `%23`, escape a literal hyphen as `--`, and use `_` or `%20` for spaces. See the [full escaping table](docs/BADGE_GUIDE.md#escaping-rules).

## Badge types

“Badge type” can describe how the image gets its value **or** what the value means. These are the main implementation types:

| Type | Example | Does it update automatically? |
| --- | --- | --- |
| **Static** | `Python`, `status: beta`, `PRs welcome` | No — edit the Markdown |
| **Service-backed dynamic** | GitHub stars, npm version, CI status | Yes — the provider reads a source service |
| **Dynamic data** | A version read from your JSON API | Yes — the provider reads your data |
| **Endpoint** | Your server supplies label, message, and color | Yes — you maintain the JSON endpoint |
| **Generated graphic** | Stats card, banner, contribution snake | Depends on the generator or workflow schedule |

Common purposes include releases, build health, coverage, compatibility, licenses, downloads, community, funding, and profile statistics. The [taxonomy and recipes](docs/BADGE_GUIDE.md#1-what-is-a-badge) explain when to use each one.

> [!IMPORTANT]
> A static badge is a label, not verification. “Secure” or “100% tested” does not become true because it is green. Prefer a live, linked result when the claim needs evidence.

## Styles

Use the same style within a visual group. Append `?style=STYLE` to a Shields URL:

| Style | Preview |
| --- | --- |
| `plastic` | ![Plastic](https://img.shields.io/badge/style-plastic-blue?style=plastic) |
| `flat` | ![Flat](https://img.shields.io/badge/style-flat-blue?style=flat) |
| `flat-square` | ![Flat square](https://img.shields.io/badge/style-flat--square-blue?style=flat-square) |
| `social` | ![Social](https://img.shields.io/badge/style-social-blue?style=social&logo=github) |
| `for-the-badge` | ![For the badge](https://img.shields.io/badge/style-for--the--badge-blue?style=for-the-badge) |

The catalog uses `for-the-badge`. The [guide](docs/BADGE_GUIDE.md#3-styles-colors-and-logos) also covers colors, logo slugs, removed brand icons, and light/dark themes.

## Live badge templates

Replace `OWNER/REPO` with your repository. These examples update from GitHub; the numbers are not hard-coded.

```markdown
[![Release](https://img.shields.io/github/v/release/OWNER/REPO)](https://github.com/OWNER/REPO/releases)
[![License](https://img.shields.io/github/license/OWNER/REPO)](LICENSE)
[![CI](https://img.shields.io/github/actions/workflow/status/OWNER/REPO/ci.yml?branch=main)](https://github.com/OWNER/REPO/actions/workflows/ci.yml)
[![Open issues](https://img.shields.io/github/issues/OWNER/REPO)](https://github.com/OWNER/REPO/issues)
```

Use the actual workflow filename in place of `ci.yml`. For package versions, try `https://img.shields.io/npm/v/PACKAGE` or `https://img.shields.io/pypi/v/PACKAGE`. The guide has [GitHub templates](docs/BADGE_GUIDE.md#5-github-badges), [registry and quality badges](docs/BADGE_GUIDE.md#6-packages-builds-and-quality), and [custom JSON endpoints](docs/BADGE_GUIDE.md#8-custom-dynamic-and-endpoint-badges).

## Browse the catalog

All **699 entries** live in [**docs/BADGE_CATALOG.md**](docs/BADGE_CATALOG.md), with a clickable table of contents. The original collection is preserved and expanded with **224 new examples**.

| Area | Categories include |
| --- | --- |
| Languages and apps | Programming languages, frontend, backend, cross-platform apps |
| Infrastructure | Databases, cloud/DevOps, search/vector databases, observability |
| Modern development | AI assistants/agents, testing/code quality, security/identity |
| Specialized stacks | Game development, IoT/embedded hardware, blockchain/Web3 |
| Products and people | Tools/editors, browsers/OS, data science, CMS/no-code, office/business, socials/contact |
| Project communication | Project status/community, documentation/publishing, accessibility/localization |

These are static labels. Some logos were removed from Simple Icons, so their badges intentionally use readable text instead of a broken or unrelated icon. See [logo fallbacks](docs/BADGE_GUIDE.md#named-logos-and-removed-brands).

## A few ready-made badges

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

For clickable social badges, wrap the image in your own profile or invite URL. For profile stats, streaks, banners, and contribution snakes, see [generated graphics](docs/BADGE_GUIDE.md#9-generated-graphics-and-profile-tools).

## GitHub Markdown alerts

GitHub supports five alert types. Keep the `>` on every line:

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
> Highlights information that users should take into account, even when skimming.

> [!TIP]
> Optional information to help a user be more successful.

> [!IMPORTANT]
> Crucial information necessary for users to succeed.

> [!WARNING]
> Critical content demanding immediate user attention due to potential risks.

> [!CAUTION]
> Negative potential consequences of an action.

## GitHub emoji codes

Shortcodes such as `:rocket:` render as emoji on GitHub. The original GitHub-specific examples are preserved below; availability can differ on other Markdown platforms.

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

A few useful everyday codes: `:rocket:` :rocket:, `:white_check_mark:` :white_check_mark:, `:warning:` :warning:, `:bug:` :bug:, `:sparkles:` :sparkles:, `:books:` :books:, `:lock:` :lock:, `:construction:` :construction:, `:heart:` :heart:, `:tada:` :tada:, `:bulb:` :bulb:, and `:memo:` :memo:.

## Good defaults

- **Be relevant.** Show the current release, supported runtime, or build status before decorative logos.
- **Be honest.** Static labels do not verify security, coverage, or maintenance.
- **Be consistent.** Use one style per group and descriptive alt text for every image.
- **Be useful.** Link badges to releases, reports, docs, or contribution instructions.
- **Be readable.** Check narrow screens, light/dark themes, and image-loading failures.
- **Be maintainable.** Prefer live metadata where it saves manual edits; avoid relying on many unrelated third-party services.

## Troubleshooting

| Problem | First thing to check |
| --- | --- |
| Logo is missing | The Simple Icons slug may have changed or the brand icon may have been removed |
| `invalid` / `not found` | Compare the URL with the provider's current badge builder |
| Build says `no status` | Check the workflow filename, branch, and trigger event |
| Number looks stale | The source, badge provider, or GitHub image proxy may be caching it |
| Text or color is wrong | Check `#` → `%23` and literal `-` → `--` escaping |

See the [full troubleshooting guide](docs/BADGE_GUIDE.md#11-troubleshooting). The local documentation checker is `python3 scripts/check_docs.py`; it checks repository structure, not third-party uptime.

## Contributing and translations

Contributions are welcome: new badges, corrected logos, clearer examples, and translations all help. Read [CONTRIBUTING.md](CONTRIBUTING.md), follow the [Code of Conduct](CODE_OF_CONDUCT.md), and report vulnerabilities according to [SECURITY.md](SECURITY.md).

English is the source of truth. The README is fully translated into Spanish, Brazilian Portuguese, Russian, Simplified Chinese, and Japanese using the language switcher above. The shared catalog and detailed guide remain in English; brand names, URLs, and code examples stay consistent across languages. Update all six README files when changing shared content.

## License

[MIT](LICENSE). Badge services, brand names, and logos belong to their respective owners; their inclusion here does not imply endorsement.
