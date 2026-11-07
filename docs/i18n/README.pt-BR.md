# Badges para README

**Uma coleção de badges para copiar e colar e um guia prático para deixar READMEs do GitHub mais claros.**

[![License](https://img.shields.io/github/license/readme-SVG/readme-badges?style=flat-square)](../../LICENSE)
[![GitHub stars](https://img.shields.io/github/stars/readme-SVG/readme-badges?style=flat-square)](https://github.com/readme-SVG/readme-badges/stargazers)
[![Last commit](https://img.shields.io/github/last-commit/readme-SVG/readme-badges?style=flat-square)](https://github.com/readme-SVG/readme-badges/commits/main)
[![PRs welcome](https://img.shields.io/badge/PRs-welcome-brightgreen?style=flat-square)](../../CONTRIBUTING.md)

[English](../../README.md) · [Español](README.es.md) · **Português (Brasil)** · [Русский](README.ru.md) · [简体中文](README.zh-CN.md) · [日本語](README.ja.md)

Explore **699 exemplos de badges estáticos em 23 categorias**, entenda a diferença entre badges estáticos e dinâmicos e copie modelos para versões, builds, pacotes, documentação e links da comunidade. Não é necessário instalar nenhum aplicativo.

| Recurso | O que você vai encontrar |
| --- | --- |
| [**Catálogo de badges →**](../BADGE_CATALOG.md) | A coleção completa: linguagens, frameworks, nuvem, IA, testes, segurança, jogos, hardware, links sociais e muito mais |
| [**Guia de badges →**](../BADGE_GUIDE.md) | Tipos de badges, sintaxe de URLs, estilos, logotipos, dados dinâmicos, endpoints personalizados, gráficos de perfil e solução de problemas |
| [**Como contribuir →**](../../CONTRIBUTING.md) | Adicione um badge, corrija um logotipo, melhore um exemplo ou atualize uma tradução |

> [!TIP]
> Comece com uma fileira de badges úteis, não com uma parede de logotipos. Versão, status do build, licença e um link para a documentação geralmente dizem mais do que vinte rótulos de tecnologias.

## Conteúdo

- [Início rápido](#início-rápido)
- [Tipos de badges](#tipos-de-badges)
- [Estilos](#estilos)
- [Modelos de badges dinâmicos](#modelos-de-badges-dinâmicos)
- [Explore o catálogo](#explore-o-catálogo)
- [Alguns badges prontos para usar](#alguns-badges-prontos-para-usar)
- [Alertas Markdown do GitHub](#alertas-markdown-do-github)
- [Códigos de emoji do GitHub](#códigos-de-emoji-do-github)
- [Boas práticas](#boas-práticas)
- [Solução de problemas](#solução-de-problemas)
- [Contribuições e traduções](#contribuições-e-traduções)
- [Licença](#licença)

## Início rápido

Um badge é uma imagem Markdown. Coloque-a dentro de um link para torná-la clicável:

```markdown
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)

[![Documentation](https://img.shields.io/badge/docs-read-blue)](https://example.com/docs)
```

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)

1. Abra o [catálogo](../BADGE_CATALOG.md), encontre um badge e use a visualização **Raw** do GitHub para copiar o Markdown.
2. Cole no seu README. Para um README de perfil, o repositório geralmente é `SEU-USUÁRIO/SEU-USUÁRIO`.
3. Altere o rótulo, a cor, o logotipo ou o link de destino. Em um badge dinâmico, substitua `OWNER`, `REPO` e outros marcadores conforme explicado no [guia](../BADGE_GUIDE.md#4-dynamic-badges).

A URL básica do Shields é `https://img.shields.io/badge/LABEL-MESSAGE-COLOR`. Codifique `#` como `%23`, escape um hífen literal como `--` e use `_` ou `%20` para espaços. Consulte a [tabela completa de escapes](../BADGE_GUIDE.md#escaping-rules).

## Tipos de badges

O «tipo de badge» pode descrever como a imagem obtém seu valor **ou** o que esse valor significa. Estes são os principais tipos de implementação:

| Tipo | Exemplo | Atualiza automaticamente? |
| --- | --- | --- |
| **Estático** | `Python`, `status: beta`, `PRs welcome` | Não — edite o Markdown |
| **Dinâmico via serviço** | Estrelas do GitHub, versão no npm, status de CI | Sim — o provedor consulta um serviço de origem |
| **Dados dinâmicos** | Uma versão lida da sua API JSON | Sim — o provedor lê seus dados |
| **Endpoint** | Seu servidor fornece rótulo, mensagem e cor | Sim — você mantém o endpoint JSON |
| **Gráfico gerado** | Cartão de estatísticas, banner, cobrinha de contribuições | Depende do gerador ou do agendamento do workflow |

Os usos comuns incluem versões, saúde do build, cobertura, compatibilidade, licenças, downloads, comunidade, financiamento e estatísticas de perfil. A [taxonomia e as receitas](../BADGE_GUIDE.md#1-what-is-a-badge) explicam quando usar cada tipo.

> [!IMPORTANT]
> Um badge estático é um rótulo, não uma verificação. «Seguro» ou «100% testado» não se torna verdade por estar verde. Prefira um resultado dinâmico e com link quando a afirmação precisar de evidências.

## Estilos

Use o mesmo estilo dentro de um grupo visual. Acrescente `?style=STYLE` a uma URL do Shields:

| Estilo | Prévia |
| --- | --- |
| `plastic` | ![Plastic](https://img.shields.io/badge/style-plastic-blue?style=plastic) |
| `flat` | ![Flat](https://img.shields.io/badge/style-flat-blue?style=flat) |
| `flat-square` | ![Flat square](https://img.shields.io/badge/style-flat--square-blue?style=flat-square) |
| `social` | ![Social](https://img.shields.io/badge/style-social-blue?style=social&logo=github) |
| `for-the-badge` | ![For the badge](https://img.shields.io/badge/style-for--the--badge-blue?style=for-the-badge) |

O catálogo usa `for-the-badge`. O [guia](../BADGE_GUIDE.md#3-styles-colors-and-logos) também aborda cores, slugs de logotipos, ícones de marcas removidos e temas claro/escuro.

## Modelos de badges dinâmicos

Substitua `OWNER/REPO` pelo seu repositório. Estes exemplos são atualizados pelo GitHub; os números não estão fixos no texto.

```markdown
[![Release](https://img.shields.io/github/v/release/OWNER/REPO)](https://github.com/OWNER/REPO/releases)
[![License](https://img.shields.io/github/license/OWNER/REPO)](LICENSE)
[![CI](https://img.shields.io/github/actions/workflow/status/OWNER/REPO/ci.yml?branch=main)](https://github.com/OWNER/REPO/actions/workflows/ci.yml)
[![Open issues](https://img.shields.io/github/issues/OWNER/REPO)](https://github.com/OWNER/REPO/issues)
```

Use o nome real do arquivo do workflow no lugar de `ci.yml`. Para versões de pacotes, experimente `https://img.shields.io/npm/v/PACKAGE` ou `https://img.shields.io/pypi/v/PACKAGE`. O guia contém [modelos do GitHub](../BADGE_GUIDE.md#5-github-badges), [badges de registros e qualidade](../BADGE_GUIDE.md#6-packages-builds-and-quality) e [endpoints JSON personalizados](../BADGE_GUIDE.md#8-custom-dynamic-and-endpoint-badges).

## Explore o catálogo

Todos os **699 exemplos** estão em [**docs/BADGE_CATALOG.md**](../BADGE_CATALOG.md), com um índice clicável. A coleção original foi preservada e ampliada com **224 novos exemplos**.

| Área | Categorias incluídas |
| --- | --- |
| Linguagens e aplicativos | Linguagens de programação, frontend, backend, aplicativos multiplataforma |
| Infraestrutura | Bancos de dados, nuvem/DevOps, busca/bancos vetoriais, observabilidade |
| Desenvolvimento moderno | Assistentes/agentes de IA, testes/qualidade de código, segurança/identidade |
| Stacks especializadas | Desenvolvimento de jogos, IoT/hardware embarcado, blockchain/Web3 |
| Produtos e pessoas | Ferramentas/editores, navegadores/SO, ciência de dados, CMS/no-code, escritório/negócios, redes sociais/contato |
| Comunicação do projeto | Status/comunidade, documentação/publicação, acessibilidade/localização |

Estes são rótulos estáticos. Alguns logotipos foram removidos do Simple Icons, então seus badges usam texto legível no lugar de um ícone quebrado ou não relacionado. Veja as [alternativas para logotipos](../BADGE_GUIDE.md#named-logos-and-removed-brands).

## Alguns badges prontos para usar

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

Para badges sociais clicáveis, coloque a imagem dentro da URL do seu perfil ou convite. Para estatísticas de perfil, sequências, banners e cobrinhas de contribuições, veja os [gráficos gerados](../BADGE_GUIDE.md#9-generated-graphics-and-profile-tools).

## Alertas Markdown do GitHub

O GitHub oferece suporte a cinco tipos de alerta. Mantenha `>` em todas as linhas:

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
> Destaca informações que os usuários devem considerar, mesmo em uma leitura rápida.

> [!TIP]
> Informações opcionais para ajudar o usuário a obter melhores resultados.

> [!IMPORTANT]
> Informações essenciais para o usuário continuar com sucesso.

> [!WARNING]
> Conteúdo crítico que exige atenção imediata devido a possíveis riscos.

> [!CAUTION]
> Possíveis consequências negativas de uma ação.

## Códigos de emoji do GitHub

Códigos curtos como `:rocket:` aparecem como emoji no GitHub. Os exemplos específicos do GitHub originais foram preservados abaixo; a disponibilidade pode variar em outras plataformas Markdown.

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

Alguns códigos úteis no dia a dia: `:rocket:` :rocket:, `:white_check_mark:` :white_check_mark:, `:warning:` :warning:, `:bug:` :bug:, `:sparkles:` :sparkles:, `:books:` :books:, `:lock:` :lock:, `:construction:` :construction:, `:heart:` :heart:, `:tada:` :tada:, `:bulb:` :bulb: e `:memo:` :memo:.

## Boas práticas

- **Seja relevante.** Mostre a versão atual, o runtime compatível ou o status do build antes de logotipos decorativos.
- **Seja honesto.** Rótulos estáticos não verificam segurança, cobertura ou manutenção.
- **Seja consistente.** Use um estilo por grupo e texto alternativo descritivo em todas as imagens.
- **Seja útil.** Vincule badges a versões, relatórios, documentação ou instruções de contribuição.
- **Priorize a leitura.** Verifique telas estreitas, temas claro/escuro e falhas no carregamento de imagens.
- **Facilite a manutenção.** Prefira metadados dinâmicos quando evitarem edições manuais; não dependa de muitos serviços externos sem relação.

## Solução de problemas

| Problema | O que verificar primeiro |
| --- | --- |
| O logotipo não aparece | O slug do Simple Icons pode ter mudado ou o ícone da marca pode ter sido removido |
| `invalid` / `not found` | Compare a URL com o gerador de badges atual do provedor |
| O build mostra `no status` | Verifique o nome do arquivo do workflow, a branch e o evento que o aciona |
| O número parece desatualizado | A origem, o provedor do badge ou o proxy de imagens do GitHub podem estar usando cache |
| O texto ou a cor estão errados | Verifique os escapes `#` → `%23` e `-` literal → `--` |

Consulte o [guia completo de solução de problemas](../BADGE_GUIDE.md#11-troubleshooting). O verificador local da documentação é `python3 scripts/check_docs.py`; ele verifica a estrutura do repositório, não a disponibilidade de serviços externos.

## Contribuições e traduções

Contribuições são bem-vindas: novos badges, logotipos corrigidos, exemplos mais claros e traduções. Leia [CONTRIBUTING.md](../../CONTRIBUTING.md), siga o [Código de Conduta](../../CODE_OF_CONDUCT.md) e relate vulnerabilidades conforme [SECURITY.md](../../SECURITY.md).

O inglês é a versão de referência. Este README foi traduzido integralmente para espanhol, português brasileiro, russo, chinês simplificado e japonês por meio do seletor de idiomas acima. O catálogo compartilhado e o guia detalhado permanecem em inglês; nomes de marcas, URLs e exemplos de código são consistentes entre os idiomas. Atualize os seis arquivos README ao alterar conteúdo compartilhado.

## Licença

[MIT](../../LICENSE). Os serviços de badges, nomes de marcas e logotipos pertencem aos seus respectivos proprietários; a inclusão aqui não implica endosso.
