"""마방진 검증 — RED 스텁 (GREEN 구현 전)."""

from __future__ import annotations

from magic_square.entity.types import (
    ConditionResult,
    Grid,
    ValidationResult,
)


def _check_grid_size(grid: Grid) -> ConditionResult:
    return ConditionResult(
        name="wrong",
        passed=True,
        reason=None,
    )


def _check_number_set(grid: Grid) -> ConditionResult:
    return ConditionResult(name="wrong", passed=True, reason=None)


def _check_no_duplicate(grid: Grid) -> ConditionResult:
    return ConditionResult(name="wrong", passed=True, reason=None)


def _check_row_sums(grid: Grid) -> ConditionResult:
    return ConditionResult(name="wrong", passed=True, reason=None)


def _check_col_sums(grid: Grid) -> ConditionResult:
    return ConditionResult(name="wrong", passed=True, reason=None)


def _check_diag_sums(grid: Grid) -> ConditionResult:
    return ConditionResult(name="wrong", passed=True, reason=None)


def validate(grid: Grid) -> ValidationResult:
    """RED 스텁: 4x4이면 통과+실패목록, 아니면 무효 — 모든 validate 테스트가 실패."""
    if len(grid) == 4 and all(len(row) == 4 for row in grid):
        return ValidationResult(
            is_valid=True,
            failed_conditions=[
                ConditionResult(name="wrong", passed=False, reason=None),
            ],
        )
    return ValidationResult(is_valid=False, failed_conditions=[])
