"""Count lines, words, and characters in a UTF-8 text file."""

import argparse
import json
from pathlib import Path
from typing import Dict, List, Optional


def text_stats(path: Path, top: Optional[int] = None) -> Dict[str, object]:
    """Return line, word, and character counts for a UTF-8 text file."""
    text = path.read_text(encoding="utf-8")
    stats: Dict[str, object] = {
        "lines": len(text.splitlines()),
        "words": len(text.split()),
        "characters": len(text),
    }
    if top is not None:
        word_counts: Dict[str, int] = {}
        for word in text.split():
            normalized_word = word.casefold()
            word_counts[normalized_word] = word_counts.get(normalized_word, 0) + 1

        most_frequent: List[Dict[str, object]] = [
            {"word": word, "count": count}
            for word, count in sorted(
                word_counts.items(), key=lambda item: (-item[1], item[0])
            )[:top]
        ]
        stats["top"] = most_frequent
    return stats


def nonnegative_int(value: str) -> int:
    """Parse a non-negative integer for an argparse option."""
    parsed = int(value)
    if parsed < 0:
        raise argparse.ArgumentTypeError("must be non-negative")
    return parsed


def main() -> None:
    """Parse the command line and print file statistics as JSON."""
    parser = argparse.ArgumentParser(
        description="Count lines, words, and characters in a UTF-8 text file."
    )
    parser.add_argument("file", type=Path, help="path to the UTF-8 text file")
    parser.add_argument(
        "--top",
        type=nonnegative_int,
        metavar="N",
        help="include the N most frequent words, case-insensitively",
    )
    args = parser.parse_args()
    print(json.dumps(text_stats(args.file, top=args.top)))


if __name__ == "__main__":
    main()
