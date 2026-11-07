[![CONTRIBUTING](https://raw.githubusercontent.com/OstinUA/Promt-AI-Helper/main/Additional%20files/Image/CONTRIBUTING.svg)](https://github.com/OstinUA)

[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-3e80ed?style=for-the-badge&logo=github&logoColor=white)](https://github.com/OstinUA)
[![Open Source](https://img.shields.io/badge/Open_Source-Yes-brightgreen?style=for-the-badge&logo=opensourceinitiative&logoColor=white)](https://github.com/OstinUA)
[![](https://capsule-render.vercel.app/api?type=rect&color=3e80ed&height=2&)](https://github.com/OstinUA)

Hello! Thank you for your interest in contributing to this project. I am always open to any help, whether it's fixing bugs, adding new features, improving documentation, or just sharing fresh ideas. 

This document is not a strict set of rules, but a simple guide on how we can comfortably and productively work together. I am very friendly and will be incredibly glad for absolutely any help!

## ⬢ How You Can Help

- **Have a cool idea?** You can create an Issue to discuss it first, or just jump straight in and open a Pull Request! Do whatever is more comfortable for you. We can always figure out the details together to make the project better.
- **Found a bug?** Open an Issue and briefly describe what went wrong, or just fix it right away and send a PR.
- **Ready to write code?** Feel free to fork the repository and open a Pull Request immediately. I will review it, help out if needed, and take care of the rest.
- **Improving documentation.** Fixing typos, expanding instructions, or translating — absolutely any help is highly valuable.

## ⬢ Pull Request Process

The workflow here is as straightforward as possible:

1. Fork this repository.
2. Create a new branch for your changes (`git checkout -b feature/my-awesome-idea` or `git checkout -b bugfix/issue-123`).
3. Make your changes and commit them (`git commit -m "Add new awesome feature"`).
4. Push the changes to your fork (`git push origin feature/my-awesome-idea`).
5. Open a Pull Request to this repository.

## ⬢ A Few Simple Requests

- Try to stick to the code style already used in the project.
- Make your commit messages clear so it's easy to understand what changed.
- If your Pull Request resolves a specific Issue, mention its number in the description (e.g., `Closes #42`).
- If shared documentation changes, update the English README and the relevant translations, then run the documentation checker described below.

## ⬢ Badges, Documentation & Translations

The documentation is organized so the large catalog does not have to be duplicated in every language:

```text
README.md                    # English entry point (source of truth)
docs/BADGE_CATALOG.md         # Complete static badge collection
docs/BADGE_GUIDE.md           # Types, syntax, live badges, and troubleshooting
docs/i18n/README.es.md        # Spanish
docs/i18n/README.pt-BR.md     # Portuguese (Brazil)
docs/i18n/README.ru.md        # Russian
docs/i18n/README.zh-CN.md     # Chinese (Simplified)
docs/i18n/README.ja.md        # Japanese
scripts/check_docs.py        # Offline documentation checks
```

**Adding or fixing a badge**

1. Choose the most specific category in `docs/BADGE_CATALOG.md` and follow its Markdown format.
2. Use descriptive alt text, `style=for-the-badge`, and a current [Simple Icons](https://simpleicons.org/) slug. If the brand icon was removed, omit `logo` and `logoColor`; do not substitute an unrelated product's icon.
3. Keep static labels separate from live metrics. For a new dynamic recipe, add a template and explain its identifiers in the guide.
4. Update the catalog's entry count and the README count/category references in all six languages when the totals change. The checker reports stale totals.
5. Preserve the original badge when fixing its URL unless it is an exact duplicate being intentionally removed.

**Updating translations**

Translate the prose, headings, table labels, and rendered alert explanations. Keep image URLs, fenced code examples, brand names, and placeholder identifiers (`OWNER`, `REPO`, `PACKAGE`) identical to the English README so examples remain copyable in every language. Keep the language switcher and relative links working from `docs/i18n/`. The shared catalog and guide are intentionally English-only references.

**Check your changes** (Python 3.9 or newer; no dependencies):

```sh
python3 -m unittest discover -s tests -v
python3 scripts/check_docs.py
```

This checks local links and anchors, translation structure/code/image parity, catalog counts, static badge syntax, and alt text. It does not make network requests or guarantee third-party uptime. If you have a current Simple Icons `simple-icons.json` data file locally, also run:

```sh
python3 scripts/check_docs.py --simple-icons /path/to/simple-icons.json
```

Before submitting a new external service or live-badge recipe, open its rendered image and destination in a browser. Never include access tokens or private endpoint URLs in examples.

## ⬢ Feedback

I try to review all Issues and Pull Requests as quickly as possible. Don't worry if your code isn't perfect — I'll review it, suggest tweaks, and help merge it. If I haven't replied in a while, don't hesitate to ping me in the comments.

The main rule is mutual respect. Welcome, and thank you for your contribution!

[![](https://capsule-render.vercel.app/api?type=rect&color=3e80ed&height=2&)](https://github.com/OstinUA)
