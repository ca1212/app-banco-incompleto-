from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QLabel,
    QPushButton
)

from PySide6.QtCore import Qt

from PySide6.QtGui import QFont

import qtawesome as qta

def abrir_inicio():

    janela = QWidget()

    janela.setWindowTitle(
        "Sistema Financeiro Calheiras"
    )

    janela.resize(900, 650)


    # =========================
    # LAYOUT
    # =========================

    layout = QVBoxLayout()

    layout.setContentsMargins(
        50,
        50,
        50,
        50
    )

    layout.setSpacing(20)

    janela.setLayout(layout)

    # =========================
    # TITULO
    # =========================

    texto_inicio = QLabel(
        "Sistema Financeiro\nCalheiras"
    )

    texto_inicio.setAlignment(
        Qt.AlignCenter
    )

    texto_inicio.setStyleSheet("""
    font-size: 38px;
    font-weight: bold;
    color: white;
    """)

    # =========================
    # SUBTITULO
    # =========================

    subtitulo = QLabel(
        "Controle profissional de empréstimos"
    )

    subtitulo.setAlignment(
        Qt.AlignCenter
    )

    subtitulo.setStyleSheet("""
    font-size: 16px;
    color: #9ca3af;
    """)

    # =========================
    # BOTÃO LOGIN
    # =========================

    botao_login = QPushButton(
        " Login"
    )

    botao_login.setIcon(
        qta.icon(
            "fa5s.sign-in-alt",
            color="white"
        )
    )

    botao_login.setCursor(
        Qt.PointingHandCursor
    )

    botao_login.setFixedSize(260, 60)

    # =========================
    # BOTÃO CADASTRO
    # =========================

    botao_cadastro = QPushButton(
        " Cadastrar"
    )

    botao_cadastro.setIcon(
        qta.icon(
            "fa5s.user-plus",
            color="white"
        )
    )

    botao_cadastro.setCursor(
        Qt.PointingHandCursor
    )

    botao_cadastro.setFixedSize(260, 60)

    def abrir_tela_login():
        from pages.login import abrir_login
        abrir_login(janela)
    def abrir_tela_cadastro():
        from pages.login import abrir_cadastro
        abrir_cadastro(janela)

    # =========================
    # EVENTOS
    # =========================

    botao_login.clicked.connect(
        lambda: abrir_tela_login()
    )

    botao_cadastro.clicked.connect(
        lambda: abrir_tela_cadastro()
    )

    # =========================
    # ADICIONAR NO LAYOUT
    # =========================

    layout.addStretch()

    layout.addWidget(
        texto_inicio,
        alignment=Qt.AlignHCenter
    )

    layout.addWidget(
        subtitulo,
        alignment=Qt.AlignHCenter
    )

    layout.addSpacing(40)

    layout.addWidget(
        botao_login,
        alignment=Qt.AlignHCenter
    )

    layout.addWidget(
        botao_cadastro,
        alignment=Qt.AlignHCenter
    )

    layout.addStretch()

    # =========================
    # ESTILO GLOBAL
    # =========================

    janela.setStyleSheet("""
    QWidget{
        background-color: #0f172a;
        color: white;
        font-family: Segoe UI;
    }

    QPushButton{
        background-color: #2563eb;
        color: white;
        border: none;
        border-radius: 14px;
        font-size: 16px;
        font-weight: bold;
        padding: 12px;
    }

    QPushButton:hover{
        background-color: #3b82f6;
    }

    QPushButton:pressed{
        background-color: #1d4ed8;
    }
    """)
    janela.show()
    return janela