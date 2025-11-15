from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox
from PySide6.QtGui import QIcon
import sys, os
import ctypes
from cadastro import DialogCadastro
from principal import Ui_MainWindow
import sqlite3

conn = sqlite3.connect("LOGMARKET.db")
cursor = conn.cursor()

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Forçar ícone
        myappid = u"icone_projeto"
        ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
        self.setWindowIcon(QIcon("logo_principal.ico"))

        # Botões
        self.ui.pushButton.clicked.connect(self.consultar)
        self.ui.pushButton_2.clicked.connect(self.cadastrar)
        self.ui.pushButton_3.clicked.connect(self.refresh)
        self.ui.pushButton_4.clicked.connect(self.logout)
        self.ui.Input_Pesquisar.returnPressed.connect(self.ui.pushButton.click)

    def consultar(self):
        pesquisa = self.ui.Input_Pesquisar.text().strip()

        if pesquisa == "":
            QMessageBox.warning(self, "Erro", "Digite algo para pesquisar!")
            return

        # Busca por código se for número
        if pesquisa.isnumeric():
            sql = "SELECT * FROM TABELA_LOGMARKET WHERE CODIGO = ?"
            cursor.execute(sql, (pesquisa,))
        
        # Busca por nome/modelo se for texto
        else:
            sql = """SELECT * FROM TABELA_LOGMARKET WHERE LOWER(MODELO) LIKE LOWER(?) OR LOWER(NOME) LIKE LOWER(?)"""
            parametro = f"%{pesquisa}%"
            cursor.execute(sql, (parametro, parametro))

        resultado = cursor.fetchall()

        if not resultado:
            self.refresh()
            QMessageBox.warning(self, "Erro", "Produto não encontrado!")
            return

        # Carrega o primeiro resultado
        codigo, nome, marca, modelo, unidade, valor = resultado[0]

        # Preenche interface
        self.ui.Input_Codigo.setText(str(codigo))
        self.ui.Input_Nome.setText(str(nome))
        self.ui.Input_Marca.setText(str(marca))
        self.ui.Input_Modelo.setText(str(modelo))
        self.ui.Input_Unidade.setText(str(unidade))
        self.ui.Input_Valor.setText(str(valor))
        self.ui.Input_Pesquisar.clear()

    def cadastrar(self):
        dialog = DialogCadastro(self)

        if dialog.exec():
            codigo = dialog.codigo
            nome = dialog.nome
            marca = dialog.marca
            modelo = dialog.modelo
            unidade = dialog.unidade
            valor = dialog.preco

            sql = """INSERT INTO TABELA_LOGMARKET (CODIGO, NOME, MARCA, MODELO, UNIDADE, VALOR) VALUES (?, ?, ?, ?, ?, ?)"""

            cursor.execute(sql, (codigo, nome, marca, modelo, unidade, valor))
            conn.commit()

            QMessageBox.information(
                self,
                "Produto Cadastrado",
                f"Produto cadastrado com sucesso!\n\n"
                f"Código: {codigo}\n"
                f"Nome: {nome}\n"
                f"Marca: {marca}\n"
                f"Modelo: {modelo}\n"
                f"Unidade: {unidade}\n"
                f"Valor: R$ {valor}"
            )

    def refresh(self):
        self.ui.Input_Pesquisar.clear()
        self.ui.Input_Codigo.clear()
        self.ui.Input_Nome.clear()
        self.ui.Input_Marca.clear()
        self.ui.Input_Modelo.clear()
        self.ui.Input_Unidade.clear()
        self.ui.Input_Valor.clear()

    def logout(self):
        resposta = QMessageBox.question(
            self, "Logout", "Deseja realmente sair?",
            QMessageBox.Yes | QMessageBox.No
        )
        if resposta == QMessageBox.Yes:
            self.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("logo_principal.ico"))
    window = MainWindow()
    window.show()
    sys.exit(app.exec())