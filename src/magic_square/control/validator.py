"""마방진 검증 — MVP INV-1~7 (G-033~G-041)."""

from __future__ import annotations

from magic_square.entity.types import (
    GRID_SIZE,
    REQUIRED_NUMBERS,
    TARGET_SUM,
    ConditionResult,
    Grid,
    ValidationResult,
)


def _check_grid_size(grid: Grid) -> ConditionResult:
    name = "격자 크기"
    if len(grid) != GRID_SIZE or any(len(row) != GRID_SIZE for row in grid):
        return ConditionResult(
            name=name,
            passed=False,
            reason="행 또는 열의 수가 4가 아님",
        )
    return ConditionResult(name=name, passed=True)


def _check_number_set(grid: Grid) -> ConditionResult:
    name = "숫자 집합"
    values = {cell for row in grid for cell in row if cell != 0}
    if not values.issubset(REQUIRED_NUMBERS):
        return ConditionResult(
            name=name,
            passed=False,
            reason="허용되지 않는 숫자 포함 또는 필수 숫자 누락",
        )
    if 0 not in {cell for row in grid for cell in row} and values != set(
        REQUIRED_NUMBERS
    ):
        return ConditionResult(
            name=name,
            passed=False,
            reason="허용되지 않는 숫자 포함 또는 필수 숫자 누락",
        )
    return ConditionResult(name=name, passed=True)


def _check_no_duplicate(grid: Grid) -> ConditionResult:
    name = "중복 금지"
    values = [cell for row in grid for cell in row if cell != 0]
    seen: set[int] = set()
    duplicates: set[int] = set()
    for value in values:
        if value in seen:
            duplicates.add(value)
        seen.add(value)
    if duplicates:
        dup_list = ", ".join(str(n) for n in sorted(duplicates))
        return ConditionResult(
            name=name,
            passed=False,
            reason=f"중복 숫자 존재: [{dup_list}]",
        )
    return ConditionResult(name=name, passed=True)


def _check_row_sums(grid: Grid) -> ConditionResult:
    name = "행 합"
    for index, row in enumerate(grid, start=1):
        row_sum = sum(row)
        if row_sum != TARGET_SUM:
            return ConditionResult(
                name=name,
                passed=False,
                reason=f"{index}번 행의 합이 {TARGET_SUM}가 아님 (실제: {row_sum})",
            )
    return ConditionResult(name=name, passed=True)


def _check_col_sums(grid: Grid) -> ConditionResult:
    name = "열 합"
    for index in range(GRID_SIZE):
        col_sum = sum(grid[row][index] for row in range(GRID_SIZE))
        if col_sum != TARGET_SUM:
            return ConditionResult(
                name=name,
                passed=False,
                reason=f"{index + 1}번 열의 합이 {TARGET_SUM}가 아님 (실제: {col_sum})",
            )
    return ConditionResult(name=name, passed=True)


def _check_diag_sums(grid: Grid) -> ConditionResult:
    name = "대각선 합"
    anti_diag = sum(grid[i][GRID_SIZE - 1 - i] for i in range(GRID_SIZE))
    if anti_diag != TARGET_SUM:
        return ConditionResult(
            name=name,
            passed=False,
            reason=f"반 대각선의 합이 {TARGET_SUM}가 아님 (실제: {anti_diag})",
        )
    main_diag = sum(grid[i][i] for i in range(GRID_SIZE))
    if main_diag != TARGET_SUM:
        return ConditionResult(
            name=name,
            passed=False,
            reason=f"주 대각선의 합이 {TARGET_SUM}가 아님 (실제: {main_diag})",
        )
    return ConditionResult(name=name, passed=True)


def validate(grid: Grid) -> ValidationResult:
    """7개 불변 조건 통합 판정."""
    checks = [
        _check_grid_size,
        _check_number_set,
        _check_no_duplicate,
        _check_row_sums,
        _check_col_sums,
        _check_diag_sums,
    ]
    failed = [result for check in checks if not (result := check(grid)).passed]
    return ValidationResult(
        is_valid=len(failed) == 0,
        failed_conditions=failed,
    )
