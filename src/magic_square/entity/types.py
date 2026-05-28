"""MagicSquare 도메인 엔티티 타입 정의.

ECB 아키텍처의 Entity 레이어.
순수 도메인 데이터 구조와 상수만 포함한다.
비즈니스 로직, 조건 분기, 다른 레이어 import를 포함하지 않는다.
"""
from __future__ import annotations

from dataclasses import dataclass, field
from typing import Final

# ---------------------------------------------------------------------------
# 도메인 상수
# ---------------------------------------------------------------------------

GRID_SIZE: Final[int] = 4
"""4x4 격자의 행·열 크기."""

TARGET_SUM: Final[int] = 34
"""각 행, 열, 대각선의 기준 합 (136 ÷ 4)."""

REQUIRED_NUMBERS: Final[frozenset[int]] = frozenset(range(1, 17))
"""격자에 정확히 한 번씩 존재해야 하는 숫자 집합 (1~16)."""

# ---------------------------------------------------------------------------
# 타입 별칭
# ---------------------------------------------------------------------------

type Grid = list[list[int]]
"""4x4 정수 격자. 행 우선(row-major) 순서로 표현된 2차원 리스트."""

# ---------------------------------------------------------------------------
# 도메인 데이터 클래스
# ---------------------------------------------------------------------------


@dataclass(frozen=True)
class ConditionResult:
    """단일 불변 조건의 판정 결과.

    frozen=True로 선언하여 생성 후 변경을 금지한다.
    조건의 판정 결과는 불변이어야 한다.

    Attributes:
        name: 불변 조건 이름 (예: "격자 크기", "행 합").
        passed: 해당 조건 통과 여부.
        reason: 실패 사유. 통과 시 None, 실패 시 사람이 읽을 수 있는 설명.

    Examples:
        >>> result = ConditionResult(name="격자 크기", passed=True)
        >>> result.passed
        True
        >>> result.reason is None
        True

        >>> failed = ConditionResult(
        ...     name="행 합",
        ...     passed=False,
        ...     reason="1번 행의 합이 34가 아님 (실제: 33)",
        ... )
        >>> failed.passed
        False
    """

    name: str
    passed: bool
    reason: str | None = None


@dataclass(frozen=True)
class ValidationResult:
    """7개 불변 조건 전체에 대한 통합 판정 결과.

    완성의 불가분성 원칙:
    failed_conditions에 항목이 하나라도 있으면 is_valid는 반드시 False이다.

    frozen=True로 선언하여 생성 후 변경을 금지한다.
    단, failed_conditions 리스트의 내부 변경은 Python 제약으로 막을 수 없다.

    Attributes:
        is_valid: 7개 조건 모두 통과 시에만 True.
        failed_conditions: 실패한 조건들의 목록. 모두 통과 시 빈 리스트.

    Examples:
        >>> result = ValidationResult(is_valid=True)
        >>> result.is_valid
        True
        >>> result.failed_conditions
        []

        >>> failed = ConditionResult(name="행 합", passed=False, reason="...")
        >>> invalid = ValidationResult(is_valid=False, failed_conditions=[failed])
        >>> invalid.is_valid
        False
        >>> len(invalid.failed_conditions)
        1
    """

    is_valid: bool
    failed_conditions: list[ConditionResult] = field(default_factory=list)
