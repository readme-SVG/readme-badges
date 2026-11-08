# README バッジ

**コピーして使えるバッジ集と、GitHub の README をわかりやすくするための実践ガイド。**

[![License](https://img.shields.io/github/license/readme-SVG/readme-badges?style=flat-square)](../../LICENSE)
[![GitHub stars](https://img.shields.io/github/stars/readme-SVG/readme-badges?style=flat-square)](https://github.com/readme-SVG/readme-badges/stargazers)
[![Last commit](https://img.shields.io/github/last-commit/readme-SVG/readme-badges?style=flat-square)](https://github.com/readme-SVG/readme-badges/commits/main)
[![PRs welcome](https://img.shields.io/badge/PRs-welcome-brightgreen?style=flat-square)](../../CONTRIBUTING.md)

[English](../../README.md) · [Español](README.es.md) · [Português (Brasil)](README.pt-BR.md) · [Русский](README.ru.md) · [简体中文](README.zh-CN.md) · **日本語**

**23 カテゴリ・699 個の静的バッジ例**を閲覧し、静的バッジと動的バッジの違いを理解できます。リリース、ビルド、パッケージバージョン、ドキュメント、コミュニティリンク用のテンプレートもそのままコピーできます。アプリのインストールは不要です。

| リソース | 内容 |
| --- | --- |
| [**バッジカタログ →**](../BADGE_CATALOG.md) | 言語、フレームワーク、クラウド、AI、テスト、セキュリティ、ゲーム、ハードウェア、SNS リンクなどの完全なコレクション |
| [**バッジガイド →**](../BADGE_GUIDE.md) | バッジの種類、URL 構文、スタイル、ロゴ、動的データ、カスタムエンドポイント、プロフィール画像、トラブルシューティング |
| [**コントリビュート →**](../../CONTRIBUTING.md) | バッジの追加、ロゴの修正、例の改善、翻訳の更新 |

> [!TIP]
> ロゴを大量に並べるより、まず役立つバッジを一行だけ置きましょう。リリース、ビルド状態、ライセンス、ドキュメントへのリンクは、20 個の技術ラベルよりも訪問者に多くの情報を伝えられます。

## 目次

- [クイックスタート](#クイックスタート)
- [バッジの種類](#バッジの種類)
- [スタイル](#スタイル)
- [動的バッジのテンプレート](#動的バッジのテンプレート)
- [カタログを見る](#カタログを見る)
- [すぐ使えるバッジ例](#すぐ使えるバッジ例)
- [GitHub Markdown アラート](#github-markdown-アラート)
- [GitHub 絵文字コード](#github-絵文字コード)
- [おすすめの方針](#おすすめの方針)
- [トラブルシューティング](#トラブルシューティング)
- [コントリビュートと翻訳](#コントリビュートと翻訳)
- [ライセンス](#ライセンス)

## クイックスタート

バッジは Markdown の画像です。リンクで囲むとクリックできるようになります。

```markdown
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)

[![Documentation](https://img.shields.io/badge/docs-read-blue)](https://example.com/docs)
```

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)

1. [カタログ](../BADGE_CATALOG.md)でバッジを探し、GitHub の **Raw** 表示から Markdown をコピーします。
2. 自分の README に貼り付けます。プロフィール用 README は通常 `あなたのユーザー名/あなたのユーザー名` というリポジトリに置きます。
3. ラベル、色、ロゴ、リンク先を変更します。動的バッジでは[ガイド](../BADGE_GUIDE.md#4-dynamic-badges)に従って `OWNER`、`REPO` などのプレースホルダーを置き換えてください。

Shields の基本 URL は `https://img.shields.io/badge/LABEL-MESSAGE-COLOR` です。`#` は `%23` にエンコードし、文字としてのハイフンは `--`、スペースは `_` または `%20` で表します。[エスケープ一覧](../BADGE_GUIDE.md#escaping-rules)を参照してください。

## バッジの種類

「バッジの種類」は、画像が値を取得する方法と、その値が何を表すかの両方を指します。実装方法による主な分類は次のとおりです。

| 種類 | 例 | 自動更新される？ |
| --- | --- | --- |
| **静的** | `Python`、`status: beta`、`PRs welcome` | いいえ — Markdown を編集します |
| **サービス連携型動的** | GitHub スター、npm バージョン、CI 状態 | はい — プロバイダーが情報源のサービスを読み取ります |
| **動的データ** | 自分の JSON API から読み取るバージョン | はい — プロバイダーが自分のデータを読み取ります |
| **エンドポイント** | 自分のサーバーがラベル、メッセージ、色を返す | はい — JSON エンドポイントを自分で管理します |
| **生成グラフィック** | 統計カード、バナー、コントリビューション・スネーク | ジェネレーターやワークフローのスケジュールによります |

リリース、ビルドの健全性、カバレッジ、互換性、ライセンス、ダウンロード数、コミュニティ、寄付、プロフィール統計などが主な用途です。[分類とレシピ](../BADGE_GUIDE.md#1-what-is-a-badge)で使い分けを説明しています。

> [!IMPORTANT]
> 静的バッジはラベルであり、検証結果ではありません。「安全」や「100% テスト済み」は緑色で表示しても事実にはなりません。根拠が必要な主張には、実際の結果へリンクする動的バッジを使いましょう。

## スタイル

視覚的なグループ内では同じスタイルを使いましょう。Shields の URL に `?style=STYLE` を追加します。

| スタイル | プレビュー |
| --- | --- |
| `plastic` | ![Plastic](https://img.shields.io/badge/style-plastic-blue?style=plastic) |
| `flat` | ![Flat](https://img.shields.io/badge/style-flat-blue?style=flat) |
| `flat-square` | ![Flat square](https://img.shields.io/badge/style-flat--square-blue?style=flat-square) |
| `social` | ![Social](https://img.shields.io/badge/style-social-blue?style=social&logo=github) |
| `for-the-badge` | ![For the badge](https://img.shields.io/badge/style-for--the--badge-blue?style=for-the-badge) |

カタログでは `for-the-badge` を使用しています。[ガイド](../BADGE_GUIDE.md#3-styles-colors-and-logos)では色、ロゴの slug、削除されたブランドアイコン、ライト・ダークテーマも扱っています。

## 動的バッジのテンプレート

`OWNER/REPO` を自分のリポジトリに置き換えてください。これらの例は GitHub から更新され、数値は手動で固定されていません。

```markdown
[![Release](https://img.shields.io/github/v/release/OWNER/REPO)](https://github.com/OWNER/REPO/releases)
[![License](https://img.shields.io/github/license/OWNER/REPO)](LICENSE)
[![CI](https://img.shields.io/github/actions/workflow/status/OWNER/REPO/ci.yml?branch=main)](https://github.com/OWNER/REPO/actions/workflows/ci.yml)
[![Open issues](https://img.shields.io/github/issues/OWNER/REPO)](https://github.com/OWNER/REPO/issues)
```

`ci.yml` は実際のワークフローファイル名に置き換えてください。パッケージバージョンには `https://img.shields.io/npm/v/PACKAGE` や `https://img.shields.io/pypi/v/PACKAGE` を試せます。ガイドには [GitHub テンプレート](../BADGE_GUIDE.md#5-github-badges)、[レジストリと品質のバッジ](../BADGE_GUIDE.md#6-packages-builds-and-quality)、[カスタム JSON エンドポイント](../BADGE_GUIDE.md#8-custom-dynamic-and-endpoint-badges)があります。

## カタログを見る

**699 個すべての例**は [**docs/BADGE_CATALOG.md**](../BADGE_CATALOG.md) にあり、クリック可能な目次が付いています。元のコレクションを保持しつつ、**224 個の新しい例**を追加しました。

| 分野 | 含まれるカテゴリ |
| --- | --- |
| 言語とアプリ | プログラミング言語、フロントエンド、バックエンド、クロスプラットフォームアプリ |
| インフラ | データベース、クラウド/DevOps、検索・ベクトルデータベース、オブザーバビリティ |
| 現代的な開発 | AI アシスタント/エージェント、テスト/コード品質、セキュリティ/認証 |
| 専門スタック | ゲーム開発、IoT/組み込みハードウェア、ブロックチェーン/Web3 |
| プロダクトと人 | ツール/エディター、ブラウザー/OS、データサイエンス、CMS/ノーコード、オフィス/ビジネス、SNS/連絡先 |
| プロジェクトの情報 | 状態/コミュニティ、ドキュメント/公開、アクセシビリティ/ローカライズ |

これらは静的ラベルです。一部のロゴは Simple Icons から削除されたため、壊れたアイコンや無関係なアイコンの代わりに読めるテキストを使用しています。[ロゴの代替方法](../BADGE_GUIDE.md#named-logos-and-removed-brands)を参照してください。

## すぐ使えるバッジ例

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

クリックできる SNS バッジにするには、画像を自分のプロフィールや招待 URL のリンクで囲みます。プロフィール統計、連続コントリビューション、バナー、スネークについては[生成グラフィック](../BADGE_GUIDE.md#9-generated-graphics-and-profile-tools)を参照してください。

## GitHub Markdown アラート

GitHub は 5 種類のアラートに対応しています。各行に `>` を付けてください。

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
> 流し読みするときでも考慮すべき情報を強調します。

> [!TIP]
> より良い結果を得るための補足的なヒントです。

> [!IMPORTANT]
> 作業を正しく進めるために必要な重要情報です。

> [!WARNING]
> 潜在的なリスクのため、直ちに注意が必要な内容です。

> [!CAUTION]
> 操作によって生じる可能性のある悪影響を示します。

## GitHub 絵文字コード

`:rocket:` のようなショートコードは GitHub で絵文字として表示されます。元の GitHub 固有の例を以下に残しています。他の Markdown プラットフォームでは利用できない場合があります。

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

よく使うコード：`:rocket:` :rocket:、`:white_check_mark:` :white_check_mark:、`:warning:` :warning:、`:bug:` :bug:、`:sparkles:` :sparkles:、`:books:` :books:、`:lock:` :lock:、`:construction:` :construction:、`:heart:` :heart:、`:tada:` :tada:、`:bulb:` :bulb:、`:memo:` :memo:。

## おすすめの方針

- **関連性を重視する。** 装飾的なロゴより、現在のリリース、対応ランタイム、ビルド状態を先に示します。
- **正確に伝える。** 静的ラベルは安全性、カバレッジ、メンテナンス状況を検証しません。
- **一貫性を保つ。** グループごとに一つのスタイルを使い、すべての画像に説明的な代替テキストを付けます。
- **役立つリンクにする。** リリース、レポート、ドキュメント、コントリビュート手順へつなげます。
- **読みやすさを確認する。** 狭い画面、ライト・ダークテーマ、画像読み込み失敗時の表示を確認します。
- **保守しやすくする。** 手作業の更新を減らせる場合は動的メタデータを使い、無関係な外部サービスへの依存を増やしすぎないようにします。

## トラブルシューティング

| 問題 | 最初に確認すること |
| --- | --- |
| ロゴが表示されない | Simple Icons の slug が変更されたか、ブランドアイコンが削除された可能性があります |
| `invalid` / `not found` | プロバイダーの現在のバッジ作成画面と URL を比較します |
| ビルドが `no status` | ワークフローのファイル名、ブランチ、トリガーイベントを確認します |
| 数値が古い | 情報源、バッジプロバイダー、GitHub 画像プロキシのキャッシュが考えられます |
| テキストや色が違う | `#` → `%23` と文字としての `-` → `--` のエスケープを確認します |

[詳しいトラブルシューティング](../BADGE_GUIDE.md#11-troubleshooting)を参照してください。ローカルのドキュメントチェッカーは `python3 scripts/check_docs.py` です。リポジトリ構造を検査するもので、外部サービスの稼働状況は保証しません。

## コントリビュートと翻訳

新しいバッジ、ロゴの修正、わかりやすい例、翻訳など、あらゆる貢献を歓迎します。[CONTRIBUTING.md](../../CONTRIBUTING.md)を読み、[行動規範](../../CODE_OF_CONDUCT.md)に従い、脆弱性は [SECURITY.md](../../SECURITY.md) の手順で報告してください。

英語版が基準です。この README はスペイン語、ブラジルポルトガル語、ロシア語、簡体字中国語、日本語に全文翻訳されており、上部の言語切り替えから移動できます。共有カタログと詳細ガイドは英語のままです。ブランド名、URL、コード例は言語間で統一しています。共有内容を変更するときは、6 つすべての README ファイルを更新してください。

## ライセンス

[MIT](../../LICENSE)。バッジサービス、ブランド名、ロゴはそれぞれの所有者に帰属します。ここに含まれることは推奨や提携を意味しません。
