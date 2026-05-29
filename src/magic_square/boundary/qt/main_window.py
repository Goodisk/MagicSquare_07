"""Qt Boundary — 4×4 마방진 Solver 메인 윈도우."""

from __future__ import annotations

from typing import Final

from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont
from PyQt6.QtWidgets import (
    QGridLayout,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QMainWindow,
    QMessageBox,
    QPushButton,
    QVBoxLayout,
    QWidget,
)

from magic_square.boundary.envelopes import FailureEnvelope, SuccessEnvelope
from magic_square.boundary.qt.adapter import (
    apply_solution_payload,
    cells_to_grid,
    format_error_message,
    format_solution_message,
    generate_random_puzzle,
    grid_to_cell_texts,
)
from magic_square.boundary.ui_boundary import UIBoundary
from magic_square.control.solver import UnsolvableDomainError
from magic_square.entity.types import GRID_SIZE, Grid

CELL_SIZE: Final[int] = 56


class MainWindow(QMainWindow):
    """4×4 격자 입력 및 Solver 호출 UI."""

    def __init__(self) -> None:
        super().__init__()
        self._boundary = UIBoundary()
        self._cells: list[list[QLineEdit]] = []
        self._status_label = QLabel("초기화로 새 문제를 만들고 풀기를 눌러 완성하세요.")
        self._status_label.setWordWrap(True)
        self._build_ui()
        self._reset_puzzle()

    def _build_ui(self) -> None:
        self.setWindowTitle("Magic Square 4×4 Solver")
        self.setMinimumSize(420, 380)

        central = QWidget()
        self.setCentralWidget(central)
        root = QVBoxLayout(central)
        root.setSpacing(12)

        title = QLabel("4×4 Magic Square")
        title_font = QFont()
        title_font.setPointSize(14)
        title_font.setBold(True)
        title.setFont(title_font)
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        root.addWidget(title)

        hint = QLabel("빈칸: 0 또는 비워두기 · 숫자: 1~16")
        hint.setAlignment(Qt.AlignmentFlag.AlignCenter)
        root.addWidget(hint)

        grid_widget = QWidget()
        grid_layout = QGridLayout(grid_widget)
        grid_layout.setSpacing(6)
        cell_font = QFont()
        cell_font.setPointSize(13)

        for row in range(GRID_SIZE):
            row_cells: list[QLineEdit] = []
            for col in range(GRID_SIZE):
                cell = QLineEdit()
                cell.setFixedSize(CELL_SIZE, CELL_SIZE)
                cell.setAlignment(Qt.AlignmentFlag.AlignCenter)
                cell.setFont(cell_font)
                cell.setPlaceholderText("·")
                cell.setMaxLength(2)
                grid_layout.addWidget(cell, row, col)
                row_cells.append(cell)
            self._cells.append(row_cells)

        root.addWidget(grid_widget, alignment=Qt.AlignmentFlag.AlignCenter)

        button_row = QHBoxLayout()
        solve_btn = QPushButton("풀기")
        solve_btn.setDefault(True)
        solve_btn.clicked.connect(self._on_solve)
        reset_btn = QPushButton("초기화")
        reset_btn.clicked.connect(self._reset_puzzle)
        button_row.addWidget(solve_btn)
        button_row.addWidget(reset_btn)
        root.addLayout(button_row)

        self._status_label.setStyleSheet("color: #333; padding: 4px;")
        root.addWidget(self._status_label)

    def _read_cell_texts(self) -> list[list[str]]:
        return [[cell.text() for cell in row] for row in self._cells]

    def _set_grid_display(self, grid: Grid) -> None:
        texts = grid_to_cell_texts(grid)
        for row_index, row in enumerate(self._cells):
            for col_index, cell in enumerate(row):
                cell.setText(texts[row_index][col_index])

    def _reset_puzzle(self) -> None:
        puzzle = generate_random_puzzle()
        self._set_grid_display(puzzle)
        self._status_label.setText("새 문제를 생성했습니다. 풀기를 눌러 보세요.")
        self._status_label.setStyleSheet("color: #333; padding: 4px;")

    def _on_solve(self) -> None:
        grid = cells_to_grid(self._read_cell_texts())
        if grid is None:
            self._show_error("PARSE_ERROR")
            return

        try:
            envelope = self._boundary.solve(grid)
        except UnsolvableDomainError:
            self._show_error("UNSOLVABLE")
            return

        if isinstance(envelope, FailureEnvelope):
            self._show_error(envelope.code)
            return

        if isinstance(envelope, SuccessEnvelope):
            filled = apply_solution_payload(grid, envelope.payload)
            self._set_grid_display(filled)
            message = format_solution_message(envelope.payload)
            self._status_label.setText(f"완성: {message}")
            self._status_label.setStyleSheet("color: #1a7f37; padding: 4px;")
            return

        self._show_error("UNKNOWN")

    def _show_error(self, code: str) -> None:
        message = format_error_message(code)
        self._status_label.setText(message)
        self._status_label.setStyleSheet("color: #c0392b; padding: 4px;")
        if code in {"PARSE_ERROR", "UNSOLVABLE"}:
            QMessageBox.warning(self, "입력 오류", message)
