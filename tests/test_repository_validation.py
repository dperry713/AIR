from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from scripts.validate_repository import validate_repository


VALID_MEC = """# MASTER ENGINEERING CONTRACT (MEC)

# 1. MISSION AND PRODUCT DEFINITION

# 3. NON-NEGOTIABLE ENGINEERING PRINCIPLES
"""


class ValidateRepositoryTests(unittest.TestCase):
    def write_valid_repository(self, root: Path) -> None:
        (root / "README.md").write_text(
            "# AIR\n\nProject specification: [MEC](MEC.md).\n",
            encoding="utf-8",
        )
        (root / "MEC.md").write_text(VALID_MEC, encoding="utf-8")

    def test_accepts_valid_minimal_repository(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self.write_valid_repository(root)
            self.assertEqual(validate_repository(root), [])

    def test_reports_missing_required_document(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "README.md").write_text("# AIR\nMEC.md\n", encoding="utf-8")
            errors = validate_repository(root)
            self.assertTrue(any("MEC.md" in error and "missing" in error for error in errors))

    def test_reports_empty_markdown_file(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self.write_valid_repository(root)
            (root / "docs").mkdir()
            (root / "docs" / "empty.md").write_text("  \n", encoding="utf-8")
            errors = validate_repository(root)
            self.assertTrue(any("Markdown file is empty: docs/empty.md" == error for error in errors))

    def test_reports_merge_conflict_markers(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self.write_valid_repository(root)
            (root / "MEC.md").write_text(
                VALID_MEC + "\n<<<<<<< current\nconflict\n=======\nother\n>>>>>>> incoming\n",
                encoding="utf-8",
            )
            errors = validate_repository(root)
            self.assertTrue(any("merge-conflict marker" in error for error in errors))
            self.assertTrue(any("merge-conflict separator" in error for error in errors))

    def test_reports_missing_required_mec_section(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self.write_valid_repository(root)
            (root / "MEC.md").write_text("# MASTER ENGINEERING CONTRACT (MEC)\n", encoding="utf-8")
            errors = validate_repository(root)
            self.assertTrue(any("MEC.md is missing required section" in error for error in errors))


if __name__ == "__main__":
    unittest.main()
