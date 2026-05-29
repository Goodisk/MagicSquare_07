"""Boundary 응답 스키마."""

from __future__ import annotations

from typing import Final, Literal

from pydantic import BaseModel

INVALID_SIZE_CODE: Final[str] = "INVALID_SIZE"
INVALID_SIZE_MESSAGE: Final[str] = "Grid must be 4x4."


class FailureResponse(BaseModel):
    """입력 검증 실패 응답."""

    type: Literal["ERROR"]
    code: str
    message: str
