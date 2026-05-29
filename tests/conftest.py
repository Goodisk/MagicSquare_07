"""pytest 공유 fixture 정의.

scope 규칙:
- function (기본값): 상태 격리가 필요한 대부분의 테스트에 사용
- module: 같은 파일 내 읽기 전용 공유 데이터
- session: 초기화 비용이 큰 외부 의존성 (현재 없음)
"""
import pytest

from magic_square.entity.types import ConditionResult, Grid, ValidationResult


@pytest.fixture
def valid_magic_square() -> Grid:
    """완전한 4x4 마방진 격자 (모든 불변 조건 충족).

    행·열·대각선 합 = 34, 숫자 1~16 각 1회 등장.
    """
    return [
        [16,  3,  2, 13],
        [ 5, 10, 11,  8],
        [ 9,  6,  7, 12],
        [ 4, 15, 14,  1],
    ]


@pytest.fixture
def invalid_grid_wrong_row_count() -> Grid:
    """행이 3개인 비정상 격자 (격자 크기 조건 위반)."""
    return [
        [16,  3,  2, 13],
        [ 5, 10, 11,  8],
        [ 9,  6,  7, 12],
    ]


@pytest.fixture
def invalid_grid_wrong_col_count() -> Grid:
    """열이 5개인 비정상 격자 (격자 크기 조건 위반)."""
    return [
        [16,  3,  2, 13,  0],
        [ 5, 10, 11,  8,  0],
        [ 9,  6,  7, 12,  0],
        [ 4, 15, 14,  1,  0],
    ]


@pytest.fixture
def passed_condition() -> ConditionResult:
    """통과 상태의 ConditionResult."""
    return ConditionResult(name="격자 크기", passed=True)


@pytest.fixture
def failed_condition() -> ConditionResult:
    """실패 상태의 ConditionResult."""
    return ConditionResult(
        name="행 합",
        passed=False,
        reason="1번 행의 합이 34가 아님 (실제: 33)",
    )


@pytest.fixture
def valid_validation_result() -> ValidationResult:
    """모든 조건 통과 상태의 ValidationResult."""
    return ValidationResult(is_valid=True)


@pytest.fixture
def invalid_validation_result(failed_condition: ConditionResult) -> ValidationResult:
    """하나 이상의 조건 실패 상태의 ValidationResult."""
    return ValidationResult(is_valid=False, failed_conditions=[failed_condition])
