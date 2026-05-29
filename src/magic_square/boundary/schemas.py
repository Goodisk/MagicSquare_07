"""Boundary 입력 스키마 — RED 스텁 (GREEN 구현 전)."""

from __future__ import annotations

from pydantic import BaseModel, Field


class GridInputSchema(BaseModel):
    """flat 입력 — RED 스텁: 잘못된 길이도 허용하여 스키마 테스트가 실패한다."""

    cells: list[int] = Field(default_factory=lambda: list(range(1, 17)))
