"""UI Boundary — Track A U-FLOW / U-OUT."""

from __future__ import annotations

from magic_square.boundary.envelopes import FailureEnvelope, SuccessEnvelope
from magic_square.boundary.input_validator import InputValidator
from magic_square.control.solver import SolvePartialMagicSquare
from magic_square.entity.types import Grid


class UIBoundary:
    """입력 검증 후 Domain execute를 호출하는 Boundary."""

    def __init__(self) -> None:
        self._validator = InputValidator()
        self._solver = SolvePartialMagicSquare()

    def solve(self, matrix: Grid) -> FailureEnvelope | SuccessEnvelope:
        validation = self._validator.validate(matrix)
        if isinstance(validation, FailureEnvelope):
            return validation
        payload = self._solver.execute(matrix)
        return SuccessEnvelope(payload=payload)
