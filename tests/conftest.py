"""pytest 공유 fixture 정의.

scope 규칙:
- function (기본값): 상태 격리가 필요한 대부분의 테스트에 사용
- module: 같은 파일 내 읽기 전용 공유 데이터
- session: 초기화 비용이 큰 외부 의존성 (현재 없음)
"""
import pytest

from magic_square.entity.types import Grid


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
def invalid_grid_five_rows() -> Grid:
    """행이 5개인 비정상 격자 (AC-FR-01-01 INVALID_SIZE)."""
    return [
        [16,  3,  2, 13],
        [ 5, 10, 11,  8],
        [ 9,  6,  7, 12],
        [ 4, 15, 14,  1],
        [ 1,  2,  3,  4],
    ]


@pytest.fixture
def invalid_grid_empty() -> Grid:
    """행이 0개인 빈 격자 (AC-FR-01-01 INVALID_SIZE)."""
    return []


@pytest.fixture
def invalid_grid_jagged_rows() -> Grid:
    """행마다 열 수가 다른 비정형 격자 (AC-FR-01-01 INVALID_SIZE)."""
    return [
        [16,  3,  2, 13],
        [ 5, 10, 11],
        [ 9,  6,  7, 12,  0],
        [ 4, 15, 14,  1],
    ]


@pytest.fixture
def invalid_grid_missing_number() -> Grid:
    """숫자 7이 누락되고 17이 포함된 격자 (숫자 집합 조건 위반)."""
    return [
        [16,  3,  2, 13],
        [ 5, 10, 11,  8],
        [ 9,  6, 17, 12],
        [ 4, 15, 14,  1],
    ]


@pytest.fixture
def invalid_grid_duplicate_number() -> Grid:
    """숫자 5가 중복 등장하는 격자 (중복 금지 조건 위반)."""
    return [
        [16,  3,  2, 13],
        [ 5, 10,  5,  8],
        [ 9,  6,  7, 12],
        [ 4, 15, 14,  1],
    ]


@pytest.fixture
def invalid_grid_wrong_row_sum() -> Grid:
    """1번 행 합이 33인 격자 (행 합 조건 위반)."""
    return [
        [16,  3,  2, 12],
        [ 5, 10, 11,  8],
        [ 9,  6,  7, 12],
        [ 4, 15, 14,  1],
    ]


@pytest.fixture
def invalid_grid_wrong_col_sum() -> Grid:
    """3번 열 합이 35인 격자 (열 합 조건 위반)."""
    return [
        [16,  3,  2, 13],
        [ 5, 10, 11,  8],
        [ 9,  6,  8, 12],
        [ 4, 15, 14,  1],
    ]


@pytest.fixture
def invalid_grid_wrong_diagonal_sum() -> Grid:
    """반 대각선 합이 34가 아닌 격자 (대각선 합 조건 위반)."""
    return [
        [16,  3,  2, 13],
        [ 5, 10, 11,  8],
        [ 9,  6,  7, 12],
        [ 4, 15, 14,  2],
    ]


@pytest.fixture
def grid_two_blanks() -> Grid:
    """빈칸 2개(값 0)인 4x4 격자 — Solver·BlankFinder용."""
    return [
        [16,  3,  2, 13],
        [ 5, 10, 11,  8],
        [ 9,  6,  0, 12],
        [ 4, 15,  0,  1],
    ]


@pytest.fixture
def grid_one_blank() -> Grid:
    """빈칸 1개인 4x4 격자 (입력 검증 위반)."""
    return [
        [16,  3,  2, 13],
        [ 5, 10, 11,  8],
        [ 9,  6,  0, 12],
        [ 4, 15, 14,  1],
    ]


@pytest.fixture
def grid_three_blanks() -> Grid:
    """빈칸 3개인 4x4 격자 (입력 검증 위반)."""
    return [
        [16,  3,  2, 13],
        [ 5, 10, 11,  8],
        [ 9,  6,  0, 12],
        [ 4, 15,  0,  0],
    ]


@pytest.fixture
def grid_four_blanks() -> Grid:
    """빈칸 4개인 4x4 격자 (입력 검증 위반)."""
    return [
        [16,  3,  0, 13],
        [ 5, 10,  0,  8],
        [ 9,  6,  0, 12],
        [ 4, 15,  0,  1],
    ]


@pytest.fixture
def grid_with_duplicate_and_two_blanks() -> Grid:
    """빈칸 2개·숫자 5 중복 격자 (입력 검증 위반)."""
    return [
        [16,  3,  2, 13],
        [ 5, 10,  5,  8],
        [ 9,  6,  0, 12],
        [ 4, 15,  0,  1],
    ]


@pytest.fixture
def grid_with_value_above_max() -> Grid:
    """17 포함·빈칸 2개 격자 (입력 검증 위반)."""
    return [
        [16,  3,  2, 13],
        [ 5, 10, 11,  8],
        [ 9,  6,  0, 12],
        [ 4, 15,  0, 17],
    ]


@pytest.fixture
def grid_with_value_below_min() -> Grid:
    """-1 포함·빈칸 2개 격자 (입력 검증 위반)."""
    return [
        [16,  3,  2, 13],
        [ 5, 10, 11,  8],
        [ 9,  6,  0, 12],
        [ 4, 15,  0, -1],
    ]


@pytest.fixture
def grid_three_blanks_for_finder() -> Grid:
    """빈칸 3개 격자 — BlankFinder AC-02-5용."""
    return [
        [16,  3,  2, 13],
        [ 5, 10, 11,  8],
        [ 9,  6,  0, 12],
        [ 4,  0,  0,  1],
    ]


@pytest.fixture
def grid_duplicate_for_missing_finder() -> Grid:
    """중복 포함·빈칸 2개 격자 — MissingNumberFinder AC-03-5용."""
    return [
        [16,  3,  2, 13],
        [ 5, 10,  5,  8],
        [ 9,  6,  0, 12],
        [ 4, 15,  0,  1],
    ]


@pytest.fixture
def grid_unsolvable_two_blanks() -> Grid:
    """두 조합 모두 마방진 완성 불가 격자 — Solver SC-DOM-SOL-003용."""
    return [
        [ 1,  2,  3,  4],
        [ 5,  6,  0,  8],
        [ 9, 10, 11, 12],
        [13, 14,  0, 16],
    ]
