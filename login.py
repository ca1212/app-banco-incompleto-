from PySide6.QtWidgets import (
    QApplication,
    QWidget,
    QVBoxLayout,
    QLabel,
    QPushButton,
    QLineEdit,
    QFrame,
    QHBoxLayout
)

from PySide6.QtCore import Qt



from pages.dashboard import abrir_dashboard
from pages.inicio import abrir_inicio
import qtawesome as qta
import re
import json


# =========================
# CARREGAR USUÁRIOS
# =========================

try:

    with open(
        "database/usuarios.json",
        "r",
        encoding="utf-8"
    ) as arquivo:

        usuarios = json.load(arquivo)

except:

    usuarios = []


# =========================
# ESTILO GLOBAL
# =========================

ESTILO = """
QWidget{
    background-color: #0f0f0f;
    color: white;
    font-size: 14px;
}

QFrame{
    background-color: #1b1b1b;
    border-radius: 20px;
}

QLineEdit{
    background-color: #262626;
    border: 2px solid #333;
    border-radius: 10px;
    padding: 10px;
    font-size: 15px;
}

QLineEdit:focus{
    border: 2px solid #00b894;
}

QPushButton{
    background-color: #00b894;
    border: none;
    border-radius: 10px;
    padding: 12px;
    font-size: 15px;
    font-weight: bold;
}

QPushButton:hover{
    background-color: #00a383;
}

QLabel{
    background: transparent;
}
"""


# =========================
# CADASTRO
# =========================

def abrir_cadastro(janela):
    
    janela.close()

    global Jcadastro

    Jcadastro = QWidget()

    Jcadastro.setWindowTitle("Cadastro")

    Jcadastro.resize(900, 600)

    Jcadastro.setStyleSheet(ESTILO)

    layout_principal = QVBoxLayout()

    Jcadastro.setLayout(layout_principal)

    layout_principal.addStretch()

    # CARD
    card = QFrame()

    card.setFixedWidth(450)

    layout_card = QVBoxLayout()

    card.setLayout(layout_card)

    # TÍTULO
    titulo = QLabel("Criar Conta")

    titulo.setAlignment(Qt.AlignCenter)

    titulo.setStyleSheet("""
    font-size: 30px;
    font-weight: bold;
    """)

    subtitulo = QLabel(
        "Cadastre um novo usuário"
    )

    subtitulo.setAlignment(Qt.AlignCenter)

    subtitulo.setStyleSheet("""
    color: #aaaaaa;
    font-size: 15px;
    """)

    # LOGIN
    Log_entrada = QLineEdit()

    Log_entrada.setPlaceholderText(
        "Login"
    )

    Log_entrada.setFixedHeight(45)

    # SENHA
    Sen_entrada = QLineEdit()

    Sen_entrada.setPlaceholderText(
        "Senha"
    )

    Sen_entrada.setEchoMode(
        QLineEdit.Password
    )

    Sen_entrada.setFixedHeight(45)

    # BOTÃO
    voltar = QPushButton("← Voltar")
    voltar.setFixedHeight(50)

    voltar.setCursor(
        Qt.PointingHandCursor
    )
    
    cadastrar = QPushButton(
        "Cadastrar"
    )

    cadastrar.setFixedHeight(50)

    cadastrar.setIcon(
        qta.icon(
            "fa5s.user-plus",
            color="white"
        )
    )

    # ERRO
    TErro = QLabel("")

    TErro.setAlignment(Qt.AlignCenter)

    TErro.setStyleSheet("""
    color: #ff7675;
    font-size: 13px;
    """)

    # ADICIONAR
    layout_card.addWidget(voltar)
    layout_card.addSpacing(20)

    layout_card.addWidget(titulo)

    layout_card.addWidget(subtitulo)

    layout_card.addSpacing(20)

    layout_card.addWidget(Log_entrada)

    layout_card.addWidget(Sen_entrada)

    layout_card.addSpacing(10)

    layout_card.addWidget(cadastrar)

    layout_card.addWidget(TErro)

    layout_card.addSpacing(20)

    layout_principal.addWidget(
        card,
        alignment=Qt.AlignCenter
    )

    layout_principal.addStretch()

    def voltar_inicio():
        from pages.inicio import abrir_inicio
        Jcadastro.close()

        abrir_inicio()

    voltar.clicked.connect(voltar_inicio)

    # =========================
    # VALIDAR
    # =========================

    def validar():

        login = Log_entrada.text()

        senha = Sen_entrada.text()

        if (
            len(senha) >= 10
            and re.search(r"\d.*\d", senha)
            and re.search(r"[!@#$%&*()]", senha)
        ):

            for usuario in usuarios:

                if usuario["login"] == login:

                    TErro.setText(
                        "Esse login já existe."
                    )

                    return

            novo_usuario = {

                "login": login,
                "senha": senha

            }

            usuarios.append(
                novo_usuario
            )

            with open(
                "database/usuarios.json",
                "w",
                encoding="utf-8"
            ) as arquivo:

                json.dump(
                    usuarios,
                    arquivo,
                    indent=4,
                    ensure_ascii=False
                )

            Jcadastro.close()

            abrir_dashboard()

        else:

            TErro.setText(
                "Senha inválida.\n"
                "Use 10 caracteres, 2 números e 1 símbolo."
            )

    cadastrar.clicked.connect(validar)

    Sen_entrada.returnPressed.connect(
        validar
    )

    Jcadastro.show()


# =========================
# LOGIN
# =========================

def abrir_login(janela):

    janela.close()

    global Jlogin

    Jlogin = QWidget()

    Jlogin.setWindowTitle("Login")

    Jlogin.resize(900, 600)

    Jlogin.setStyleSheet(ESTILO)

    layout_principal = QVBoxLayout()

    Jlogin.setLayout(layout_principal)

    layout_principal.addStretch()

    # CARD
    card = QFrame()

    card.setFixedWidth(450)

    layout_card = QVBoxLayout()

    card.setLayout(layout_card)

    # TÍTULO
    titulo = QLabel("Login")

    titulo.setAlignment(Qt.AlignCenter)

    titulo.setStyleSheet("""
    font-size: 30px;
    font-weight: bold;
    """)

    subtitulo = QLabel(
        "Entre na sua conta"
    )

    subtitulo.setAlignment(Qt.AlignCenter)

    subtitulo.setStyleSheet("""
    color: #aaaaaa;
    font-size: 15px;
    """)

    # LOGIN
    Log_login = QLineEdit()

    Log_login.setPlaceholderText(
        "Login"
    )

    Log_login.setFixedHeight(45)

    # SENHA
    Sen_login = QLineEdit()

    Sen_login.setPlaceholderText(
        "Senha"
    )

    Sen_login.setEchoMode(
        QLineEdit.Password
    )

    Sen_login.setFixedHeight(45)

    # BOTÃO
    voltar = QPushButton("← Voltar")
    voltar.setFixedHeight(50)

    voltar.setCursor(
        Qt.PointingHandCursor
    )   
    logar = QPushButton(
        "Entrar"
    )
    
    logar.setFixedHeight(50)

    logar.setIcon(
        qta.icon(
            "fa5s.sign-in-alt",
            color="white"
        )
    )

    # TEXTO ERRO
    erro = QLabel("")

    erro.setAlignment(Qt.AlignCenter)

    erro.setStyleSheet("""
    color: #ff7675;
    font-size: 13px;
    """)

    # ADICIONAR
    layout_card.addWidget(voltar)
    layout_card.addSpacing(20)

    layout_card.addWidget(titulo)

    layout_card.addWidget(subtitulo)

    layout_card.addSpacing(20)

    layout_card.addWidget(Log_login)

    layout_card.addWidget(Sen_login)

    layout_card.addSpacing(10)

    layout_card.addWidget(logar)

    layout_card.addWidget(erro)

    layout_card.addSpacing(20)

    layout_principal.addWidget(
        card,
        alignment=Qt.AlignCenter
    )

    layout_principal.addStretch()

    def voltar_inicio():

        Jlogin.close()

        abrir_inicio()

    voltar.clicked.connect(voltar_inicio)

    # =========================
    # LOGIN
    # =========================

    def dash():

        login = Log_login.text()

        senha = Sen_login.text()

        try:

            with open(
                "database/usuarios.json",
                "r",
                encoding="utf-8"
            ) as arquivo:

                usuarios_atualizados = json.load(
                    arquivo
                )

        except:

            usuarios_atualizados = []

        for usuario in usuarios_atualizados:

            if (
                usuario["login"] == login
                and usuario["senha"] == senha
            ):

                Jlogin.close()

                abrir_dashboard()

                return

        erro.setText(
            "Login ou senha incorretos"
        )

    def pular():
        global dashboard
        dashboard = abrir_dashboard()

    logar.clicked.connect(pular)

    Sen_login.returnPressed.connect(dash)

    Jlogin.show()