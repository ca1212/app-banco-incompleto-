from PySide6.QtWidgets import (
    QApplication,
    QWidget,
    QVBoxLayout,
    QLabel,
    QPushButton
)

from PySide6.QtCore import Qt

from PySide6.QtGui import QFont, QIcon

import qtawesome as qta

import sys
from pages.inicio import abrir_inicio

app = QApplication(sys.argv)
app.setWindowIcon(QIcon("icone.ico"))

abrir_inicio()

sys.exit(app.exec())