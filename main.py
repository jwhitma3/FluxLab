# SPDX-FileCopyrightText: 2026 Joshua C. Whitman <jwhitma3@my.westga.edu>
# SPDX-License-Identifier: MIT

"""Main entry point for FluxLab."""

import sys

from PySide6.QtCore import QFile, QIODevice
from PySide6.QtUiTools import QUiLoader
from PySide6.QtWidgets import QApplication


def main() -> None:
    """Run the main application."""
    app = QApplication(sys.argv)

    ui_file_path = "view/ui/mainwindow.ui"
    ui_file = QFile(ui_file_path)
    if not ui_file.open(QIODevice.ReadOnly):
        print(f"Cannot open {ui_file_path}: {ui_file.errorString()}")
        sys.exit(-1)

    loader = QUiLoader()
    window = loader.load(ui_file)
    ui_file.close()

    if not window:
        print(loader.errorString())
        sys.exit(-1)

    window.setWindowTitle("Flux Lab")
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
