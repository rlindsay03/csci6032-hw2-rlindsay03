import json
import subprocess
import sys
import unittest
from pathlib import Path
from tempfile import TemporaryDirectory


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "src" / "text_stats.py"


class TextStatsTests(unittest.TestCase):
    def test_text_stats_counts_lines_words_and_characters(self):
        from src.text_stats import text_stats

        with TemporaryDirectory() as temporary_directory:
            path = Path(temporary_directory) / "input.txt"
            path.write_text("Hello, world!\nCafé\n", encoding="utf-8")

            self.assertEqual(
                text_stats(path),
                {"lines": 2, "words": 3, "characters": 19},
            )

    def test_text_stats_reports_case_insensitive_top_words_with_tie_breaking(self):
        from src.text_stats import text_stats

        with TemporaryDirectory() as temporary_directory:
            path = Path(temporary_directory) / "input.txt"
            path.write_text("Beta alpha ALPHA beta gamma", encoding="utf-8")

            self.assertEqual(
                text_stats(path, top=3),
                {
                    "lines": 1,
                    "words": 5,
                    "characters": 27,
                    "top": [
                        {"word": "alpha", "count": 2},
                        {"word": "beta", "count": 2},
                        {"word": "gamma", "count": 1},
                    ],
                },
            )

    def test_command_outputs_json_for_sample_file(self):
        result = subprocess.run(
            [sys.executable, str(SCRIPT), str(ROOT / "sample.txt")],
            capture_output=True,
            check=True,
            text=True,
        )

        self.assertEqual(
            json.loads(result.stdout),
            {"lines": 5, "words": 14, "characters": 66},
        )

    def test_command_top_option_outputs_requested_number_of_words(self):
        result = subprocess.run(
            [
                sys.executable,
                str(SCRIPT),
                str(ROOT / "sample.txt"),
                "--top",
                "2",
            ],
            capture_output=True,
            check=True,
            text=True,
        )

        self.assertEqual(
            json.loads(result.stdout)["top"],
            [
                {"word": "67", "count": 1},
                {"word": "beat", "count": 1},
            ],
        )


if __name__ == "__main__":
    unittest.main()
