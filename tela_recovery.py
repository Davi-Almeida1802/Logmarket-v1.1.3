from PySide6.QtWidgets import QApplication, QDialog, QLineEdit
from PySide6.QtGui import QIcon
from PySide6.QtCore import QTimer
import sys, ctypes
import sqlite3
from recovery import Ui_Recovery

conn = sqlite3.connect("LOGMARKET.db")
cursor = conn.cursor()

class Recovery(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Recovery()
        self.ui.setupUi(self)
        self.ui.lineEdit.setMaxLength(11)   # Ex.: limitar CPF para 11 dígitos


        # Ícone do app
        myappid = u"icone_projeto"
        ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)

        # Centraliza janela
        qr = self.frameGeometry()
        cp = QApplication.primaryScreen().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

        # Eventos
        self.ui.pushButton_2.clicked.connect(self.on_login_clicked)
        self.ui.pushButton.pressed.connect(self.mostrar_senha)
        self.ui.pushButton.released.connect(self.ocultar_senha)
        self.ui.pushButton_3.clicked.connect(self.voltar_login_aguarde)

    def limpar_dados(self):
        self.ui.label_alerta.clear()

    def voltar_login_aguarde(self):
        self.ui.label_alerta.setStyleSheet("color: #1E90FF; font-weight: bold")
        self.ui.label_alerta.setText("Aguarde...")
        QTimer.singleShot(300, self.voltar_login)

    def voltar_login(self):
        from tela_login import MeuApp
        self.login_window = MeuApp()
        self.login_window.show()
        self.close()

    def mostrar_senha(self):
        self.ui.lineEdit_2.setEchoMode(QLineEdit.Normal)

    def ocultar_senha(self):
        self.ui.lineEdit_2.setEchoMode(QLineEdit.Password)

    #Recovery
    def on_login_clicked(self):
        cpf = self.ui.lineEdit.text().strip()
        nova_senha = self.ui.lineEdit_2.text().strip()

        if not cpf or not nova_senha:
            self.ui.label_alerta.setStyleSheet("color: #f22222; font-weight: bold")
            self.ui.label_alerta.setText("Preencha CPF e nova senha!")
            QTimer.singleShot(2500, self.limpar_dados)
            return

        consulta = "SELECT CPF FROM TABELA_LOGMARKET_USUARIOS WHERE CPF = ?"

        try:
            cursor.execute(consulta, (cpf,))
            resultado = cursor.fetchone()

        except Exception as erro:
            self.ui.label_alerta.setStyleSheet("color: #f22222; font-weight: bold")
            self.ui.label_alerta.setText("Erro ao acessar banco!")
            print("ERRO SQL:", erro)
            QTimer.singleShot(2000, self.limpar_dados)
            return

        # CPF encontrado
        if resultado:
            try:
                alteracao = "UPDATE TABELA_LOGMARKET_USUARIOS SET SENHA = ? WHERE CPF = ?"
                cursor.execute(alteracao, (nova_senha, cpf))
                conn.commit()

            except Exception as erro:
                self.ui.label_alerta.setStyleSheet("color: #f22222; font-weight: bold")
                self.ui.label_alerta.setText("Erro ao atualizar senha!")
                print("ERRO UPDATE:", erro)
                QTimer.singleShot(2500, self.limpar_dados)
                return

            self.ui.label_alerta.setStyleSheet("color: #28a745; font-weight: bold")
            self.ui.label_alerta.setText("Senha atualizada!")
            QTimer.singleShot(1000, self.voltar_login)
            return

        # CPF não encontrado
        self.ui.label_alerta.setStyleSheet("color: #f22222; font-weight: bold")
        self.ui.label_alerta.setText("Usuário não encontrado!")
        self.ui.lineEdit.clear()
        self.ui.lineEdit_2.clear()
        QTimer.singleShot(2500, self.limpar_dados)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("logo_principal.ico"))
    janela = Recovery()
    janela.show()
    sys.exit(app.exec())
