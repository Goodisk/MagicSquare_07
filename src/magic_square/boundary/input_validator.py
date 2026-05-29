"""입력 검증 — RED 스텁 (GREEN 구현 전)."""

from __future__ import annotations

from magic_square.entity.types import (
    GRID_SIZE,
    Grid,
    InputValidationResult,
    ValidationErrorCode,
)


def _check_blank_count(grid: Grid) -> None:
    """빈칸 수 검증 — GREEN 단계에서 구현."""
    raise NotImplementedError


def validate_input(grid: Grid) -> InputValidationResult:
    """입력 검증 — GREEN: 비 4×4 격자 시 INVALID_SIZE (G-017~G-022)."""
    if len(grid) != GRID_SIZE:
        return InputValidationResult(
            is_valid=False,
            error_codes=[ValidationErrorCode.INVALID_SIZE],
        )
    if any(len(row) != GRID_SIZE for row in grid):
        return InputValidationResult(
            is_valid=False,
            error_codes=[ValidationErrorCode.INVALID_SIZE],
        )

    return InputValidationResult(
        is_valid=True,
        error_codes=[],
    )
