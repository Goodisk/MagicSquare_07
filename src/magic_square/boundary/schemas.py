"""Boundary 입력 스키마 — AC-FR-01-01 GridInputSchema (G-024)."""

from __future__ import annotations

from typing import Final

from pydantic import BaseModel, Field, field_validator

from magic_square.entity.types import GRID_SIZE

FLAT_CELL_COUNT: Final[int] = GRID_SIZE * GRID_SIZE


class GridInputSchema(BaseModel):
    """flat 입력 — 16칸(4×4) 고정."""

    cells: list[int] = Field(...)

    @field_validator("cells")
    @classmethod
    def validate_cell_count(cls, cells: list[int]) -> list[int]:
        if len(cells) != FLAT_CELL_COUNT:
            raise ValueError("INVALID_SIZE")
        return cells
