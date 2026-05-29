"""Boundary 입력 검증 — AC-FR-01-01 GREEN (grid is None만)."""

from __future__ import annotations

from boundary.schemas import (
    INVALID_SIZE_CODE,
    INVALID_SIZE_MESSAGE,
    FailureResponse,
)
from magic_square.entity.types import Grid


class InputValidator:
    """격자 입력 형식·크기 검증 (Boundary)."""

    def validate(self, grid: Grid | None) -> FailureResponse:
        """grid가 None이면 INVALID_SIZE 실패 응답을 반환한다."""
        if grid is None:
            return FailureResponse(
                type="ERROR",
                code=INVALID_SIZE_CODE,
                message=INVALID_SIZE_MESSAGE,
            )
        raise NotImplementedError
