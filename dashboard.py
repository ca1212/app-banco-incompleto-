from PySide6.QtWidgets import (
    QWidget,
    QLabel,
    QPushButton,
    QVBoxLayout,
    QHBoxLayout,
    QStackedWidget,
    QLineEdit,
    QTableWidget,
    QTableWidgetItem,
    QAbstractItemView,
    QHeaderView,
    QScrollArea,
    QMenu,
    QMessageBox,
    QComboBox,
    QGridLayout
)

import qtawesome as qta

from PySide6.QtCore import Qt
from PySide6.QtGui import QFont, QPixmap, QCursor

from pages.excclientes import abrir_exc

import json



def abrir_dashboard():

    global dashboard

    dashboard = QWidget()
    dashboard.setWindowTitle("Calheiras APP")
    dashboard.resize(1000, 600)

    layout_principal = QHBoxLayout()

    # =========================================================
    # MENU LATERAL
    # =========================================================

    menu_widget = QWidget()
    menu_widget.setFixedWidth(240)

    menu_widget.setStyleSheet("""
    background-color: #111827;
    border-right: 1px solid #1f2937;
    """)

    menu = QVBoxLayout()
    menu.setContentsMargins(15, 20, 15, 20)
    menu.setSpacing(15)

    menu_widget.setLayout(menu)

    paginas = QStackedWidget()

    show_menu = QPushButton("Menu")
    cad_clientes = QPushButton("Cadastrar clientes")
    ver_clientes = QPushButton("Ver clientes")
    exc_clientes = QPushButton("Excluir clientes")

    # =========================================================
    # PÁGINA MENU
    # =========================================================

    pagina_menu = QWidget()

    layout_menu = QVBoxLayout()

    pagina_menu.setLayout(layout_menu)

    grid_cards = QGridLayout()

    def criar_card(titulo, valor):
        card = QWidget()
        card.setStyleSheet("background-color: #1f2937; border-radius: 15px; padding: 20px;")
        vbox = QVBoxLayout(card)
        lbl_titulo = QLabel(titulo)
        lbl_titulo.setStyleSheet("font-size: 14px; color: #9ca3af;")
        lbl_valor = QLabel(valor)
        lbl_valor.setStyleSheet("font-size: 24px; font-weight: bold; color: white;")
        vbox.addWidget(lbl_titulo)
        vbox.addWidget(lbl_valor)
        return card
    
    card_total = criar_card("Total Emprestado", "R$ 0,00")
    card_recebido = criar_card("Total Recebido", "R$ 0,00")
    card_ativos = criar_card("Clientes Ativos", "0")
    card_inad = criar_card("Inadimplentes", "0")
    card_lucro = criar_card("Lucro Mensal", "R$ 0,00")

    grid_cards.addWidget(card_total, 0, 0)
    grid_cards.addWidget(card_recebido, 0, 1)
    grid_cards.addWidget(card_ativos, 1, 0)
    grid_cards.addWidget(card_inad, 1, 1)
    grid_cards.addWidget(card_lucro, 2, 0, 1, 2)

    
    layout_menu.addStretch()

    texto_menu = QLabel(
        "Sistema Financeiro\nControle de Empréstimos"
    )

    texto_menu.setAlignment(Qt.AlignCenter)

    texto_menu.setStyleSheet("""
    font-size: 30px;
    font-weight: bold;
    color: white;
    """)

    layout_menu.addStretch()
    layout_menu.addWidget(texto_menu)
    layout_menu.addStretch()
    layout_menu.addLayout(grid_cards)

    def carregar_metricas():
        try:
            with open("database/clientes.json", "r", encoding="utf-8") as f:
                clientes = json.load(f)
        except:
            return

        total_emp = 0.0
        total_rec = 0.0
        # Exemplo de lógica simples (ajuste conforme os dados do seu JSON)
        for c in clientes:
            for emp in c.get("emprestimos", []):
                try:
                    total_emp += float(emp.get("saldo", 0))
                    # Adicione aqui a lógica de como você define "recebido"
                except:
                    continue
    carregar_metricas()           
    # =========================================================
    # PÁGINA CADASTRO
    # =========================================================
    
    pagina_cadastro = QWidget()

    layout_cadastro = QVBoxLayout()

    pagina_cadastro.setLayout(layout_cadastro)

    texto_cadastro = QLabel("Cadastro de Clientes")

    texto_cadastro.setAlignment(Qt.AlignCenter)

    texto_cadastro.setStyleSheet("""
    font-size: 28px;
    font-weight: bold;
    """)

    

    entrada_nome = QLineEdit()
    entrada_nome.setPlaceholderText("Nome")

    tipo_operacao = QComboBox()
    tipo_operacao.addItem(" Emprestimo")
    tipo_operacao.addItem(" Parcelamento")        
    tipo_operacao.addItem(" Financiamento")        
    tipo_operacao.addItem(" Renegociação")        
            
    tipo_operacao.setStyleSheet("""
    QComboBox{
        background-color: #111827;
        color: white;
        border: 2px solid #1f2937;
        border-radius: 12px;
        padding: 10px;
        font-size: 15px;
        font-weight: bold;
        min-height: 20px;
    }

    QComboBox:hover{
        border: 2px solid #2563eb;
    }

    QComboBox::drop-down{
        border: none;
        width: 30px;
    }

    QComboBox QAbstractItemView{
        background-color: #1f2937;
        color: white;
        selection-background-color: #2563eb;
        border: 1px solid #374151;
        outline: none;
        padding: 5px;
    }
    """)

    
    quant_emprestimo = QLineEdit()
    quant_emprestimo.setPlaceholderText("Quantidade de Empréstimos")
    botao_criar = QPushButton(
                "Criar campos de empréstimos"
            )
    
    entrada_documento = QLineEdit()
    entrada_documento.setPlaceholderText("Documento CPF/CNPJ ")
    
    entrada_nasc = QLineEdit()
    entrada_nasc.setPlaceholderText("Data de nascimento")

    entrada_endereco = QLineEdit()
    entrada_endereco.setPlaceholderText("Endereço/CEP")

    entrada_cell = QLineEdit()
    entrada_cell.setPlaceholderText("Numero Telefonico")

    def atualizar_texto():
            tipo = tipo_operacao.currentText()
            
            if tipo == " Emprestimo":
                quant_emprestimo.setPlaceholderText(
                    "Quantidade de Empréstimos"
                )

            elif tipo == " Parcelamento":
                quant_emprestimo.setPlaceholderText(
                    "Quantidade de Parcelamentos"
                )

            elif tipo == " Financiamento":
                quant_emprestimo.setPlaceholderText(
                    "Quantidade de Financiamentos"
                )

            elif tipo == " Renegociação":
                quant_emprestimo.setPlaceholderText(
                    "Quantidade de Renegociações"
                )
                        
            

            if tipo == " Emprestimo":
                botao_criar.setText(
                    "Criar campos de empréstimos"
                )

            elif tipo == " Parcelamento":
                botao_criar.setText(
                    "Criar campos de parcelamentos"
                )

            elif tipo == " Financiamento":
                botao_criar.setText(
                    "Criar campos de financiamentos"
                )

            elif tipo == " Renegociação":
                botao_criar.setText(
                    "Criar campos de renegociação"
                )

    tipo_operacao.currentTextChanged.connect(
        atualizar_texto
        )
    atualizar_texto()
    
      

    # ========================================================
    # ÁREA SCROLL DOS EMPRÉSTIMOS
    # =========================================================

    container_emprestimos = QWidget()

    emprestimos_layout = QVBoxLayout()

    container_emprestimos.setLayout(
        emprestimos_layout
    )

    scroll_emprestimos = QScrollArea()

    scroll_emprestimos.setWidgetResizable(True)

    scroll_emprestimos.setWidget(
        container_emprestimos
    )

    scroll_emprestimos.setMinimumHeight(300)

    emprestimos_widgets = []

    cliente_editando = None

       

    def limpar_emprestimos():

        while emprestimos_layout.count():

            item = emprestimos_layout.takeAt(0)

            widget = item.widget()

            if widget:
                widget.deleteLater()

    

    def criar_campos_emprestimos():

        nonlocal emprestimos_widgets

        try:
            quantidade = int(
                quant_emprestimo.text()
            )

        except:
            QMessageBox.warning(
                dashboard,
                "Erro",
                "Digite um número válido"
            )
            return
        
        atual = len(emprestimos_widgets)

        if quantidade <= atual:
            return
    
        tipo = tipo_operacao.currentText()

        for i in range(atual, quantidade):

            container = QWidget()
            layout_bloco = QVBoxLayout(container)

            titulo = QLabel(
                f"tipo {i + 1}"
            )

            titulo.setStyleSheet("""
            font-size: 18px;
            font-weight: bold;
            margin-top: 15px;
            """)

            botao_excluir = QPushButton("Excluir este empréstimo")

            entrada_contrato = QLineEdit()

            if tipo == " Emprestimo":
                entrada_contrato.setPlaceholderText(
                    "Número do contrato"
                )

            elif tipo == " Parcelamento":
                entrada_contrato.setPlaceholderText(
                    "Cartão / Banco"
                )

            elif tipo == " Financiamento":
                entrada_contrato.setPlaceholderText(
                    "Bem financiado"
                )

            elif tipo == " Renegociação":
                entrada_contrato.setPlaceholderText(
                    "Origem da dívida"
                )

            entrada_saldo = QLineEdit()
            entrada_saldo.setPlaceholderText(
                "Saldo devedor"
            )

            entrada_taxa = QLineEdit()
            entrada_taxa.setPlaceholderText(
                "Taxa de juros"
            )

            entrada_entrada = QLineEdit()
            entrada_entrada.setPlaceholderText(
                "Entrada"
            )

            entrada_parcelas = QLineEdit()
            entrada_parcelas.setPlaceholderText(
                "Parcelas"
            )

            entrada_payday = QLineEdit()
            entrada_payday.setPlaceholderText(
                "Dia do pagamento"
            )

            layout_bloco.addWidget(titulo)
            layout_bloco.addSpacing(10)
            layout_bloco.addWidget(entrada_contrato)
            layout_bloco.addWidget(entrada_saldo)
            layout_bloco.addWidget(entrada_taxa)
            layout_bloco.addWidget(entrada_entrada)
            layout_bloco.addWidget(entrada_parcelas)
            layout_bloco.addWidget(entrada_payday)
            layout_bloco.addWidget(botao_excluir)

            emprestimos_layout.addWidget(container)
            
            

            emprestimos_widgets.append({
                "container": container,
                "contrato": entrada_contrato,
                "saldo": entrada_saldo,
                "taxa": entrada_taxa,
                "entrada": entrada_entrada,
                "parcelas": entrada_parcelas,
                "payday": entrada_payday,
                "botao excluir": botao_excluir
            })
        tipo_operacao.setEnabled(False)

    botao_criar.clicked.connect(
        criar_campos_emprestimos
    )

    # =========================================================
    # SALVAR CLIENTE
    # =========================================================

    botao_salvar = QPushButton(
        "Salvar Cliente"
    )

    def salvar_cliente():

        nonlocal cliente_editando

        nome = entrada_nome.text()
        documento = entrada_documento.text()
        telefone = entrada_cell.text()
        endereco = entrada_endereco.text()
        nascimento = entrada_nasc.text()

        emprestimos = []

        for emp in emprestimos_widgets:

            emprestimos.append({

                "contrato":
                emp["contrato"].text(),

                "saldo":
                emp["saldo"].text(),

                "taxa":
                emp["taxa"].text(),

                "entrada":
                emp["entrada"].text(),

                "parcelas":
                emp["parcelas"].text(),

                "dia do pagamento":
                emp["payday"].text()
            })

        cliente = {
            "nome": nome,
            "tipo_operacao":tipo_operacao.currentText(),
            "emprestimos": emprestimos,
            "documento": documento,
            "telefone": telefone,
            "endereco": endereco,
            "nascimento": nascimento
        }

        try:

            with open(
                "database/clientes.json",
                "r",
                encoding="utf-8"
            ) as arquivo:

                clientes = json.load(
                    arquivo
                )

        except:
            clientes = []

        # =====================================================
        # EDITAR CLIENTE
        # =====================================================

        if cliente_editando is not None:

            clientes[cliente_editando] = cliente

            cliente_editando = None

        else:

            clientes.append(cliente)

        # =====================================================
        # SALVAR JSON
        # =====================================================

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
        
        entrada_nome.clear()
        entrada_documento.clear()
        entrada_cell.clear()
        entrada_endereco.clear()
        entrada_nasc.clear()
        quant_emprestimo.clear()

        limpar_emprestimos()
        emprestimos_widgets.clear()

        mostrar_clientes()

        QMessageBox.information(
            dashboard,
            "Sucesso",
            "Cliente salvo com sucesso!"
        )

        tipo_operacao.setEnabled(True)

    botao_salvar.clicked.connect(
        salvar_cliente
    )

    layout_cadastro.addWidget(texto_cadastro)
    layout_cadastro.addWidget(entrada_nome)
    layout_cadastro.addWidget(tipo_operacao)
    layout_cadastro.addWidget(entrada_endereco)
    layout_cadastro.addWidget(entrada_nasc)
    layout_cadastro.addWidget(entrada_cell)
    layout_cadastro.addWidget(entrada_documento)
    layout_cadastro.addWidget(quant_emprestimo)
    layout_cadastro.addWidget(botao_criar)
    layout_cadastro.addWidget(scroll_emprestimos)
    layout_cadastro.addWidget(botao_salvar)

    # =========================================================
    # PÁGINA CLIENTES
    # =========================================================

    pagina_clientes = QWidget()

    layout_clientes = QVBoxLayout()

    pagina_clientes.setLayout(
        layout_clientes
    )

    lista_clientes_layout = QVBoxLayout()

    container_clientes = QWidget()

    container_clientes.setLayout(
        lista_clientes_layout
    )

    scroll = QScrollArea()

    scroll.setWidgetResizable(True)

    scroll.setWidget(container_clientes)

    texto_clientes = QLabel(
        "Clientes Existentes"
    )
    
    texto_clientes.setAlignment(
        Qt.AlignCenter
    )

    texto_clientes.setStyleSheet("""
    font-size: 28px;
    font-weight: bold;
    """)

    pesquisa_cliente = QLineEdit()

    pesquisa_cliente.setPlaceholderText(
        "Pesquisar cliente..."
    )

    layout_clientes.addWidget(
        pesquisa_cliente
    )

    layout_clientes.addWidget(
        texto_clientes
    )

    layout_clientes.addWidget(
        scroll
    )

    # =========================================================
    # EDITAR CLIENTE
    # =========================================================

    def editar_cliente(cliente):

        nonlocal cliente_editando

        try:

            with open(
                "database/clientes.json",
                "r",
                encoding="utf-8"
            ) as arquivo:

                clientes = json.load(
                    arquivo
                )

        except:
            return

        cliente_editando = clientes.index(cliente)

        paginas.setCurrentWidget(
            pagina_cadastro
        )

        entrada_nome.setText(
            cliente["nome"]
        )

        entrada_documento.setText(
            cliente["documento"]
        )
        entrada_cell.setText(
            cliente["telefone"]
        )
        entrada_endereco.setText(
            cliente["endereco"]
        )
        entrada_nasc.setText(
            cliente["nascimento"]
        )
        quant_emprestimo.setText(
            str(len(cliente["emprestimos"]))
        )

        limpar_emprestimos()
        emprestimos_widgets.clear()

        criar_campos_emprestimos()

        for i, emp in enumerate(
            cliente["emprestimos"]
        ):
            def excluir_emprestimo(i):

                del cliente["emprestimos"][i]

                try:
                    with open(
                        "database/clientes.json",
                        "r",
                        encoding="utf-8"
                    ) as arquivo:

                        clientes = json.load(arquivo)

                except:
                    return

                clientes[cliente_editando] = cliente

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

                editar_cliente(cliente)
    
            emprestimos_widgets[i]["contrato"].setText(
                emp["contrato"]
            )

            emprestimos_widgets[i]["saldo"].setText(
                emp["saldo"]
            )

            emprestimos_widgets[i]["taxa"].setText(
                emp["taxa"]
            )

            emprestimos_widgets[i]["entrada"].setText(
                emp["entrada"]
            )

            emprestimos_widgets[i]["parcelas"].setText(
                emp["parcelas"]
            )

            emprestimos_widgets[i]["payday"].setText(
                emp["dia do pagamento"]
            )
            emprestimos_widgets[i]["botao excluir"].clicked.connect(
            lambda _, indice=i: excluir_emprestimo(indice)
            )

    # =========================================================
    # MENU CONTEXTO
    # =========================================================

    def abrir_menu(pos, cliente):

        menu = QMenu()

        editar = menu.addAction(
            "Editar cliente"
        )

        acao = menu.exec(
            QCursor.pos()
        )

        if acao == editar:
            editar_cliente(cliente)

    # =========================================================
    # MOSTRAR CLIENTES
    # =========================================================

    def mostrar_clientes():

        while lista_clientes_layout.count():

            item = lista_clientes_layout.takeAt(0)

            widget = item.widget()

            if widget:
                widget.deleteLater()

        try:

            with open(
                "database/clientes.json",
                "r",
                encoding="utf-8"
            ) as arquivo:

                clientes = json.load(
                    arquivo
                )

        except:
            clientes = []

        for cliente in clientes:

            quantidade = len(
                cliente.get(
                    "emprestimos",
                    []
                )
            )

            texto = (
                f'{cliente["nome"]}\n'
                f'Tipo: {cliente.get("tipo_operacao", "Empréstimo")}\n'
                f'Operações: {quantidade}'
            )

            botao = QPushButton(texto)

            botao.setFixedHeight(100)

            botao.setStyleSheet("""
            QPushButton{
                background-color: #1f2937;
                text-align: left;
                padding-left: 20px;
                font-size: 16px;
                border-radius: 15px;
            }

            QPushButton:hover{
                background-color: #374151;
            }
            """)

            botao.setContextMenuPolicy(
                Qt.CustomContextMenu
            )

            botao.customContextMenuRequested.connect(
                lambda pos, c=cliente:
                abrir_menu(pos, c)
            )

            botao.clicked.connect(
                lambda checked=False, c=cliente:
                abrir_detalhes(c)
            )

            lista_clientes_layout.addWidget(
                botao
            )

    # =========================================================
    # DETALHES CLIENTE
    # =========================================================

    def abrir_detalhes(cliente):

        global janela_cliente

        janela_cliente = QWidget()

        janela_cliente.setWindowTitle(
            cliente["nome"]
        )

        janela_cliente.resize(1000, 400)

        layout = QVBoxLayout()

        tabela = QTableWidget()

        tabela.setColumnCount(7)

        emprestimos = cliente.get(
            "emprestimos",
            []
        )

        tabela.setRowCount(
            len(emprestimos)
        )

        tabela.setEditTriggers(
            QAbstractItemView.NoEditTriggers
        )
        tipo = cliente.get("tipo_operacao", "Emprestimo")
        if tipo == " Emprestimo":
            tabela.setHorizontalHeaderLabels([
                "Nome",
                "Contrato",
                "Saldo",
                "Taxa",
                "Entrada",
                "Parcelas",
                "Pagamento"
            ])
        elif tipo == " Parcelamento":
            tabela.setHorizontalHeaderLabels([
                "Nome",
                "Cartão / Banco",
                "Saldo",
                "Taxa",
                "Entrada",
                "Parcelas",
                "Pagamento"
            ])
        elif tipo == " Financiamento":
            tabela.setHorizontalHeaderLabels([
            "Nome",
            "Bem financiado",
            "Saldo",
            "Taxa",
            "Entrada",
            "Parcelas",
            "Pagamento"#Origem da dívida
            ])
        elif tipo == " Renegociação":
            tabela.setHorizontalHeaderLabels([
            "Nome",
            "Origem da dívida",
            "Saldo",
            "Taxa",
            "Entrada",
            "Parcelas",
            "Pagamento"
            ])
        for linha, emp in enumerate(
            emprestimos
        ):

            tabela.setItem(
                linha,
                0,
                QTableWidgetItem(
                    cliente["nome"]
                )
            )

            tabela.setItem(
                linha,
                1,
                QTableWidgetItem(
                    emp["contrato"]
                )
            )

            tabela.setItem(
                linha,
                2,
                QTableWidgetItem(
                    emp["saldo"]
                )
            )

            tabela.setItem(
                linha,
                3,
                QTableWidgetItem(
                    emp["taxa"]
                )
            )

            tabela.setItem(
                linha,
                4,
                QTableWidgetItem(
                    emp["entrada"]
                )
            )

            tabela.setItem(
                linha,
                5,
                QTableWidgetItem(
                    emp["parcelas"]
                )
            )

            tabela.setItem(
                linha,
                6,
                QTableWidgetItem(
                    emp["dia do pagamento"]
                )
            )

        tabela.horizontalHeader().setSectionResizeMode(
            QHeaderView.Stretch
        )

        layout.addWidget(tabela)

        janela_cliente.setLayout(
            layout
        )

        janela_cliente.show()

    # =========================================================
    # PESQUISA
    # =========================================================

    def pesquisar_cliente():

        texto = pesquisa_cliente.text().lower()

        for i in range(
            lista_clientes_layout.count()
        ):

            widget = lista_clientes_layout.itemAt(i).widget()

            if widget:

                nome = widget.text().lower()

                widget.setVisible(
                    texto in nome
                )

    pesquisa_cliente.textChanged.connect(
        pesquisar_cliente
    )

    mostrar_clientes()

    # =========================================================
    # STACK
    # =========================================================

    paginas.addWidget(pagina_menu)
    paginas.addWidget(pagina_cadastro)
    paginas.addWidget(pagina_clientes)

    paginas.setCurrentWidget(pagina_menu)

    # =========================================================
    # BOTÕES MENU
    # =========================================================

    show_menu.clicked.connect(
        lambda:
        paginas.setCurrentWidget(
            pagina_menu
        )
    )

    cad_clientes.clicked.connect(
        lambda:
        paginas.setCurrentWidget(
            pagina_cadastro
        )
    )

    ver_clientes.clicked.connect(
        lambda:
        paginas.setCurrentWidget(
            pagina_clientes
        )
    )

    exc_clientes.clicked.connect(
        lambda:
        abrir_exc(mostrar_clientes)
    )

    # =========================================================
    # ADICIONAR MENU
    # =========================================================

    menu.addWidget(show_menu)
    menu.addWidget(cad_clientes)
    menu.addWidget(ver_clientes)
    menu.addWidget(exc_clientes)

    menu.addStretch()

    layout_principal.addWidget(menu_widget)
    layout_principal.addWidget(paginas, 4)

    dashboard.setLayout(layout_principal)

    # =========================================================
    # ESTILO
    # =========================================================

    for botao in [
        show_menu,
        cad_clientes,
        ver_clientes,
        exc_clientes
    ]:

        botao.setFixedHeight(50)

        botao.setCursor(
            Qt.PointingHandCursor
        )

    dashboard.setStyleSheet("""
    QWidget{
        background-color: #0f172a;
        color: white;
        font-size: 14px;
    }

    QPushButton{
        background-color: #696969;
        border: none;
        border-radius: 10px;
        padding: 12px;
    }

    QPushButton:hover{
        background-color: #4F4F4F;
    }

    QLineEdit{
        background-color: #111827;
        border: 2px solid #1f2937;
        border-radius: 12px;
        padding: 10px;
        min-height: 20px;
    }

    QTableWidget{
        background-color: #1b1b1b;
        gridline-color: #333;
    }
    """)

    botao_salvar.setStyleSheet("""
    QPushButton{
        background-color: #2563eb;
        color: white;
        font-size: 15px;
        font-weight: bold;
        border-radius: 12px;
    }

    QPushButton:hover{
        background-color: #3b82f6;
    }
    """)

    # =========================================================
    # ÍCONES
    # =========================================================

    show_menu.setIcon(
        qta.icon(
            "fa5s.home",
            color="white"
        )
    )

    cad_clientes.setIcon(
        qta.icon(
            "fa5s.user-plus",
            color="white"
        )
    )

    ver_clientes.setIcon(
        qta.icon(
            "fa5s.users",
            color="white"
        )
    )

    exc_clientes.setIcon(
        qta.icon(
            "fa5s.trash",
            color="white"
        )
    )

    dashboard.setFont(
        QFont("Segoe UI", 10)
    )

    # =========================================================
    # FUNDO MENU
    # =========================================================

    fundo = QLabel(menu_widget)

    fundo.setPixmap(
        QPixmap("fundo.jpg")
    )

    fundo.setScaledContents(True)

    fundo.setGeometry(
        menu_widget.rect()
    )

    fundo.lower()

    fundo.show()

    menu_widget.resizeEvent = lambda event: (
        fundo.setGeometry(menu_widget.rect()),
        QWidget.resizeEvent(menu_widget, event)
    )

    dashboard.show()

    return dashboard