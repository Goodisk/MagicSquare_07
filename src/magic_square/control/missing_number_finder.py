"""누락 숫자 탐색 — S-03 · D-MIS-01 (G-046~G-049)."""

from __future__ import annotations

from magic_square.entity.types import REQUIRED_NUMBERS, Grid


def find_missing_numbers(grid: Grid) -> list[int]:
    """격자에 등장하지 않는 1~16 숫자를 오름차순으로 반환한다."""
    return find_not_exist_nums(grid)


def find_not_exist_nums(grid: Grid) -> list[int]:
    """격자(0 제외)에 없는 1~16 숫자를 오름차순으로 반환한다."""
    present = {cell for row in grid for cell in row if cell != 0}
    return sorted(number for number in REQUIRED_NUMBERS if number not in present)
