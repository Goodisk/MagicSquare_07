"""Boundary 응답 envelope — Track A U-IN / U-FLOW / U-OUT."""

from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(frozen=True)
class FailureEnvelope:
    """입력·처리 실패 응답."""

    success: bool = False
    code: str = ""


@dataclass(frozen=True)
class SuccessEnvelope:
    """입력 검증 통과 응답."""

    success: bool = True
    payload: list[int] = field(default_factory=list)
