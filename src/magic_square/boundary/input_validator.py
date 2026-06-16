"""입력 검증 — AC-FR-01-01 · S-01 (G-017~G-032)."""

from __future__ import annotations

from typing import Final

from magic_square.boundary.envelopes import FailureEnvelope, SuccessEnvelope
from magic_square.entity.types import (
    GRID_SIZE,
    REQUIRED_NUMBERS,
    Grid,
    InputValidationResult,
    ValidationErrorCode,
)

REQUIRED_BLANK_COUNT: Final[int] = 2
MIN_CELL_VALUE: Final[int] = min(REQUIRED_NUMBERS)
MAX_CELL_VALUE: Final[int] = max(REQUIRED_NUMBERS)

ERROR_OUT_OF_RANGE: Final[str] = "E004"
ERROR_DUPLICATE: Final[str] = "E005"
ERROR_BLANK_COUNT: Final[str] = "E002"


def _check_blank_count(grid: Grid) -> None:
    """빈칸 수 검증 — size 통과 후에만 호출."""
    blank_count = sum(1 for row in grid for cell in row if cell == 0)
    if blank_count != REQUIRED_BLANK_COUNT:
        raise ValueError("blank_count")


def _is_valid_grid_size(grid: Grid) -> bool:
    if len(grid) != GRID_SIZE:
        return False
    return all(len(row) == GRID_SIZE for row in grid)


def _collect_input_errors(grid: Grid) -> list[ValidationErrorCode | str]:
    errors: list[ValidationErrorCode | str] = []
    if not _is_valid_grid_size(grid):
        return [ValidationErrorCode.INVALID_SIZE, "grid_size"]

    blank_count = sum(1 for row in grid for cell in row if cell == 0)
    if blank_count != REQUIRED_BLANK_COUNT:
        errors.append("blank_count")

    values = [cell for row in grid for cell in row if cell != 0]
    if len(values) != len(set(values)):
        errors.append("duplicate")

    for cell in values:
        if cell < MIN_CELL_VALUE or cell > MAX_CELL_VALUE:
            errors.append("out_of_range")
            break

    return errors


def validate_input(grid: Grid) -> InputValidationResult:
    """격자 입력 검증 — 크기·빈칸·중복·범위."""
    errors = _collect_input_errors(grid)
    if errors:
        return InputValidationResult(is_valid=False, error_codes=errors)
    return InputValidationResult(is_valid=True, error_codes=[])


class InputValidator:
    """Track A 입력 검증 — Failure/Success envelope."""

    def validate(self, matrix: Grid) -> FailureEnvelope | SuccessEnvelope:
        if not _is_valid_grid_size(matrix):
            return FailureEnvelope(code=ValidationErrorCode.INVALID_SIZE)

        blank_count = sum(1 for row in matrix for cell in row if cell == 0)
        if blank_count != REQUIRED_BLANK_COUNT:
            return FailureEnvelope(code=ERROR_BLANK_COUNT)

        values = [cell for row in matrix for cell in row if cell != 0]
        if len(values) != len(set(values)):
            return FailureEnvelope(code=ERROR_DUPLICATE)

        for cell in values:
            if cell < MIN_CELL_VALUE or cell > MAX_CELL_VALUE:
                return FailureEnvelope(code=ERROR_OUT_OF_RANGE)

        return SuccessEnvelope()
