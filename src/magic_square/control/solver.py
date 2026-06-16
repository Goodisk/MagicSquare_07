"""마방진 Solver — S-05 · D-SOL-01~04 (G-050~G-054)."""

from __future__ import annotations

from magic_square.control.blank_finder import find_blank_coords
from magic_square.control.magic_square_validator import is_magic_square
from magic_square.control.missing_number_finder import find_not_exist_nums
from magic_square.control.validator import validate
from magic_square.entity.types import Grid


class UnsolvableDomainError(Exception):
    """두 조합 모두 마방진 완성 불가."""


def _fill_grid(grid: Grid, blanks: list[tuple[int, int]], values: list[int]) -> Grid:
    filled = [row[:] for row in grid]
    for (row_index, col_index), value in zip(blanks, values, strict=True):
        filled[row_index][col_index] = value
    return filled


def _try_assignments(
    grid: Grid,
    blanks: list[tuple[int, int]],
    missing: list[int],
) -> list[int] | None:
    ordered = sorted(missing)
    for assignment in (ordered, list(reversed(ordered))):
        filled = _fill_grid(grid, blanks, assignment)
        if is_magic_square(filled):
            row_a, col_a = blanks[0]
            row_b, col_b = blanks[1]
            return [
                row_a + 1,
                col_a + 1,
                assignment[0],
                row_b + 1,
                col_b + 1,
                assignment[1],
            ]
    return None


def solution(grid: Grid) -> list[int]:
    """Track B — 1-index 좌표 + 값 6-tuple payload."""
    blanks = find_blank_coords(grid)
    missing = find_not_exist_nums(grid)
    if len(blanks) != 2 or len(missing) != 2:
        raise UnsolvableDomainError("blank or missing count is not 2")
    result = _try_assignments(grid, blanks, missing)
    if result is None:
        raise UnsolvableDomainError("no valid assignment")
    return result


def solve(grid: Grid) -> Grid | None:
    """MVP — small-first 후 large-first fallback으로 완성 격자 반환."""
    blanks = find_blank_coords(grid)
    missing = find_not_exist_nums(grid)
    if len(blanks) != 2 or len(missing) != 2:
        return None
    ordered = sorted(missing)
    for assignment in (ordered, list(reversed(ordered))):
        filled = _fill_grid(grid, blanks, assignment)
        if validate(filled).is_valid:
            return filled
    return None


class SolvePartialMagicSquare:
    """Domain bridge — UIBoundary에서 호출."""

    def execute(self, grid: Grid) -> list[int]:
        return solution(grid)
