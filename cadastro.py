from PySide6.QtWidgets import (QApplication, QDialog, QVBoxLayout, QLineEdit, QPushButton, QFormLayout, QMessageBox, QDoubleSpinBox)
import sys

class DialogCadastro(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Cadastrar Produto")
        self.setFixedSize(300, 250)

        # Campos
        self.input_codigo = QLineEdit()
        self.input_nome = QLineEdit()
        self.input_marca = QLineEdit()
        self.input_modelo = QLineEdit()
        self.input_unidade = QDoubleSpinBox()
        self.input_unidade.setRange(0, 999999)
        self.input_unidade.setDecimals(0)
        self.input_preco = QDoubleSpinBox()
        self.input_preco.setPrefix("R$ ")
        self.input_preco.setRange(0, 99999.99)
        self.input_preco.setDecimals(2)

        # Layout
        layout_form = QFormLayout()
        layout_form.addRow("Código:", self.input_codigo)
        layout_form.addRow("Nome:", self.input_nome)
        layout_form.addRow("Marca:", self.input_marca)
        layout_form.addRow("Modelo:", self.input_modelo)
        layout_form.addRow("Unidade:", self.input_unidade)
        layout_form.addRow("Preço:", self.input_preco)

        # Botões
        self.btn_salvar = QPushButton("Salvar")
        self.btn_cancelar = QPushButton("Cancelar")
        self.btn_salvar.clicked.connect(self.salvar)
        self.btn_cancelar.clicked.connect(self.reject)

        # Widgets
        layout_principal = QVBoxLayout()
        layout_principal.addLayout(layout_form)
        layout_principal.addWidget(self.btn_salvar)
        layout_principal.addWidget(self.btn_cancelar)

        self.setLayout(layout_principal)
        self.input_codigo.setFocus()

    def salvar(self):
        # Pega os valores
        self.codigo = self.input_codigo.text().strip()
        self.nome = self.input_nome.text().strip()
        self.marca = self.input_marca.text().strip()
        self.modelo = self.input_modelo.text().strip()
        self.unidade = int(self.input_unidade.value())
        self.preco = self.input_preco.value()

        # Valida campos
        if not all([self.codigo, self.nome, self.marca, self.modelo, self.unidade]) or self.preco == 0:
            QMessageBox.warning(self, "Erro", "Preencha todos os campos e defina o preço!")
            return
        
        if not self.codigo.isnumeric():
            QMessageBox.warning(self, "Erro", "O código deve conter apenas números!")
            return

        self.accept() # Fecha o diálogo corretamente

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = DialogCadastro()
    window.show()
    sys.exit(app.exec())