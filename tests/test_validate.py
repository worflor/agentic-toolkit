"""Regression checks for the repository's small validation script."""

from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from scripts.validate import link_errors, skill_errors, validate


class SkillValidationTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temporary = tempfile.TemporaryDirectory()
        self.root = Path(self.temporary.name)
        self.folder = self.root / "skills" / "sample-skill"
        self.folder.mkdir(parents=True)
        self.entry = self.folder / "SKILL.md"

    def tearDown(self) -> None:
        self.temporary.cleanup()

    def write_skill(self, name: str = "sample-skill", description: str = "Do the work.") -> None:
        self.entry.write_text(
            f"---\nname: {name}\ndescription: >-\n  {description}\n---\n\n# Method\n",
            encoding="utf-8",
        )

    def test_valid_skill_and_folded_description(self) -> None:
        self.write_skill()
        self.assertEqual(skill_errors(self.entry), [])

    def test_name_must_match_directory(self) -> None:
        self.write_skill(name="other-skill")
        self.assertTrue(any("name must match" in error for error in skill_errors(self.entry)))

    def test_description_is_required(self) -> None:
        self.write_skill(description="")
        self.assertTrue(any("description" in error for error in skill_errors(self.entry)))

    def test_local_links_and_fenced_examples(self) -> None:
        document = self.root / "README.md"
        (self.root / "named doc.md").write_text("Hello", encoding="utf-8")
        document.write_text(
            "[Good](named%20doc.md)\n"
            + chr(96) * 3 + "md\n"
            "[Not a real link](does-not-exist.md)\n"
            + chr(96) * 3 + "\n"
            "[Missing](missing.md)\n",
            encoding="utf-8",
        )
        errors, count = link_errors(self.root, document)
        self.assertEqual(count, 2)
        self.assertEqual(len(errors), 1)
        self.assertIn("missing.md", errors[0])

    def test_full_repository_validation(self) -> None:
        self.write_skill()
        (self.root / "README.md").write_text("[Skill](skills/sample-skill/SKILL.md)", encoding="utf-8")
        (self.root / "AGENTS.md").write_text("# Agents", encoding="utf-8")
        (self.root / "LICENSE").write_text("Example", encoding="utf-8")
        errors, skills, documents, links = validate(self.root)
        self.assertEqual(errors, [])
        self.assertEqual((skills, documents, links), (1, 3, 1))


if __name__ == "__main__":
    unittest.main()
