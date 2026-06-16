"""빈칸 탐색 — S-02 · D-LOC-01 (G-042~G-045)."""

from __future__ import annotations

from magic_square.entity.types import Grid


def find_blanks(grid: Grid) -> list[tuple[int, int]]:
    """0(빈칸) 좌표를 row-major 순서로 반환한다."""
    return find_blank_coords(grid)


def find_blank_coords(grid: Grid) -> list[tuple[int, int]]:
    """0(빈칸) 좌표를 row-major 0-index (row, col)로 반환한다."""
    coordinates: list[tuple[int, int]] = []
    for row_index, row in enumerate(grid):
        for col_index, cell in enumerate(row):
            if cell == 0:
                coordinates.append((row_index, col_index))
    return coordinates
