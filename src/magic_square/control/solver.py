"""마방진 Solver — RED 스텁 (GREEN 구현 전)."""

from __future__ import annotations

from magic_square.entity.types import Grid


def solve(grid: Grid) -> Grid | None:
    """RED 스텁: 항상 잘못된 격자 반환 (None·4x4 성공 케이스 모두 실패)."""
    return [[0]]
