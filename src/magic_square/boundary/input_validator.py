"""입력 검증 — RED 스텁 (GREEN 구현 전)."""

from __future__ import annotations

from magic_square.entity.types import Grid, InputValidationResult


def _check_blank_count(grid: Grid) -> None:
    """빈칸 수 검증 — GREEN 단계에서 구현."""
    raise NotImplementedError


def validate_input(grid: Grid) -> InputValidationResult:
    """RED 스텁: 항상 통과·오류 없음을 반환하여 검증 실패 테스트가 통과하지 않게 한다."""
    from magic_square.entity.types import ValidationErrorCode

    return InputValidationResult(
        is_valid=True,
        error_codes=[ValidationErrorCode.INVALID_SIZE],
    )
