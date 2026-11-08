"""Regression tests for the offline documentation checker (stdlib only)."""
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import check_docs


class DocumentationCheckerTests(unittest.TestCase):
    def test_colors(self):
        for color in ("brightgreen", "orange", "3776AB", "%233776AB", "#fff", "inactive"):
            self.assertTrue(check_docs.valid_color(color), color)
        for color in ("%23Clojure", "not-a-color", "#12GGFF", ""):
            self.assertFalse(check_docs.valid_color(color), color)

    def test_multilingual_anchors(self):
        cases = {
            "## Inicio rápido": "inicio-rápido",
            "## Быстрый старт": "быстрый-старт",
            "## GitHub Markdown 提示框": "github-markdown-提示框",
            "## クイックスタート": "クイックスタート",
            '## Tools & Editors': "tools--editors",
        }
        for heading, anchor in cases.items():
            self.assertIn(anchor, check_docs.heading_anchors(heading))

    def test_explicit_anchor(self):
        self.assertIn("stable-id", check_docs.heading_anchors('<a id="stable-id"></a>\n\n## 🛠️ Tools'))

    def test_inline_template_is_not_a_local_link(self):
        text = "`[![alt](image-url)](destination-url)`"
        self.assertEqual([], check_docs.local_destinations(text))

    def test_linked_image_destination_is_checked(self):
        text = "[![License](https://img.shields.io/github/license/a/b)](LICENSE)"
        self.assertIn("LICENSE", check_docs.local_destinations(text))

    def test_fenced_template_is_not_navigation(self):
        text = "```markdown\n[example](MISSING.md)\n```\n[real](README.md)"
        self.assertEqual(["README.md"], check_docs.local_destinations(text))

    def test_bad_static_color_is_reported(self):
        errors = []
        text = "![Test](https://img.shields.io/badge/Test-%23Clojure?style=for-the-badge)"
        check_docs.check_catalog(text, None, errors)
        self.assertTrue(any("invalid color" in error for error in errors))
        self.assertTrue(any("count mismatch" in error for error in errors))

    def test_unknown_logo_is_reported(self):
        errors = []
        text = "**1 copy-paste Markdown badges**\n\n![Test](https://img.shields.io/badge/Test-blue?style=for-the-badge&logo=not-a-real-logo)"
        check_docs.check_catalog(text, {"python"}, errors)
        self.assertTrue(any("unknown current Simple Icons slug" in error for error in errors))

    def test_translation_fences_are_exact(self):
        self.assertEqual(["a\n"], check_docs.fenced_blocks("```markdown\na\n```\n"))
        self.assertNotEqual(check_docs.fenced_blocks("```\na\n```"), check_docs.fenced_blocks("```\nb\n```"))


if __name__ == "__main__":
    unittest.main()
