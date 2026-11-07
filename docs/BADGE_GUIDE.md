# The Badge Guide: Types, Syntax & Usage

[← Back to README](../README.md) · [Browse the badge catalog](BADGE_CATALOG.md)

A practical guide to the small images that make a README easier to scan. Most examples are plain Markdown or GitHub-compatible HTML; custom-data and workflow sections also use JSON, Python, and YAML. You do not need to install a badge library to use the catalog.

> **Conventions:** replace `OWNER`, `REPO`, `USER`, `PACKAGE`, and filenames with your own values. Examples containing placeholders are **templates**, not working repository URLs. Keep `https://` in image URLs. This guide is the English reference for all README translations.

## Contents

1. [What is a badge?](#1-what-is-a-badge)
2. [Static badges](#2-static-badges)
3. [Styles, colors, and logos](#3-styles-colors-and-logos)
4. [Dynamic badges](#4-dynamic-badges)
5. [GitHub badges](#5-github-badges)
6. [Packages, builds, and quality](#6-packages-builds-and-quality)
7. [Community, documentation, and funding](#7-community-documentation-and-funding)
8. [Custom dynamic and endpoint badges](#8-custom-dynamic-and-endpoint-badges)
9. [Generated graphics and profile tools](#9-generated-graphics-and-profile-tools)
10. [Layout and accessibility](#10-layout-and-accessibility)
11. [Troubleshooting](#11-troubleshooting)
12. [Maintenance and resources](#12-maintenance-and-resources)

---

## 1. What is a badge?

A badge is an image, usually an SVG, showing a short label and a value: **build → passing**, **npm → v10.2.0**, or **license → MIT**. In Markdown, it is simply an image, optionally wrapped in a link:

```markdown
![Alternative text](https://example.com/badge.svg)
[![Alternative text](https://example.com/badge.svg)](https://example.com/details)
```

The alt text describes the image. The outer link decides where a click goes. Neither changes the image itself.

### Two useful ways to classify badges

**By how the value is produced:**

| Type | Source of the value | Examples | Maintenance |
| --- | --- | --- | --- |
| Static | Text written into the URL | Tech stack, project stage, code style | Edit the URL when the fact changes |
| Service-backed dynamic | A provider reads an API or build status | GitHub stars, npm version, CI status | Replace identifiers; the value updates itself |
| Dynamic data | A JSON, YAML, or XML document | Latest version from your own API | Maintain the data source and query |
| Endpoint | Your server returns the badge's display data | Internal release status, custom metric | Maintain a small public JSON endpoint |
| Generated graphic | A service or workflow renders an SVG | Stats cards, contribution snake, banners | Configure the generator and its schedule |

**By what the badge communicates:**

| Purpose | Typical badges | Good destination for the click |
| --- | --- | --- |
| Identity | Project name, technology, platform | Project homepage or relevant documentation |
| Release | Version, tag, release date | Releases page or package registry |
| Health | Build, tests, coverage, uptime | CI run, coverage report, status page |
| Compatibility | Language/runtime versions, OS support | Installation or support policy |
| Legal | License, copyright/reuse status | `LICENSE` or policy file |
| Adoption | Downloads, stars, forks, contributors | Registry or repository insights |
| Community | Chat, discussions, contributing | Chat invite or `CONTRIBUTING.md` |
| Funding | Sponsors, donations, funding links | Sponsorship or funding page |
| Profile | Languages, activity, achievements | Your GitHub profile or source project |

These classifications overlap: an npm version badge is both **service-backed dynamic** and a **release** badge. A static “Security: audited” label is not evidence of an audit; link the actual report or use a verifiable service instead.

## 2. Static badges

[Shields.io](https://shields.io/badges/static-badge) can render a badge without contacting your repository:

```text
https://img.shields.io/badge/LABEL-MESSAGE-COLOR
https://img.shields.io/badge/MESSAGE-COLOR
```

For example:

```markdown
![Python](https://img.shields.io/badge/Python-3.12-3776AB?style=flat-square&logo=python&logoColor=white)
![Project status](https://img.shields.io/badge/status-beta-orange)
```

![Python](https://img.shields.io/badge/Python-3.12-3776AB?style=flat-square&logo=python&logoColor=white)
![Project status](https://img.shields.io/badge/status-beta-orange)

### Escaping rules

The path uses `-` to separate fields and `_` to represent spaces. Escape literal characters in this order:

| Desired character | Write in the path | Example |
| --- | --- | --- |
| Space | `_` or `%20` | `Made_with-Markdown-blue` |
| Literal hyphen | `--` | `long--term-support-blue` |
| Literal underscore | `__` | `my__tool-v1-blue` |
| `#` in a color | `%23` | `%233776AB` |
| `+` | `%2B` | `C%2B%2B` |
| `/` | `%2F` | `shadcn%2Fui` |
| `?` | `%3F` | `ready%3F-yes-blue` |

Do not confuse a separator with text: `long-term-support-blue` has extra fields, while `long--term--support-blue` displays “long-term-support.” URL encoding is still needed for reserved URL characters.

**Quick recommendation:** use the [catalog](BADGE_CATALOG.md) for technology labels, then change only the fields you need. A static Python 3.12 badge will not detect that you upgraded to Python 3.13.

## 3. Styles, colors, and logos

### Styles

Append `?style=STYLE`, or `&style=STYLE` if the URL already has query parameters.

| Style | Preview | Suggested use |
| --- | --- | --- |
| `plastic` | ![Plastic](https://img.shields.io/badge/style-plastic-blue?style=plastic) | Glossy, retro look |
| `flat` | ![Flat](https://img.shields.io/badge/style-flat-blue?style=flat) | Default; compact project metadata |
| `flat-square` | ![Flat square](https://img.shields.io/badge/style-flat--square-blue?style=flat-square) | Minimal, square corners |
| `social` | ![Social](https://img.shields.io/badge/style-social-blue?style=social&logo=github) | Repository and community counters |
| `for-the-badge` | ![For the badge](https://img.shields.io/badge/style-for--the--badge-blue?style=for-the-badge) | Large technology and portfolio labels |

Pick one style for each visual group. The catalog uses `for-the-badge`; mixing it with tiny status badges in the same row often looks uneven.

### Common query parameters

| Parameter | Purpose | Example |
| --- | --- | --- |
| `style` | Badge appearance | `style=flat-square` |
| `logo` | Simple Icons slug or an SVG data URI | `logo=python` |
| `logoColor` | Named logo color | `logoColor=white` |
| `label` | Override the left-side label | `label=release` |
| `labelColor` | Left-side background | `labelColor=24292f` |
| `color` | Override the right-side background | `color=success` |
| `cacheSeconds` | Request a cache lifetime, subject to service limits | `cacheSeconds=3600` |

Parameters apply to the **image URL**, not to the destination link around it. Not every option behaves identically in every style; the `social` style has its own layout rules.

### Colors

Use a hex value without `#` (`3776AB`), an encoded `#` (`%233776AB`), a supported CSS color name (`orange`), or a semantic Shields alias:

| Alias | Typical meaning |
| --- | --- |
| `brightgreen` / `success` | Passing, available, maintained |
| `yellow` / `yellowgreen` | Caution or intermediate state |
| `orange` / `important` | Beta, attention needed |
| `red` / `critical` | Failing or unsupported |
| `blue` / `informational` | Neutral information |
| `lightgrey` / `inactive` | Unknown, archived, inactive |

Always communicate the state in words too. Color alone is not an accessible status indicator.

### Named logos and removed brands

Shields uses [Simple Icons](https://simpleicons.org/) for named logos. Use the current **slug**, not a guess based on the product name: `nodedotjs`, `nextdotjs`, `css`, and `googlegemini` are examples of slugs that are easy to get wrong.

Simple Icons periodically renames or removes brands. A removed logo does **not** mean the technology disappeared. You have three safe options:

1. Use the brand's current slug if it was renamed.
2. Remove `logo` and `logoColor` and keep a readable text badge.
3. Supply a logo you have permission to use as an SVG data URI.

This catalog uses options 1 and 2. It does not substitute an unrelated logo just to fill the space.

For an original logo, the general format is:

```text
logo=data:image/svg+xml;base64,BASE64_ENCODED_SVG
```

Generate it locally rather than hand-encoding it:

```python
from base64 import b64encode
from pathlib import Path
from urllib.parse import quote

svg = Path("my-logo.svg").read_bytes()
print("data:image/svg+xml;base64," + b64encode(svg).decode("ascii"))
```

Use a small, trusted SVG without scripts or external resources. Check the destination's URL-length limits. Brand availability and trademark permission are separate questions.

## 4. Dynamic badges

A dynamic badge fetches a live value. Its URL contains **identifiers**, not the displayed number:

```markdown
[![GitHub stars](https://img.shields.io/github/stars/OWNER/REPO?style=social)](https://github.com/OWNER/REPO/stargazers)
```

Choose a service in the [Shields badge directory](https://shields.io/badges), fill in your identifiers, and copy the Markdown. Prefer an official provider badge when the provider offers a copy-ready snippet.

**Before adding one, check:**

- Is the repository/package public, or does the badge service require authorization?
- Does the identifier refer to the correct owner, branch, package, or workflow?
- Does the value mean what the label says? “Downloads last month” is not “active users.”
- Is a temporary provider outage acceptable in your README?
- Does the linked page explain the metric?

Values are cached by the badge provider and may also be cached by GitHub's image proxy. A delay does not necessarily mean your URL is wrong. Never put an access token in a public README URL to work around privacy or rate limits.

## 5. GitHub badges

Replace `OWNER/REPO` in these templates. Add `?style=flat-square` or another style consistently. For an existing query string, append `&style=...` instead.

| What it shows | Badge URL template |
| --- | --- |
| Latest release | `https://img.shields.io/github/v/release/OWNER/REPO` |
| Latest tag | `https://img.shields.io/github/v/tag/OWNER/REPO` |
| Release date | `https://img.shields.io/github/release-date/OWNER/REPO` |
| License detected by GitHub | `https://img.shields.io/github/license/OWNER/REPO` |
| Stars | `https://img.shields.io/github/stars/OWNER/REPO` |
| Forks | `https://img.shields.io/github/forks/OWNER/REPO` |
| Watchers | `https://img.shields.io/github/watchers/OWNER/REPO` |
| Open issues | `https://img.shields.io/github/issues/OWNER/REPO` |
| Open pull requests | `https://img.shields.io/github/issues-pr/OWNER/REPO` |
| Closed pull requests | `https://img.shields.io/github/issues-pr-closed/OWNER/REPO` |
| Contributors | `https://img.shields.io/github/contributors/OWNER/REPO` |
| Last commit | `https://img.shields.io/github/last-commit/OWNER/REPO` |
| Commits per month | `https://img.shields.io/github/commit-activity/m/OWNER/REPO` |
| Repository size | `https://img.shields.io/github/repo-size/OWNER/REPO` |
| Code size | `https://img.shields.io/github/languages/code-size/OWNER/REPO` |
| Top language by bytes | `https://img.shields.io/github/languages/top/OWNER/REPO` |
| Number of detected languages | `https://img.shields.io/github/languages/count/OWNER/REPO` |
| Discussions count | `https://img.shields.io/github/discussions/OWNER/REPO` |
| User followers | `https://img.shields.io/github/followers/USER?style=social` |
| User sponsors | `https://img.shields.io/github/sponsors/USER` |

GitHub's issue API can include pull requests in issue counts; do not treat an issue badge as a precise “bugs only” metric. “Top language” is based on detected code size, not quality or effort.

### A repository header

```markdown
[![Release](https://img.shields.io/github/v/release/OWNER/REPO)](https://github.com/OWNER/REPO/releases)
[![License](https://img.shields.io/github/license/OWNER/REPO)](LICENSE)
[![CI](https://img.shields.io/github/actions/workflow/status/OWNER/REPO/ci.yml?branch=main)](https://github.com/OWNER/REPO/actions/workflows/ci.yml)
[![Contributors](https://img.shields.io/github/contributors/OWNER/REPO)](https://github.com/OWNER/REPO/graphs/contributors)
```

The workflow filename is the actual file under `.github/workflows/`, such as `ci.yml`; a workflow's display name is not always its filename. `branch=main` should match the branch you intend to describe. Use `event=push` or another trigger when you need to disambiguate runs.

## 6. Packages, builds, and quality

### Package registries

| Ecosystem | Version template | Other useful routes |
| --- | --- | --- |
| npm | `https://img.shields.io/npm/v/PACKAGE` | `npm/dw/PACKAGE`, `npm/dm/PACKAGE`, `npm/dy/PACKAGE`, `npm/l/PACKAGE` |
| PyPI | `https://img.shields.io/pypi/v/PACKAGE` | `pypi/pyversions/PACKAGE`, `pypi/status/PACKAGE`, `pypi/l/PACKAGE` |
| Crates.io | `https://img.shields.io/crates/v/CRATE` | `crates/d/CRATE`, `crates/l/CRATE` |
| NuGet | `https://img.shields.io/nuget/v/PACKAGE` | `nuget/dt/PACKAGE` |
| Packagist | `https://img.shields.io/packagist/v/VENDOR/PACKAGE` | `packagist/dt/VENDOR/PACKAGE` |
| RubyGems | `https://img.shields.io/gem/v/GEM` | `gem/dt/GEM` |
| Maven Central | `https://img.shields.io/maven-central/v/GROUP_ID/ARTIFACT_ID` | See the service's options for metadata |
| Pub | `https://img.shields.io/pub/v/PACKAGE` | `pub/points/PACKAGE`, `pub/likes/PACKAGE` |
| Docker Hub | `https://img.shields.io/docker/v/USER/IMAGE` | `docker/pulls/USER/IMAGE`, `docker/image-size/USER/IMAGE` |

The routes in the last column use the same `https://img.shields.io/` prefix. npm `dw`, `dm`, and `dy` mean weekly, monthly, and yearly downloads. Scoped npm packages and registry-specific identifiers may need URL encoding; use the provider's badge builder rather than guessing.

```markdown
[![npm version](https://img.shields.io/npm/v/PACKAGE)](https://www.npmjs.com/package/PACKAGE)
[![PyPI version](https://img.shields.io/pypi/v/PACKAGE)](https://pypi.org/project/PACKAGE/)
```

### Build and CI status

**GitHub Actions, directly from GitHub:**

```markdown
[![CI](https://github.com/OWNER/REPO/actions/workflows/ci.yml/badge.svg?branch=main)](https://github.com/OWNER/REPO/actions/workflows/ci.yml)
```

**GitHub Actions, through Shields:**

```markdown
![CI](https://img.shields.io/github/actions/workflow/status/OWNER/REPO/ci.yml?branch=main)
```

Other services supported by Shields include CircleCI, Travis CI, AppVeyor, GitLab, Azure DevOps, and Jenkins. Their URLs can require a branch, project ID, job name, or public pipeline. Copy the exact snippet from the relevant service rather than adapting a GitHub URL.

A passing build badge describes the selected workflow/run, not every test or deployment in its entirety.

### Coverage and quality

| Service | Template or source |
| --- | --- |
| Codecov | `https://codecov.io/gh/OWNER/REPO/branch/main/graph/badge.svg` |
| Coveralls | `https://coveralls.io/repos/github/OWNER/REPO/badge.svg?branch=main` |
| CodeFactor | `https://www.codefactor.io/repository/github/OWNER/REPO/badge` |
| Code Climate | Copy the repository-specific badge from Code Climate; it contains a project identifier |
| SonarQube | Copy the project badge from the SonarQube dashboard; the project key and metric matter |
| Snyk | `https://snyk.io/test/github/OWNER/REPO/badge.svg` |

Connect the repository and upload reports where required **before** adding these badges. Coverage is not correctness, and a vulnerability scanner's “no known issues” result is not a guarantee of security.

## 7. Community, documentation, and funding

Static contact badges are clickable links; dynamic community badges show live counts.

```markdown
[![Discussions](https://img.shields.io/badge/ask-discussions-181717?logo=github)](https://github.com/OWNER/REPO/discussions)
[![Contributing](https://img.shields.io/badge/PRs-welcome-brightgreen)](CONTRIBUTING.md)
[![Documentation](https://img.shields.io/readthedocs/PACKAGE)](https://PACKAGE.readthedocs.io/)
```

| Need | Template | Important detail |
| --- | --- | --- |
| Discord online count | `https://img.shields.io/discord/SERVER_ID` | Enable the server widget; use the server ID, not an invite code |
| Documentation build | `https://img.shields.io/readthedocs/PROJECT` | Use the Read the Docs project slug |
| Website availability | `https://img.shields.io/website?url=https%3A%2F%2Fexample.com` | This is a simple check, not an SLA or uptime history |
| GitHub Sponsors | `https://img.shields.io/github/sponsors/USER` | Link to the actual sponsorship page |
| Stack Exchange reputation | Use the Stack Exchange badge builder | Site and numeric user ID are both required |

For social/contact links, wrap a static badge in your real destination:

```markdown
[![Email](https://img.shields.io/badge/email-contact-blue)](mailto:you@example.com)
[![Mastodon](https://img.shields.io/badge/Mastodon-follow-6364FF?logo=mastodon&logoColor=white)](https://INSTANCE/@USER)
[![Sponsor](https://img.shields.io/badge/sponsor-project-ea4aaa?logo=githubsponsors&logoColor=white)](https://github.com/sponsors/USER)
```

Only advertise contact details and funding accounts you intend to make public. A badge is not a substitute for a thoughtfully scoped `FUNDING.yml` or a support policy.

## 8. Custom dynamic and endpoint badges

### Read a value from JSON

Suppose `https://example.com/status.json` returns:

```json
{ "version": "2.1.0", "healthy": true }
```

Use Shields' dynamic JSON route:

```text
https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fexample.com%2Fstatus.json&query=%24.version&label=version&color=blue
```

- `url`: URL-encoded address of the public data.
- `query=%24.version`: JSONPath `$.version`.
- `label`: the left-side text.
- `prefix` / `suffix`: optional text around the value.

Shields also supports dynamic YAML and XML. Keep the data small, public, stable, and served over HTTPS. Dynamic badges are not a monitoring system or a way to expose internal APIs.

### Return the whole badge definition

Create a public JSON file such as `https://example.com/badge.json`:

```json
{
  "schemaVersion": 1,
  "label": "release",
  "message": "2.1.0",
  "color": "blue",
  "namedLogo": "github",
  "logoColor": "white",
  "cacheSeconds": 3600
}
```

Then reference it:

```text
https://img.shields.io/endpoint?url=https%3A%2F%2Fexample.com%2Fbadge.json
```

`schemaVersion`, `label`, and `message` are required; `label` may be an empty string and `message` must be a string. Optional fields include `color`, `labelColor`, `isError`, `namedLogo`, `logoSvg`, `logoColor`, `style`, and `cacheSeconds`. Do not supply `namedLogo` and `logoSvg` together.

Your endpoint controls the displayed text, so generate it from trusted data. Do not accept arbitrary user input without validation. See the [official endpoint schema](https://github.com/badges/shields/blob/master/services/endpoint-common.js).

### Self-hosting

For private infrastructure or custom services, consider [self-hosting Shields](https://github.com/badges/shields/blob/master/doc/self-hosting.md). A public endpoint badge still needs to be reachable by the badge server. Self-hosting is a deployment project: configure credentials server-side, restrict network access, and disable dynamic/endpoint routes if untrusted users could make the server fetch internal resources.

## 9. Generated graphics and profile tools

These are often called “badges,” but many are **cards, banners, or animations**. They usually belong in a profile README (`USER/USER`), not at the top of a library's installation instructions.

| Project | What it generates | Example image URL or setup |
| --- | --- | --- |
| [GitHub README Stats](https://github.com/anuraghazra/github-readme-stats) | Contribution/stat card | `https://github-readme-stats.vercel.app/api?username=USER&show_icons=true&theme=transparent` |
| [Top Languages](https://github.com/anuraghazra/github-readme-stats) | Language card | `https://github-readme-stats.vercel.app/api/top-langs/?username=USER&layout=compact` |
| [GitHub Readme Streak Stats](https://github.com/DenverCoder1/github-readme-streak-stats) | Contribution streak card | `https://streak-stats.demolab.com?user=USER&theme=transparent` |
| [GitHub Profile Trophy](https://github.com/ryo-ma/github-profile-trophy) | Achievement graphic | `https://github-profile-trophy.vercel.app/?username=USER` |
| [GitHub README Activity Graph](https://github.com/Ashutosh00710/github-readme-activity-graph) | Activity graph | `https://github-readme-activity-graph.vercel.app/graph?username=USER` |
| [Readme Typing SVG](https://github.com/DenverCoder1/readme-typing-svg) | Animated typing line | `https://readme-typing-svg.demolab.com?font=Fira+Code&size=24&pause=1000&lines=Build%20small.;Ship%20often.` |
| [Capsule Render](https://github.com/kyechan99/capsule-render) | Header/footer banner | `https://capsule-render.vercel.app/api?type=waving&color=gradient&height=160&section=header&text=Project%20Name` |
| [GitHub Profile Views Counter](https://github.com/antonkomarev/github-profile-views-counter) | Profile view counter | `https://komarev.com/ghpvc/?username=USER&style=flat-square` |
| [Snk](https://github.com/Platane/snk) | Contribution-grid snake animation | Generate SVGs with a GitHub Action, then link the files |
| [Metrics](https://github.com/lowlighter/metrics) | Configurable profile/project infographics | Generate an image with the workflow and commit the output |

Public demo instances are community services, not GitHub APIs. They can rate-limit, change URLs, or go offline. For reliability, follow the project's self-hosting instructions or generate images on a schedule. A views counter counts requests observed since setup; it is not GitHub's historical profile analytics. Language cards measure repository bytes and can exclude repositories or languages through configuration.

### Example: generate a contribution snake

Save this as `.github/workflows/snake.yml` **in your profile repository**, review the action versions, and pin third-party actions to audited commit SHAs according to your security policy:

```yaml
name: Generate contribution snake
on:
  schedule:
    - cron: "0 3 * * *"
  workflow_dispatch:
permissions:
  contents: write
jobs:
  generate:
    runs-on: ubuntu-latest
    steps:
      - uses: Platane/snk/svg-only@v3
        with:
          github_user_name: ${{ github.repository_owner }}
          outputs: |
            dist/github-snake.svg
            dist/github-snake-dark.svg?palette=github-dark
      - uses: crazy-max/ghaction-github-pages@v4
        with:
          target_branch: output
          build_dir: dist
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
```

After the workflow has published the `output` branch:

```markdown
![Contribution snake](https://raw.githubusercontent.com/USER/USER/output/github-snake.svg)
```

The URL alone does not run the workflow. The same principle applies to Metrics and other generated images: **generation, storage, and display are separate steps**.

## 10. Layout and accessibility

### Recommended repository order

1. Project name and one-sentence explanation.
2. A small, relevant badge row: release, build, license, package/docs.
3. Installation and a minimal working example.
4. Configuration, deeper documentation, and limitations.
5. Contributing, security, funding, and license details.

For a personal profile, put your introduction and links before optional stats cards. There is no required badge count; remove anything that does not help a reader decide what to do next.

### Make every badge readable and useful

- Write alt text such as `Build status on main`, not `badge1` or an empty string.
- For a linked badge, let the alt text describe the badge; the surrounding prose should explain the destination when it is not obvious.
- Keep text in the image, not color-only signaling.
- Use a consistent style and a short row rather than a wall of unrelated logos.
- Link to a useful page, and prefer relative links for files in your repository.
- Avoid animated banners when motion adds no information; consider readers sensitive to motion.
- Check the README on a narrow screen and in both GitHub themes.

### Centering and HTML links

GitHub permits a useful subset of HTML. This keeps a group together:

```html
<p align="center">
  <a href="https://github.com/OWNER/REPO/releases">
    <img alt="Latest release" src="https://img.shields.io/github/v/release/OWNER/REPO">
  </a>
  <a href="LICENSE">
    <img alt="Repository license" src="https://img.shields.io/github/license/OWNER/REPO">
  </a>
</p>
```

In HTML attributes, write query separators as `&amp;` (for example, `?style=flat&amp;logo=python`). In ordinary Markdown URLs, `&` is fine.

### Light and dark themes

A transparent badge with a fixed dark logo can disappear in dark mode. Choose contrasting colors, or supply two versions. GitHub supports theme-specific image fragments:

```markdown
![Stats in light mode](https://github-readme-stats.vercel.app/api?username=USER&theme=default#gh-light-mode-only)
![Stats in dark mode](https://github-readme-stats.vercel.app/api?username=USER&theme=dark#gh-dark-mode-only)
```

For locally generated images, the `<picture>` element with `prefers-color-scheme` sources is another option. These are rendering hints; other Markdown platforms may not implement GitHub's fragments.

## 11. Troubleshooting

| Symptom | Likely cause | What to try |
| --- | --- | --- |
| `invalid` or `badge not found` | Wrong route or missing path field | Compare with the provider's current badge builder |
| `repo not found` / `not found` | Typo, private resource, wrong owner | Check the exact public repository/package identifier |
| `no status` on a build badge | Wrong workflow filename, branch, or trigger | Open the workflow and copy its native badge snippet |
| `inaccessible` or provider error | API outage, permissions, or rate limit | Check the source service; do not embed a secret token |
| Logo is missing | Removed or renamed Simple Icons slug | Search the current slug; use a text-only fallback |
| Wrong color or truncated text | Unescaped `#`, `-`, `_`, or reserved character | Apply the escaping table above |
| Value looks stale | Provider/GitHub image caching | Check the source, wait for cache expiry, compare with `cacheSeconds` |
| Badge works locally but not on GitHub | Relative image path or blocked content | Use a public HTTPS image URL or a correct repository-relative path |
| Click does nothing | Image is not wrapped in a link | Use `[![alt](image-url)](destination-url)` |
| Discord badge fails | Widget disabled or invite code used as ID | Enable the widget and use the numeric server ID |
| Stats card is empty | New account, private activity, configuration, or rate limit | Check the generator's documentation and exclusions |
| Huge image breaks the layout | Banner/card rather than a compact badge | Constrain with HTML width or move it below the introduction |

Debug in this order: **open the source page → open the image URL directly → check identifiers → check encoding → check caching**. GitHub's image proxy can make a recently fixed badge appear stale for a while.

## 12. Maintenance and resources

When maintaining this repository:

1. Add a badge to the most specific existing catalog category.
2. Use descriptive alt text and a current logo slug, or intentionally omit the logo.
3. Keep static labels distinct from live metrics.
4. Update the English README first, then its five translations; keep image URLs and code examples synchronized.
5. Run `python3 scripts/check_docs.py` from the repository root.
6. Check new external services in a browser before publishing. The local checker validates structure; it cannot guarantee a third party's uptime.

### Primary references

- [Shields.io badge directory](https://shields.io/badges) — current routes, parameters, and examples.
- [Shields source and self-hosting documentation](https://github.com/badges/shields) — implementation and deployment details.
- [Simple Icons](https://simpleicons.org/) — current brand slugs and colors.
- [GitHub Docs: basic writing and formatting](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax) — Markdown, images, and theme handling.
- [GitHub Docs: alerts](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax#alerts) — the `NOTE`, `TIP`, `IMPORTANT`, `WARNING`, and `CAUTION` syntax.
- [Shields.io](https://shields.io/), [Badgen](https://badgen.net/), and [dwyl/repo-badges](https://github.com/dwyl/repo-badges) — additional badge services and examples.

---

[Back to README](../README.md) · [Badge catalog](BADGE_CATALOG.md) · [Contribution guide](../CONTRIBUTING.md)
