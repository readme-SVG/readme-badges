# Бейджи для README

**Коллекция бейджей для копирования и практическое руководство по созданию понятных README на GitHub.**

[![License](https://img.shields.io/github/license/readme-SVG/readme-badges?style=flat-square)](../../LICENSE)
[![GitHub stars](https://img.shields.io/github/stars/readme-SVG/readme-badges?style=flat-square)](https://github.com/readme-SVG/readme-badges/stargazers)
[![Last commit](https://img.shields.io/github/last-commit/readme-SVG/readme-badges?style=flat-square)](https://github.com/readme-SVG/readme-badges/commits/main)
[![PRs welcome](https://img.shields.io/badge/PRs-welcome-brightgreen?style=flat-square)](../../CONTRIBUTING.md)

[English](../../README.md) · [Español](README.es.md) · [Português (Brasil)](README.pt-BR.md) · **Русский** · [简体中文](README.zh-CN.md) · [日本語](README.ja.md)

Здесь собраны **699 статических бейджей в 23 категориях**. Разберитесь, чем статические бейджи отличаются от динамических, и скопируйте шаблоны для релизов, сборок, версий пакетов, документации и ссылок на сообщество. Устанавливать приложения не нужно.

| Ресурс | Что внутри |
| --- | --- |
| [**Каталог бейджей →**](../BADGE_CATALOG.md) | Полная коллекция: языки, фреймворки, облака, ИИ, тестирование, безопасность, игры, железо, социальные ссылки и не только |
| [**Руководство по бейджам →**](../BADGE_GUIDE.md) | Типы бейджей, синтаксис URL, стили, логотипы, динамические данные, свои эндпоинты, графика для профиля и решение проблем |
| [**Как помочь проекту →**](../../CONTRIBUTING.md) | Добавьте бейдж, исправьте логотип, улучшите пример или обновите перевод |

> [!TIP]
> Начните с одной строки полезных бейджей, а не со стены логотипов. Версия, статус сборки, лицензия и ссылка на документацию обычно говорят посетителю больше, чем двадцать названий технологий.

## Содержание

- [Быстрый старт](#быстрый-старт)
- [Типы бейджей](#типы-бейджей)
- [Стили](#стили)
- [Шаблоны динамических бейджей](#шаблоны-динамических-бейджей)
- [Обзор каталога](#обзор-каталога)
- [Несколько готовых бейджей](#несколько-готовых-бейджей)
- [Markdown-уведомления GitHub](#markdown-уведомления-github)
- [Коды эмодзи GitHub](#коды-эмодзи-github)
- [Полезные правила](#полезные-правила)
- [Решение проблем](#решение-проблем)
- [Участие и переводы](#участие-и-переводы)
- [Лицензия](#лицензия)

## Быстрый старт

Бейдж — это изображение в Markdown. Оберните его в ссылку, чтобы по нему можно было кликнуть:

```markdown
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)

[![Documentation](https://img.shields.io/badge/docs-read-blue)](https://example.com/docs)
```

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)

1. Откройте [каталог](../BADGE_CATALOG.md), найдите бейдж и скопируйте его Markdown через режим просмотра **Raw** на GitHub.
2. Вставьте его в свой README. Для README профиля обычно используется репозиторий `ВАШ-ЛОГИН/ВАШ-ЛОГИН`.
3. Измените подпись, цвет, логотип или ссылку назначения. В динамическом бейдже замените `OWNER`, `REPO` и другие заполнители по инструкции из [руководства](../BADGE_GUIDE.md#4-dynamic-badges).

Базовый URL Shields: `https://img.shields.io/badge/LABEL-MESSAGE-COLOR`. Кодируйте `#` как `%23`, экранируйте обычный дефис как `--`, а для пробелов используйте `_` или `%20`. См. [полную таблицу экранирования](../BADGE_GUIDE.md#escaping-rules).

## Типы бейджей

«Тип бейджа» может означать способ получения значения **или** смысл этого значения. Вот основные типы по способу реализации:

| Тип | Пример | Обновляется автоматически? |
| --- | --- | --- |
| **Статический** | `Python`, `status: beta`, `PRs welcome` | Нет — нужно редактировать Markdown |
| **Динамический через сервис** | Звёзды GitHub, версия npm, статус CI | Да — провайдер обращается к сервису-источнику |
| **Динамические данные** | Версия из вашего JSON API | Да — провайдер читает ваши данные |
| **Эндпоинт** | Ваш сервер задаёт подпись, сообщение и цвет | Да — вы поддерживаете JSON-эндпоинт |
| **Сгенерированная графика** | Карточка статистики, баннер, змейка вкладов | Зависит от генератора или расписания workflow |

Основные назначения: релизы, состояние сборки, покрытие тестами, совместимость, лицензии, загрузки, сообщество, финансирование и статистика профиля. [Классификация и рецепты](../BADGE_GUIDE.md#1-what-is-a-badge) объясняют, когда какой тип использовать.

> [!IMPORTANT]
> Статический бейдж — это подпись, а не подтверждение факта. Надписи «Безопасно» и «100% протестировано» не становятся правдой от зелёного цвета. Если утверждение требует доказательств, используйте динамический бейдж со ссылкой на результат.

## Стили

В пределах одной визуальной группы используйте одинаковый стиль. Добавьте `?style=STYLE` к URL Shields:

| Стиль | Предпросмотр |
| --- | --- |
| `plastic` | ![Plastic](https://img.shields.io/badge/style-plastic-blue?style=plastic) |
| `flat` | ![Flat](https://img.shields.io/badge/style-flat-blue?style=flat) |
| `flat-square` | ![Flat square](https://img.shields.io/badge/style-flat--square-blue?style=flat-square) |
| `social` | ![Social](https://img.shields.io/badge/style-social-blue?style=social&logo=github) |
| `for-the-badge` | ![For the badge](https://img.shields.io/badge/style-for--the--badge-blue?style=for-the-badge) |

В каталоге используется `for-the-badge`. В [руководстве](../BADGE_GUIDE.md#3-styles-colors-and-logos) также разбираются цвета, slug-идентификаторы логотипов, удалённые иконки брендов и светлая/тёмная темы.

## Шаблоны динамических бейджей

Замените `OWNER/REPO` на свой репозиторий. Эти примеры получают актуальные данные из GitHub; числа в них не зашиты вручную.

```markdown
[![Release](https://img.shields.io/github/v/release/OWNER/REPO)](https://github.com/OWNER/REPO/releases)
[![License](https://img.shields.io/github/license/OWNER/REPO)](LICENSE)
[![CI](https://img.shields.io/github/actions/workflow/status/OWNER/REPO/ci.yml?branch=main)](https://github.com/OWNER/REPO/actions/workflows/ci.yml)
[![Open issues](https://img.shields.io/github/issues/OWNER/REPO)](https://github.com/OWNER/REPO/issues)
```

Вместо `ci.yml` укажите настоящее имя файла workflow. Для версий пакетов попробуйте `https://img.shields.io/npm/v/PACKAGE` или `https://img.shields.io/pypi/v/PACKAGE`. В руководстве есть [шаблоны GitHub](../BADGE_GUIDE.md#5-github-badges), [бейджи реестров и качества кода](../BADGE_GUIDE.md#6-packages-builds-and-quality) и [собственные JSON-эндпоинты](../BADGE_GUIDE.md#8-custom-dynamic-and-endpoint-badges).

## Обзор каталога

Все **699 примеров** находятся в [**docs/BADGE_CATALOG.md**](../BADGE_CATALOG.md) с кликабельным оглавлением. Исходная коллекция сохранена и дополнена **224 новыми примерами**.

| Область | Примеры категорий |
| --- | --- |
| Языки и приложения | Языки программирования, frontend, backend, кроссплатформенные приложения |
| Инфраструктура | Базы данных, облака/DevOps, поиск/векторные БД, наблюдаемость |
| Современная разработка | ИИ-помощники/агенты, тестирование/качество кода, безопасность/идентификация |
| Специализированные стеки | Разработка игр, IoT/встраиваемое железо, блокчейн/Web3 |
| Продукты и люди | Инструменты/редакторы, браузеры/ОС, data science, CMS/no-code, офис/бизнес, социальные сети/контакты |
| Коммуникация проекта | Статус/сообщество, документация/публикация, доступность/локализация |

Это статические подписи. Некоторые логотипы удалены из Simple Icons, поэтому в таких бейджах намеренно используется читаемый текст вместо сломанной или неподходящей иконки. См. [варианты замены логотипов](../BADGE_GUIDE.md#named-logos-and-removed-brands).

## Несколько готовых бейджей

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

Чтобы сделать социальный бейдж кликабельным, оберните изображение в ссылку на свой профиль или приглашение. Статистика профиля, серии активности, баннеры и змейки вкладов разобраны в разделе [генерируемой графики](../BADGE_GUIDE.md#9-generated-graphics-and-profile-tools).

## Markdown-уведомления GitHub

GitHub поддерживает пять типов уведомлений. Оставляйте `>` в начале каждой строки:

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
> Важная информация, которую стоит учесть даже при беглом чтении.

> [!TIP]
> Дополнительный совет, который поможет добиться лучшего результата.

> [!IMPORTANT]
> Ключевая информация, необходимая для успешной работы.

> [!WARNING]
> Критически важная информация, требующая немедленного внимания из-за возможных рисков.

> [!CAUTION]
> Возможные негативные последствия действия.

## Коды эмодзи GitHub

Короткие коды вроде `:rocket:` отображаются на GitHub как эмодзи. Ниже сохранены исходные примеры специфичных для GitHub кодов; на других Markdown-платформах их доступность может отличаться.

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

Полезные коды на каждый день: `:rocket:` :rocket:, `:white_check_mark:` :white_check_mark:, `:warning:` :warning:, `:bug:` :bug:, `:sparkles:` :sparkles:, `:books:` :books:, `:lock:` :lock:, `:construction:` :construction:, `:heart:` :heart:, `:tada:` :tada:, `:bulb:` :bulb: и `:memo:` :memo:.

## Полезные правила

- **Выбирайте по смыслу.** Сначала покажите актуальную версию, поддерживаемую среду выполнения или статус сборки, а уже потом декоративные логотипы.
- **Не вводите в заблуждение.** Статические подписи не подтверждают безопасность, покрытие тестами или поддержку проекта.
- **Соблюдайте единообразие.** Один стиль на группу и осмысленный альтернативный текст у каждого изображения.
- **Приносите пользу.** Ведите с бейджей на релизы, отчёты, документацию или инструкции для участников.
- **Заботьтесь о читаемости.** Проверяйте узкие экраны, светлую/тёмную темы и ситуации, когда изображения не загрузились.
- **Упрощайте поддержку.** Используйте динамические метаданные, если они избавляют от ручных правок; не зависьте от множества посторонних сервисов.

## Решение проблем

| Проблема | Что проверить сначала |
| --- | --- |
| Пропал логотип | Slug в Simple Icons мог измениться, либо иконку бренда удалили |
| `invalid` / `not found` | Сравните URL с актуальным конструктором бейджей провайдера |
| Сборка показывает `no status` | Проверьте имя файла workflow, ветку и событие запуска |
| Число выглядит устаревшим | Источник, провайдер бейджа или прокси изображений GitHub может кешировать результат |
| Неверный текст или цвет | Проверьте экранирование `#` → `%23` и обычного `-` → `--` |

См. [полное руководство по решению проблем](../BADGE_GUIDE.md#11-troubleshooting). Локальная проверка документации запускается командой `python3 scripts/check_docs.py`; она проверяет структуру репозитория, а не доступность сторонних сервисов.

## Участие и переводы

Будем рады помощи: новым бейджам, исправленным логотипам, понятным примерам и переводам. Прочитайте [CONTRIBUTING.md](../../CONTRIBUTING.md), соблюдайте [Кодекс поведения](../../CODE_OF_CONDUCT.md) и сообщайте об уязвимостях по правилам [SECURITY.md](../../SECURITY.md).

Основная версия — английская. README полностью переведён на испанский, бразильский португальский, русский, упрощённый китайский и японский; переключатель языков находится вверху. Общий каталог и подробное руководство остаются на английском; названия брендов, URL и примеры кода одинаковы во всех языковых версиях. При изменении общего содержания обновляйте все шесть файлов README.

## Лицензия

[MIT](../../LICENSE). Сервисы бейджей, названия брендов и логотипы принадлежат их владельцам; их присутствие здесь не означает одобрения или партнёрства.
