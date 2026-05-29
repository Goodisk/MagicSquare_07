"""Qt GUI 진입점 — python -m magic_square.boundary.qt"""

from __future__ import annotations

import sys

from PyQt6.QtWidgets import QApplication

from magic_square.boundary.qt.main_window import MainWindow


def main() -> None:
    """Qt 애플리케이션을 실행한다."""
    app = QApplication(sys.argv)
    app.setApplicationName("Magic Square Solver")
    window = MainWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
