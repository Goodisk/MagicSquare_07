"""MagicSquare 도메인 엔티티 — RED 스텁 (GREEN 구현 전).

Entity 레이어 본 구현(상수·frozen dataclass)은 GREEN 단계에서 추가한다.
RED 단계에서는 Grid 타입 별칭과 Boundary 테스트용 최소 스텁만 둔다.
"""
from __future__ import annotations

from dataclasses import dataclass, field
from enum import StrEnum

type Grid = list[list[int]]
"""4x4 정수 격자. 행 우선(row-major) 순서로 표현된 2차원 리스트."""


class ValidationErrorCode(StrEnum):
    """입력 검증 오류 코드 — RED 스텁."""

    INVALID_SIZE = "INVALID_SIZE"


@dataclass
class InputValidationResult:
    """입력 검증 결과 — RED 스텁 (항상 통과 반환)."""

    is_valid: bool = True
    error_codes: list[ValidationErrorCode | str] = field(default_factory=list)


@dataclass
class ConditionResult:
    """단일 불변 조건 판정 — RED 스텁 (frozen·규약 미구현)."""

    name: str = ""
    passed: bool = True
    reason: str | None = None


@dataclass
class ValidationResult:
    """통합 판정 — RED 스텁 (항상 통과)."""

    is_valid: bool = True
    failed_conditions: list[ConditionResult] = field(default_factory=list)
