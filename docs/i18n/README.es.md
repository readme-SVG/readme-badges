# Badges para README

**Una colección de badges para copiar y pegar, y una guía práctica para crear READMEs de GitHub más claros.**

[![License](https://img.shields.io/github/license/readme-SVG/readme-badges?style=flat-square)](../../LICENSE)
[![GitHub stars](https://img.shields.io/github/stars/readme-SVG/readme-badges?style=flat-square)](https://github.com/readme-SVG/readme-badges/stargazers)
[![Last commit](https://img.shields.io/github/last-commit/readme-SVG/readme-badges?style=flat-square)](https://github.com/readme-SVG/readme-badges/commits/main)
[![PRs welcome](https://img.shields.io/badge/PRs-welcome-brightgreen?style=flat-square)](../../CONTRIBUTING.md)

[English](../../README.md) · **Español** · [Português (Brasil)](README.pt-BR.md) · [Русский](README.ru.md) · [简体中文](README.zh-CN.md) · [日本語](README.ja.md)

Explora **699 ejemplos de badges estáticos en 23 categorías**, aprende a distinguir los badges estáticos de los dinámicos y copia plantillas para versiones, compilaciones, paquetes, documentación y enlaces de comunidad. No necesitas instalar ninguna aplicación.

| Recurso | Qué encontrarás |
| --- | --- |
| [**Catálogo de badges →**](../BADGE_CATALOG.md) | La colección completa: lenguajes, frameworks, nube, IA, pruebas, seguridad, juegos, hardware, enlaces sociales y mucho más |
| [**Guía de badges →**](../BADGE_GUIDE.md) | Tipos de badges, sintaxis de URL, estilos, logotipos, datos dinámicos, endpoints personalizados, gráficos de perfil y resolución de problemas |
| [**Cómo contribuir →**](../../CONTRIBUTING.md) | Añade un badge, corrige un logotipo, mejora un ejemplo o actualiza una traducción |

> [!TIP]
> Empieza con una fila de badges útiles, no con un muro de logotipos. La versión, el estado de la compilación, la licencia y un enlace a la documentación suelen aportar más que veinte etiquetas de tecnologías.

## Contenidos

- [Inicio rápido](#inicio-rápido)
- [Tipos de badges](#tipos-de-badges)
- [Estilos](#estilos)
- [Plantillas de badges dinámicos](#plantillas-de-badges-dinámicos)
- [Explorar el catálogo](#explorar-el-catálogo)
- [Algunos badges listos para usar](#algunos-badges-listos-para-usar)
- [Alertas Markdown de GitHub](#alertas-markdown-de-github)
- [Códigos de emoji de GitHub](#códigos-de-emoji-de-github)
- [Valores recomendados](#valores-recomendados)
- [Resolución de problemas](#resolución-de-problemas)
- [Contribuciones y traducciones](#contribuciones-y-traducciones)
- [Licencia](#licencia)

## Inicio rápido

Un badge es una imagen Markdown. Envuélvela en un enlace para que se pueda hacer clic en ella:

```markdown
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)

[![Documentation](https://img.shields.io/badge/docs-read-blue)](https://example.com/docs)
```

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)

1. Abre el [catálogo](../BADGE_CATALOG.md), busca un badge y usa la vista **Raw** de GitHub para copiar su Markdown.
2. Pégalo en tu README. Para un README de perfil, el repositorio suele ser `TU-USUARIO/TU-USUARIO`.
3. Cambia la etiqueta, el color, el logotipo o el enlace de destino. En un badge dinámico, sustituye `OWNER`, `REPO` y otros marcadores como se explica en la [guía](../BADGE_GUIDE.md#4-dynamic-badges).

La URL básica de Shields es `https://img.shields.io/badge/LABEL-MESSAGE-COLOR`. Codifica `#` como `%23`, escapa un guion literal como `--` y usa `_` o `%20` para los espacios. Consulta la [tabla completa de escapes](../BADGE_GUIDE.md#escaping-rules).

## Tipos de badges

El «tipo de badge» puede describir cómo obtiene su valor la imagen **o** qué significa ese valor. Estos son los principales tipos según su implementación:

| Tipo | Ejemplo | ¿Se actualiza automáticamente? |
| --- | --- | --- |
| **Estático** | `Python`, `status: beta`, `PRs welcome` | No — edita el Markdown |
| **Dinámico mediante un servicio** | Estrellas de GitHub, versión de npm, estado de CI | Sí — el proveedor consulta un servicio de origen |
| **Datos dinámicos** | Una versión leída de tu API JSON | Sí — el proveedor lee tus datos |
| **Endpoint** | Tu servidor proporciona etiqueta, mensaje y color | Sí — tú mantienes el endpoint JSON |
| **Gráfico generado** | Tarjeta de estadísticas, banner, serpiente de contribuciones | Depende del generador o de la programación del workflow |

Los usos habituales incluyen versiones, estado de compilación, cobertura, compatibilidad, licencias, descargas, comunidad, financiación y estadísticas de perfil. La [taxonomía y las recetas](../BADGE_GUIDE.md#1-what-is-a-badge) explican cuándo usar cada tipo.

> [!IMPORTANT]
> Un badge estático es una etiqueta, no una verificación. «Seguro» o «100% probado» no se vuelve cierto por aparecer en verde. Prefiere un resultado dinámico y enlazado cuando la afirmación necesite pruebas.

## Estilos

Usa el mismo estilo dentro de un grupo visual. Añade `?style=STYLE` a una URL de Shields:

| Estilo | Vista previa |
| --- | --- |
| `plastic` | ![Plastic](https://img.shields.io/badge/style-plastic-blue?style=plastic) |
| `flat` | ![Flat](https://img.shields.io/badge/style-flat-blue?style=flat) |
| `flat-square` | ![Flat square](https://img.shields.io/badge/style-flat--square-blue?style=flat-square) |
| `social` | ![Social](https://img.shields.io/badge/style-social-blue?style=social&logo=github) |
| `for-the-badge` | ![For the badge](https://img.shields.io/badge/style-for--the--badge-blue?style=for-the-badge) |

El catálogo utiliza `for-the-badge`. La [guía](../BADGE_GUIDE.md#3-styles-colors-and-logos) también explica los colores, los slugs de logotipos, los iconos de marcas eliminados y los temas claro/oscuro.

## Plantillas de badges dinámicos

Sustituye `OWNER/REPO` por tu repositorio. Estos ejemplos se actualizan desde GitHub; los números no están escritos manualmente.

```markdown
[![Release](https://img.shields.io/github/v/release/OWNER/REPO)](https://github.com/OWNER/REPO/releases)
[![License](https://img.shields.io/github/license/OWNER/REPO)](LICENSE)
[![CI](https://img.shields.io/github/actions/workflow/status/OWNER/REPO/ci.yml?branch=main)](https://github.com/OWNER/REPO/actions/workflows/ci.yml)
[![Open issues](https://img.shields.io/github/issues/OWNER/REPO)](https://github.com/OWNER/REPO/issues)
```

Usa el nombre real del archivo del workflow en lugar de `ci.yml`. Para versiones de paquetes, prueba `https://img.shields.io/npm/v/PACKAGE` o `https://img.shields.io/pypi/v/PACKAGE`. La guía incluye [plantillas de GitHub](../BADGE_GUIDE.md#5-github-badges), [badges de registros y calidad](../BADGE_GUIDE.md#6-packages-builds-and-quality) y [endpoints JSON personalizados](../BADGE_GUIDE.md#8-custom-dynamic-and-endpoint-badges).

## Explorar el catálogo

Los **699 ejemplos** están en [**docs/BADGE_CATALOG.md**](../BADGE_CATALOG.md), con un índice navegable. Se conserva la colección original y se amplía con **224 ejemplos nuevos**.

| Área | Categorías incluidas |
| --- | --- |
| Lenguajes y aplicaciones | Lenguajes de programación, frontend, backend, aplicaciones multiplataforma |
| Infraestructura | Bases de datos, nube/DevOps, búsqueda/bases de datos vectoriales, observabilidad |
| Desarrollo moderno | Asistentes/agentes de IA, pruebas/calidad de código, seguridad/identidad |
| Stacks especializados | Desarrollo de juegos, IoT/hardware embebido, blockchain/Web3 |
| Productos y personas | Herramientas/editores, navegadores/SO, ciencia de datos, CMS/no-code, oficina/negocios, redes/contacto |
| Comunicación del proyecto | Estado/comunidad, documentación/publicación, accesibilidad/localización |

Estas son etiquetas estáticas. Algunos logotipos se eliminaron de Simple Icons, por lo que sus badges utilizan texto legible en lugar de un icono roto o no relacionado. Consulta las [alternativas para logotipos](../BADGE_GUIDE.md#named-logos-and-removed-brands).

## Algunos badges listos para usar

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

Para badges sociales en los que se pueda hacer clic, envuelve la imagen en la URL de tu perfil o invitación. Para estadísticas de perfil, rachas, banners y serpientes de contribuciones, consulta los [gráficos generados](../BADGE_GUIDE.md#9-generated-graphics-and-profile-tools).

## Alertas Markdown de GitHub

GitHub admite cinco tipos de alerta. Mantén `>` en cada línea:

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
> Destaca información que los usuarios deben tener en cuenta, incluso al leer rápidamente.

> [!TIP]
> Información opcional para ayudar al usuario a obtener mejores resultados.

> [!IMPORTANT]
> Información esencial para que el usuario pueda continuar correctamente.

> [!WARNING]
> Contenido crítico que requiere atención inmediata debido a posibles riesgos.

> [!CAUTION]
> Posibles consecuencias negativas de una acción.

## Códigos de emoji de GitHub

Los códigos cortos como `:rocket:` se muestran como emoji en GitHub. A continuación se conservan los ejemplos específicos de GitHub originales; la disponibilidad puede variar en otras plataformas Markdown.

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

Algunos códigos útiles para el día a día: `:rocket:` :rocket:, `:white_check_mark:` :white_check_mark:, `:warning:` :warning:, `:bug:` :bug:, `:sparkles:` :sparkles:, `:books:` :books:, `:lock:` :lock:, `:construction:` :construction:, `:heart:` :heart:, `:tada:` :tada:, `:bulb:` :bulb: y `:memo:` :memo:.

## Valores recomendados

- **Sé relevante.** Muestra la versión actual, el runtime compatible o el estado de compilación antes que los logotipos decorativos.
- **Sé honesto.** Las etiquetas estáticas no verifican la seguridad, la cobertura ni el mantenimiento.
- **Sé consistente.** Usa un estilo por grupo y texto alternativo descriptivo en cada imagen.
- **Sé útil.** Enlaza los badges a versiones, informes, documentación o instrucciones para contribuir.
- **Prioriza la legibilidad.** Comprueba pantallas estrechas, temas claro/oscuro y errores de carga de imágenes.
- **Facilita el mantenimiento.** Prefiere metadatos dinámicos cuando ahorren ediciones manuales; evita depender de muchos servicios externos sin relación.

## Resolución de problemas

| Problema | Qué comprobar primero |
| --- | --- |
| Falta el logotipo | El slug de Simple Icons puede haber cambiado o el icono de la marca puede haberse eliminado |
| `invalid` / `not found` | Compara la URL con el generador de badges actual del proveedor |
| La compilación muestra `no status` | Comprueba el nombre del archivo del workflow, la rama y el evento que lo activa |
| El número parece desactualizado | El origen, el proveedor del badge o el proxy de imágenes de GitHub pueden estar usando caché |
| El texto o el color son incorrectos | Comprueba los escapes `#` → `%23` y `-` literal → `--` |

Consulta la [guía completa de resolución de problemas](../BADGE_GUIDE.md#11-troubleshooting). El comprobador local de documentación es `python3 scripts/check_docs.py`; comprueba la estructura del repositorio, no la disponibilidad de servicios externos.

## Contribuciones y traducciones

Las contribuciones son bienvenidas: nuevos badges, logotipos corregidos, ejemplos más claros y traducciones. Lee [CONTRIBUTING.md](../../CONTRIBUTING.md), sigue el [Código de conducta](../../CODE_OF_CONDUCT.md) y notifica vulnerabilidades según [SECURITY.md](../../SECURITY.md).

El inglés es la versión de referencia. Este README está traducido íntegramente al español, portugués brasileño, ruso, chino simplificado y japonés mediante el selector de idiomas superior. El catálogo compartido y la guía detallada se mantienen en inglés; los nombres de marcas, las URL y los ejemplos de código son consistentes entre idiomas. Actualiza los seis archivos README al cambiar contenido compartido.

## Licencia

[MIT](../../LICENSE). Los servicios de badges, los nombres de marcas y los logotipos pertenecen a sus respectivos propietarios; su inclusión aquí no implica respaldo.
