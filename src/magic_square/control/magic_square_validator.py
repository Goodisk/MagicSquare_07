"""완성 격자 마방진 판정 — D-VAL-01~06."""

from __future__ import annotations

from magic_square.control.validator import validate
from magic_square.entity.types import Grid


def is_magic_square(grid: Grid) -> bool:
    """완성 격자가 마방진 불변 조건을 모두 만족하는지 판정한다."""
    if any(cell == 0 for row in grid for cell in row):
        return False
    return validate(grid).is_valid
