# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Modelo_QT.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDialog, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QWidget)
import sprites

class Ui_Recovery(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(500, 400)
        Dialog.setMinimumSize(QSize(500, 400))
        Dialog.setMaximumSize(QSize(500, 400))
        Dialog.setStyleSheet(u"background-color: #2c3e50; /* Cor escura */\n"
"")
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(200, 18, 131, 25))
        self.label.setMaximumSize(QSize(16777215, 25))
        self.label.setStyleSheet(u"font-family: Roboto;\n"
"font-size: 16pt;\n"
"border-bottom-color: rgb(221, 221, 221);\n"
"color: #ecf0f1	;")
        self.label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(200, 50, 111, 71))
        self.label_2.setStyleSheet(u"image: url(:/sprites/person-circle.svg);")
        self.pushButton_2 = QPushButton(Dialog)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(200, 310, 120, 35))
        self.pushButton_2.setMinimumSize(QSize(110, 35))
        self.pushButton_2.setMaximumSize(QSize(120, 35))
        self.pushButton_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_2.setStyleSheet(u"QPushButton {\n"
"font-family: Roboto;\n"
"background-color:#3498db;\n"
"border-radius: 5px;\n"
"border: 1px solid black;\n"
"color: white;\n"
"font-weight: bold;\n"
"  \n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #2980b9;      /* Cor quando passar o mouse */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #1c5980;      /* Cor quando pressionado */\n"
"}\n"
"")
        self.lineEdit = QLineEdit(Dialog)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(110, 150, 280, 32))
        self.lineEdit.setMinimumSize(QSize(280, 32))
        self.lineEdit.setMaximumSize(QSize(280, 32))
        self.lineEdit.setSizeIncrement(QSize(0, 0))
        self.lineEdit.setMaxLength(11)
        self.lineEdit.setStyleSheet(u"QLineEdit {\n"
"  background-color: #fff;  /* Fundo branco */\n"
"  color: #222;             /* Texto em azul escuro, mesma cor da janela */\n"
"  border: 2px solid #2c3e50;  /* Borda cinza clara */\n"
"  border-radius: 6px;\n"
"  font-size: 10pt;\n"
"  padding: 6px;\n"
"}\n"
"\n"
"\n"
"QLineEdit:focus {\n"
"  border-color: #5dade2;      /* Azul mais vibrante no foco */\n"
"  box-shadow: 0 0 5px rgba(52, 152, 219, 0.5); /* Leve sombra azul */\n"
"}\n"
"\n"
"QLineEdit::placeholder {\n"
"  color: #95a5a6;             /* Cinza claro para o placeholder */\n"
"}\n"
"\n"
"\n"
"")
        self.lineEdit.setMaxLength(32)
        self.lineEdit.setEchoMode(QLineEdit.Normal)
        self.lineEdit_2 = QLineEdit(Dialog)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(110, 220, 280, 32))
        self.lineEdit_2.setMinimumSize(QSize(280, 32))
        self.lineEdit_2.setMaximumSize(QSize(280, 32))
        self.lineEdit_2.setStyleSheet(u"QLineEdit{\n"
"font-family: Roboto;\n"
"border: 2px solid #2c3e50;\n"
"border-radius: 5px;\n"
"padding: 6px;\n"
"background-color: #ecf0f1	;\n"
"color: #222;\n"
"font-size: 10pt;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"  border-color: #5dade2;      /* Azul mais vibrante no foco */\n"
"  box-shadow: 0 0 5px rgba(52, 152, 219, 0.5); /* Leve sombra azul */\n"
"}\n"
"\n"
"")
        self.lineEdit_2.setMaxLength(24)
        self.lineEdit_2.setEchoMode(QLineEdit.Password)
        self.lineEdit_2.setReadOnly(False)
        self.label_3 = QLabel(Dialog)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(110, 130, 51, 10))
        self.label_3.setMaximumSize(QSize(16777215, 10))
        self.label_3.setStyleSheet(u"font-family: Roboto;\n"
"font-size: 8pt;\n"
"color: #ecf0f1	;\n"
"font-weight: bold")
        self.label_alerta = QLabel(Dialog)
        self.label_alerta.setObjectName("label_sucesso")
        self.label_alerta.setGeometry(QRect(110, 261, 280, 20))  # Ajuste a posição e tamanho
        self.label_alerta.setStyleSheet("color: #28a745; font-weight: bold;")
        self.label_alerta.setText("")
        self.label_5 = QLabel(Dialog)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(110, 200, 81, 10))
        self.label_5.setMaximumSize(QSize(16777215, 10))
        self.label_5.setStyleSheet(u"font-family: Roboto;\n"
"font-size: 8pt;\n"
"color: #ecf0f1	;\n"
"font-weight: bold")
        self.pushButton = QPushButton(Dialog)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(360, 230, 18, 15))
        self.pushButton.setMinimumSize(QSize(18, 15))
        self.pushButton.setMaximumSize(QSize(18, 15))
        self.pushButton.setCursor(QCursor(Qt.ArrowCursor))
        self.pushButton.setStyleSheet(u"QPushButton{\n"
"image: url(:/sprites/eye-slash.svg);\n"
"background-repeat: no-repeat;\n"
"background-size: 50x50;\n"
"border: none;\n"
"background: transparent;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    \n"
"	\n"
"	\n"
"	image: url(:/sprites/eye.svg);\n"
"}\n"
"\n"
"\n"
"\n"
"")
        icon = QIcon()
        icon.addFile(u"../Downloads/eye-slash.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QSize(18, 18))
        self.pushButton_3 = QPushButton(Dialog)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(275, 260, 121, 23))
        self.pushButton_3.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_3.setStyleSheet(u"QPushButton{\n"
"font-family: Roboto;\n"
"font-size: 8pt;\n"
"color: #ecf0f1	;\n"
"border: none;\n"
"font-weight: bold;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    color: #2980b9;\n"
"    text-decoration: underline;\n"
"}")
        self.label_2.raise_()
        self.pushButton_2.raise_()
        self.lineEdit.raise_()
        self.lineEdit_2.raise_()
        self.label_3.raise_()
        self.label_5.raise_()
        self.pushButton.raise_()
        self.pushButton_3.raise_()
        self.label.raise_()

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"LogMarket v1.1.3", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Recupera\u00e7\u00e3o", None))
        self.label_2.setText("")
        self.pushButton_2.setText(QCoreApplication.translate("Dialog", u"Confirmar", None))
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("Dialog", u"Digite seu CPF", None))
        self.lineEdit_2.setPlaceholderText(QCoreApplication.translate("Dialog", u"Digite a Nova Senha", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"CPF:", None))
        self.label_5.setText(QCoreApplication.translate("Dialog", u"NOVA SENHA:", None))
        self.pushButton.setText("")
        self.pushButton_3.setText(QCoreApplication.translate("Dialog", u"Voltar ao Login ?", None))
    # retranslateUi

