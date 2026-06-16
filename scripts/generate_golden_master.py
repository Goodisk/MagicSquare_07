#!/usr/bin/env python3
"""Magic Square Solver Golden Master 기준 파일 생성 스크립트.

현재 Solver(UIBoundary) 출력을 캡처하여 tests/golden_master_expected.txt 를 갱신한다.

Usage:
    python scripts/generate_golden_master.py
    python scripts/generate_golden_master.py --output tests/golden_master_expected.txt
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJECT_ROOT / "src"))
sys.path.insert(0, str(PROJECT_ROOT))

from tests.golden_master.support import (  # noqa: E402
    GOLDEN_MASTER_PATH,
    write_golden_master,
)


def main() -> int:
    """Golden Master 기준 파일을 생성하고 경로를 stdout에 출력한다."""
    parser = argparse.ArgumentParser(
        description="Magic Square Solver Golden Master 기준 파일 생성",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=GOLDEN_MASTER_PATH,
        help=f"출력 경로 (기본: {GOLDEN_MASTER_PATH})",
    )
    args = parser.parse_args()

    output_path = write_golden_master(args.output)
    print(f"Golden Master 기준 파일 생성: {output_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
