from PySide6.QtWidgets import QApplication, QDialog
from PySide6.QtWidgets import QLineEdit
from PySide6.QtCore import QTimer
from PySide6.QtGui import QIcon
import sys, os
import ctypes
import sqlite3
from tela_principal import MainWindow
from login import Ui_Dialog

def get_conn():
    return sqlite3.connect("LOGMARKET.db")

class MeuApp(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        # Forçar Alteração do Ícone
        myappid = u"icone_projeto"
        ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
        self.setWindowIcon(QIcon("logo_principal.ico"))

        # Centralizar Janela
        qr = self.frameGeometry()
        cp = QApplication.primaryScreen().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

        # Eventos dos botões
        self.ui.pushButton_2.clicked.connect(self.on_login_clicked)
        self.ui.pushButton.pressed.connect(self.mostrar_senha)
        self.ui.pushButton.released.connect(self.ocultar_senha)
        self.ui.pushButton_3.clicked.connect(self.alterar_senha_aguarde)

    def tela_principal(self):
        self.login_window = MainWindow()
        self.login_window.show()
        self.close()

    def alterar_senha_aguarde(self):
        self.ui.label_alerta.setStyleSheet("color: #1E90FF; font-weight: bold")
        self.ui.label_alerta.setText("Aguarde...")
        QTimer.singleShot(500, lambda: self.alterar_senha())

    def alterar_senha(self):
        from tela_recovery import Recovery
        self.recuperacao = Recovery()
        self.recuperacao.show()
        self.close()

    def mostrar_senha(self):
        self.ui.lineEdit_2.setEchoMode(QLineEdit.Normal)

    def ocultar_senha(self):
        self.ui.lineEdit_2.setEchoMode(QLineEdit.Password)

    def on_login_clicked(self):
        usuario = self.ui.lineEdit.text()
        senha = self.ui.lineEdit_2.text()

        consulta = '''SELECT USUARIO, SENHA FROM TABELA_LOGMARKET_USUARIOS WHERE USUARIO = ? AND SENHA = ?'''

        try:
            conn = get_conn()
            cursor = conn.cursor()
            cursor.execute(consulta, (usuario, senha))
            resultado = cursor.fetchone()
            conn.close()

        except sqlite3.Error as e:
            print("Erro:", e)
            self.ui.label_alerta.setText("Falha na Conexão!")
            QTimer.singleShot(100, lambda: self.ui.lineEdit.clear())
            QTimer.singleShot(100, lambda: self.ui.lineEdit_2.clear())
            QTimer.singleShot(2000, lambda: self.ui.label_alerta.clear())
            return

        if resultado:
            self.ui.label_alerta.setStyleSheet("color: #FFF; font-weight: bold")
            self.ui.label_alerta.setText("Carregando...")
            QTimer.singleShot(1000, lambda: self.tela_principal())

        else:
            self.ui.label_alerta.setStyleSheet("color: #f22222; font-weight: bold")
            self.ui.label_alerta.setText("Usuário ou Senha Incorreta!")
            QTimer.singleShot(100, lambda: self.ui.lineEdit_2.clear())
            QTimer.singleShot(2500, lambda: self.ui.label_alerta.clear())

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("logo_principal.ico"))
    janela = MeuApp()
    janela.show()
    sys.exit(app.exec())
