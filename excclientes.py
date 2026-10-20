from PySide6.QtWidgets import (
    QWidget,
    QLabel,
    QPushButton,
    QVBoxLayout,
    QScrollArea,
    QFrame,
    QMessageBox,
)

from PySide6.QtCore import Qt

import qtawesome as qta

import json


# =========================
# JANELA EXCLUIR CLIENTES
# =========================

def abrir_exc(carregar_tabela):

    global janela

    janela = QWidget()

    janela.setWindowTitle(
        "Excluir Clientes"
    )

    janela.resize(850, 600)

    janela.setStyleSheet("""
    QWidget{
        background-color: #0f0f0f;
        color: white;
        font-size: 14px;
    }

    QFrame{
        background-color: #1b1b1b;
        border-radius: 15px;
    }

    QPushButton{
        background-color: #2b2b2b;
        border: none;
        border-radius: 12px;
        padding: 15px;
        font-size: 15px;
        text-align: left;
    }

    QPushButton:hover{
        background-color: #aa0000;
    }

    QLabel{
        background: transparent;
    }
    """)

    layout = QVBoxLayout()

    janela.setLayout(layout)

    # =========================
    # TÍTULO
    # =========================

    texto = QLabel(
        "Excluir Clientes"
    )

    texto.setAlignment(
        Qt.AlignCenter
    )

    texto.setStyleSheet("""
    font-size: 30px;
    font-weight: bold;
    """)

    subtitulo = QLabel(
        "Clique em um cliente para remover"
    )

    subtitulo.setAlignment(
        Qt.AlignCenter
    )

    subtitulo.setStyleSheet("""
    color: #aaaaaa;
    font-size: 14px;
    """)

    layout.addSpacing(20)

    layout.addWidget(texto)

    layout.addWidget(subtitulo)

    layout.addSpacing(20)

    # =========================
    # SCROLL
    # =========================

    scroll = QScrollArea()

    scroll.setWidgetResizable(True)

    container = QWidget()

    lista_layout = QVBoxLayout()

    container.setLayout(lista_layout)

    scroll.setWidget(container)

    layout.addWidget(scroll)

    # =========================
    # EXCLUIR
    # =========================

    def excluir(cliente, card):

        resposta = QMessageBox.question(
            janela,
            "Confirmar Exclusão",
            (
                f'Deseja excluir "{cliente["nome"]}"?\n\n'
                "Todos os empréstimos, parcelas e "
                "movimentações financeiras serão removidos."
            ),
            QMessageBox.Yes | QMessageBox.No
        )

        if resposta != QMessageBox.Yes:
            return

        nome_cliente = cliente["nome"]

        # CLIENTES
        try:

            with open(
                "database/clientes.json",
                "r",
                encoding="utf-8"
            ) as arquivo:

                clientes = json.load(arquivo)

        except:

            clientes = []

        clientes = [
            c for c in clientes
            if c["nome"] != nome_cliente
        ]

        with open(
            "database/clientes.json",
            "w",
            encoding="utf-8"
        ) as arquivo:

            json.dump(
                clientes,
                arquivo,
                indent=4,
                ensure_ascii=False
            )

        # EMPRESTIMOS
        try:

            with open(
                "database/emprestimos.json",
                "r",
                encoding="utf-8"
            ) as arquivo:

                emprestimos = json.load(arquivo)

        except:

            emprestimos = []

        emprestimos = [
            e for e in emprestimos
            if e["cliente"] != nome_cliente
        ]

        with open(
            "database/emprestimos.json",
            "w",
            encoding="utf-8"
        ) as arquivo:

            json.dump(
                emprestimos,
                arquivo,
                indent=4,
                ensure_ascii=False
            )

        # PARCELAS
        try:

            with open(
                "database/parcelas.json",
                "r",
                encoding="utf-8"
            ) as arquivo:

                parcelas = json.load(arquivo)

        except:

            parcelas = []

        parcelas = [
            p for p in parcelas
            if p["cliente"] != nome_cliente
        ]

        with open(
            "database/parcelas.json",
            "w",
            encoding="utf-8"
        ) as arquivo:

            json.dump(
                parcelas,
                arquivo,
                indent=4,
                ensure_ascii=False
            )

        # CAIXA
        try:

            with open(
                "database/caixa.json",
                "r",
                encoding="utf-8"
            ) as arquivo:

                caixa = json.load(arquivo)

        except:

            caixa = []

        caixa = [
            c for c in caixa
            if c["cliente"] != nome_cliente
        ]

        with open(
            "database/caixa.json",
            "w",
            encoding="utf-8"
        ) as arquivo:

            json.dump(
                caixa,
                arquivo,
                indent=4,
                ensure_ascii=False
            )

        card.deleteLater()

        carregar_tabela()

        QMessageBox.information(
            janela,
            "Sucesso",
            "Cliente removido com sucesso."
        )
    # =========================
    # CARREGAR CLIENTES
    # =========================

    vazio = QLabel("")

    vazio.setAlignment(Qt.AlignCenter)

    lista_layout.addWidget(vazio)

    def carregar_botoes():

        try:

            with open(
                "database/clientes.json",
                "r",
                encoding="utf-8"
            ) as arquivo:

                clientes_atualizados = json.load(
                    arquivo
                )

        except:

            clientes_atualizados = []

        if not clientes_atualizados:

            vazio.setText(
                "Nenhum cliente cadastrado"
            )

        for cliente in clientes_atualizados:

            # CARD
            card = QFrame()

            card_layout = QVBoxLayout()

            card.setLayout(card_layout)

            # BOTÃO
            botao_cliente = QPushButton()

            botao_cliente.setFixedHeight(75)

            botao_cliente.setIcon(
                qta.icon(
                    "fa5s.user-times",
                    color="white"
                )
            )

            quantidade = 0

            try:

                with open(
                    "database/emprestimos.json",
                    "r",
                    encoding="utf-8"
                ) as arquivo:

                    emprestimos = json.load(arquivo)

                quantidade = len([
                    e for e in emprestimos
                    if e["cliente"] == cliente["nome"]
                ])

            except:
                pass
    

            botao_cliente.setText(
                f'{cliente["nome"]}\n'
                f'Empréstimos: {quantidade}'
            )

            botao_cliente.clicked.connect(
                lambda checked=False,
                c=cliente,
                ca=card:
                excluir(c, ca)
            )

            card_layout.addWidget(
                botao_cliente
            )

            lista_layout.addWidget(card)

    carregar_botoes()

    lista_layout.addStretch()

    janela.show()

    return janela