from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget)
import Background_Image
import sprites_menu

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(700, 600)
        MainWindow.setMinimumSize(QSize(700, 600))
        MainWindow.setMaximumSize(QSize(700, 600))
        MainWindow.setStyleSheet(u"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"background-color: #2c3e50;\n"
"\n"
"")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(4, 4, 4, 0)
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setMaximumSize(QSize(800, 170))
        self.frame.setStyleSheet(u"")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.widget = QWidget(self.frame)
        self.widget.setObjectName(u"widget")
        self.widget.setMaximumSize(QSize(30, 165))
        self.Refresh = QWidget(self.widget)
        self.Refresh.setObjectName(u"Refresh")
        self.Refresh.setGeometry(QRect(0, 0, 30, 30))
        self.Refresh.setMinimumSize(QSize(30, 30))
        self.Refresh.setMaximumSize(QSize(30, 30))
        self.Refresh.setStyleSheet(u"")
        self.pushButton_3 = QPushButton(self.Refresh)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(0, 0, 30, 30))
        self.pushButton_3.setMinimumSize(QSize(30, 30))
        self.pushButton_3.setMaximumSize(QSize(30, 30))
        self.pushButton_3.setStyleSheet(u"QPushButton{\n"
"	image: url(:/icones/refresh-white.svg);\n"
"    background-color: transparent;\n"
"    border: none;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	image: url(:/icones/refresh-gray.svg);\n"
"}\n"
"\n"
"QPushButton::pressed{\n"
"	image: url(:/icones/refresh.svg);\n"
"}")

        self.horizontalLayout.addWidget(self.widget)

        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMaximumSize(QSize(16777215, 160))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.Logo = QFrame(self.frame_3)
        self.Logo.setObjectName(u"Logo")
        self.Logo.setMinimumSize(QSize(0, 150))
        self.Logo.setMaximumSize(QSize(200, 160))
        self.Logo.setStyleSheet(u"image: url(:/imagens/sprites/logo_principal.png);")
        self.Logo.setFrameShape(QFrame.StyledPanel)
        self.Logo.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_2.addWidget(self.Logo)


        self.horizontalLayout.addWidget(self.frame_3)

        self.widget_2 = QWidget(self.frame)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setMaximumSize(QSize(30, 165))
        self.Logout = QWidget(self.widget_2)
        self.Logout.setObjectName(u"Logout")
        self.Logout.setGeometry(QRect(0, 0, 30, 30))
        self.Logout.setMinimumSize(QSize(30, 30))
        self.Logout.setMaximumSize(QSize(30, 30))
        self.Logout.setStyleSheet(u"")
        self.pushButton_4 = QPushButton(self.Logout)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setGeometry(QRect(0, 0, 30, 30))
        self.pushButton_4.setMinimumSize(QSize(30, 30))
        self.pushButton_4.setMaximumSize(QSize(30, 30))
        self.pushButton_4.setStyleSheet(u"QPushButton{\n"
"	\n"
"	\n"
"	\n"
"	\n"
"	image: url(:/icones/log-out-white.svg);\n"
"    background-color: transparent;\n"
"    border: none;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	\n"
"	image: url(:/icones/log-out-gray.svg);\n"
"}\n"
"\n"
"QPushButton::pressed{\n"
"	\n"
"	\n"
"	image: url(:/icones/log-out-gray.svg);\n"
"}\n"
"")

        self.horizontalLayout.addWidget(self.widget_2)


        self.verticalLayout.addWidget(self.frame)

        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setStyleSheet(u"")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setSpacing(6)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(9, 0, 9, 0)
        self.frame_5 = QFrame(self.frame_2)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMaximumSize(QSize(16777215, 120))
        self.frame_5.setStyleSheet(u"background-color: none;\n"
"")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.widget_5 = QWidget(self.frame_5)
        self.widget_5.setObjectName(u"widget_5")
        self.widget_5.setGeometry(QRect(146, 80, 120, 30))
        self.widget_5.setMaximumSize(QSize(120, 30))
        self.widget_5.setStyleSheet(u"border: 1px solid black;\n"
"border-radius: 5px;")
        self.pushButton = QPushButton(self.widget_5)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(0, 0, 120, 30))
        self.pushButton.setMinimumSize(QSize(120, 30))
        self.pushButton.setMaximumSize(QSize(120, 30))
        self.pushButton.setCursor(Qt.PointingHandCursor)
        self.pushButton.setStyleSheet(u"QPushButton{\n"
"	background-color: #3B82F6;\n"
"	color: white;\n"
"	font-weight: bold;\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"	background-color: #2563EB;\n"
"}\n"
"\n"
"QPushButton::pressed{\n"
"	background-color: #1E40AF;\n"
"}\n"
"")
        self.widget_6 = QWidget(self.frame_5)
        self.widget_6.setObjectName(u"widget_6")
        self.widget_6.setGeometry(QRect(426, 80, 120, 30))
        self.widget_6.setMaximumSize(QSize(120, 30))
        self.widget_6.setStyleSheet(u"border: 1px solid black;\n"
"border-radius: 5px;")
        self.pushButton_2 = QPushButton(self.widget_6)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(0, 0, 120, 30))
        self.pushButton_2.setMinimumSize(QSize(120, 30))
        self.pushButton_2.setMaximumSize(QSize(120, 30))
        self.pushButton_2.setCursor(Qt.PointingHandCursor)
        self.pushButton_2.setStyleSheet(u"QPushButton{\n"
"	background-color: #3B82F6;\n"
"	color: white;\n"
"	font-weight: bold;\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"	background-color: #2563EB;\n"
"}\n"
"\n"
"QPushButton::pressed{\n"
"	background-color: #1E40AF;\n"
"}\n"
"")
        self.Input_Pesquisar = QLineEdit(self.frame_5)
        self.Input_Pesquisar.setObjectName(u"Input_Pesquisar")
        self.Input_Pesquisar.setGeometry(QRect(146, 15, 400, 30))
        self.Input_Pesquisar.setMinimumSize(QSize(400, 30))
        self.Input_Pesquisar.setMaximumSize(QSize(400, 30))
        self.Input_Pesquisar.setStyleSheet(u"border: 1px solid black;\n"
"border-radius: 5px;\n"
"padding-left: 5px;\n"
"background-color: #EAEAEA;")
        self.Input_Pesquisar.setMaxLength(64)

        self.verticalLayout_2.addWidget(self.frame_5)

        self.frame_6 = QFrame(self.frame_2)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setMaximumSize(QSize(16777215, 250))
        self.frame_6.setStyleSheet(u"border: 1px solid white;\n"
"border-radius: 5px;\n"
"")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_6)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(-1, -1, 9, 0)
        self.frame_7 = QFrame(self.frame_6)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setMaximumSize(QSize(670, 30))
        self.frame_7.setStyleSheet(u"border: none;")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.Label_Titulo = QLabel(self.frame_7)
        self.Label_Titulo.setObjectName(u"Label_Titulo")
        self.Label_Titulo.setGeometry(QRect(0, 0, 650, 30))
        self.Label_Titulo.setMinimumSize(QSize(600, 30))
        self.Label_Titulo.setMaximumSize(QSize(650, 30))
        self.Label_Titulo.setStyleSheet(u"font: 75 8pt \"System\";\n"
"color: white;")
        self.Label_Titulo.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.frame_7)

        self.frame_8 = QFrame(self.frame_6)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setLayoutDirection(Qt.LeftToRight)
        self.frame_8.setStyleSheet(u"border: none;")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.Label_Codigo = QLabel(self.frame_8)
        self.Label_Codigo.setObjectName(u"Label_Codigo")
        self.Label_Codigo.setGeometry(QRect(40, 15, 75, 30))
        self.Label_Codigo.setMaximumSize(QSize(75, 30))
        self.Label_Codigo.setStyleSheet(u"font: 75 12pt \"System\";\n"
"border: 1px solid black;\n"
"border-radius: 5px;\n"
"background-color: 	#D3D3D3;")
        self.Label_Codigo.setAlignment(Qt.AlignCenter)
        self.Label_Nome = QLabel(self.frame_8)
        self.Label_Nome.setObjectName(u"Label_Nome")
        self.Label_Nome.setGeometry(QRect(220, 15, 75, 30))
        self.Label_Nome.setMinimumSize(QSize(75, 30))
        self.Label_Nome.setMaximumSize(QSize(75, 30))
        self.Label_Nome.setStyleSheet(u"font: 75 12pt \"System\";\n"
"border: 1px solid black;\n"
"border-radius: 5px;\n"
"background-color: 	#D3D3D3;\n"
"")
        self.Label_Nome.setAlignment(Qt.AlignCenter)
        self.Input_Codigo = QLineEdit(self.frame_8)
        self.Input_Codigo.setEnabled(False)
        self.Input_Codigo.setObjectName(u"Input_Codigo")
        self.Input_Codigo.setGeometry(QRect(110, 15, 60, 30))
        self.Input_Codigo.setStyleSheet(u"border: 1px solid rgba(255, 255, 255, 0.6);\n"
"border-radius: 5px;\n"
"border-left: none;\n"
"color: white;\n"
"font: 75 12pt \"MS Sans Serif\";\n"
"")
        self.Input_Codigo.setMaxLength(16)
        self.Input_Codigo.setAlignment(Qt.AlignCenter)
        self.Input_Nome = QLineEdit(self.frame_8)
        self.Input_Nome.setEnabled(False)
        self.Input_Nome.setObjectName(u"Input_Nome")
        self.Input_Nome.setGeometry(QRect(290, 15, 320, 30))
        self.Input_Nome.setMinimumSize(QSize(320, 0))
        self.Input_Nome.setMaximumSize(QSize(320, 16777215))
        self.Input_Nome.setStyleSheet(u"border: 1px solid rgba(255, 255, 255, 0.6);\n"
"border-radius: 5px;\n"
"border-left: none;\n"
"color: white;\n"
"font: 75 12pt \"MS Sans Serif\";\n"
"")
        self.Input_Nome.setMaxLength(64)
        self.Input_Nome.setAlignment(Qt.AlignCenter)
        self.Input_Nome.raise_()
        self.Input_Codigo.raise_()
        self.Label_Codigo.raise_()
        self.Label_Nome.raise_()

        self.verticalLayout_3.addWidget(self.frame_8)

        self.frame_9 = QFrame(self.frame_6)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setStyleSheet(u"border: none;")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.Label_Marca = QLabel(self.frame_9)
        self.Label_Marca.setObjectName(u"Label_Marca")
        self.Label_Marca.setGeometry(QRect(40, 15, 75, 30))
        self.Label_Marca.setMinimumSize(QSize(75, 30))
        self.Label_Marca.setMaximumSize(QSize(75, 30))
        self.Label_Marca.setStyleSheet(u"font: 75 12pt \"System\";\n"
"border: 1px solid black;\n"
"border-radius: 5px;\n"
"background-color:	#D3D3D3;\n"
"")
        self.Label_Marca.setAlignment(Qt.AlignCenter)
        self.Label_Modelo = QLabel(self.frame_9)
        self.Label_Modelo.setObjectName(u"Label_Modelo")
        self.Label_Modelo.setGeometry(QRect(310, 15, 75, 30))
        self.Label_Modelo.setMinimumSize(QSize(75, 30))
        self.Label_Modelo.setMaximumSize(QSize(75, 30))
        self.Label_Modelo.setStyleSheet(u"font: 75 12pt \"System\";\n"
"border: 1px solid black;\n"
"border-radius: 5px;\n"
"background-color: 	#D3D3D3;\n"
"")
        self.Label_Modelo.setAlignment(Qt.AlignCenter)
        self.Input_Marca = QLineEdit(self.frame_9)
        self.Input_Marca.setEnabled(False)
        self.Input_Marca.setObjectName(u"Input_Marca")
        self.Input_Marca.setGeometry(QRect(110, 15, 150, 30))
        self.Input_Marca.setMinimumSize(QSize(150, 30))
        self.Input_Marca.setMaximumSize(QSize(150, 30))
        self.Input_Marca.setStyleSheet(u"border: 1px solid rgba(255, 255, 255, 0.6);\n"
"border-radius: 5px;\n"
"border-left: none;\n"
"color: white;\n"
"font: 75 12pt \"MS Sans Serif\";\n"
"")
        self.Input_Marca.setMaxLength(64)
        self.Input_Marca.setAlignment(Qt.AlignCenter)
        self.Input_Modelo = QLineEdit(self.frame_9)
        self.Input_Modelo.setObjectName(u"Input_Modelo")
        self.Input_Modelo.setEnabled(False)
        self.Input_Modelo.setGeometry(QRect(380, 15, 230, 30))
        self.Input_Modelo.setMinimumSize(QSize(230, 0))
        self.Input_Modelo.setMaximumSize(QSize(230, 16777215))
        self.Input_Modelo.setStyleSheet(u"border: 1px solid rgba(255, 255, 255, 0.6);\n"
"border-radius: 5px;\n"
"border-left: none;\n"
"color: white;\n"
"font: 75 12pt \"MS Sans Serif\";\n"
"")
        self.Input_Modelo.setMaxLength(64)
        self.Input_Modelo.setAlignment(Qt.AlignCenter)
        self.Input_Modelo.raise_()
        self.Input_Marca.raise_()
        self.Label_Marca.raise_()
        self.Label_Modelo.raise_()

        self.verticalLayout_3.addWidget(self.frame_9)

        self.frame_10 = QFrame(self.frame_6)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setStyleSheet(u"border: none;")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.Label_Valor = QLabel(self.frame_10)
        self.Label_Valor.setObjectName(u"Label_Valor")
        self.Label_Valor.setGeometry(QRect(280, 15, 75, 30))
        self.Label_Valor.setMaximumSize(QSize(75, 30))
        self.Label_Valor.setStyleSheet(u"font: 75 12pt \"System\";\n"
"border: 1px solid black;\n"
"border-radius: 5px;\n"
"background-color: rgba(40, 167, 69, 150);")
        self.Label_Valor.setAlignment(Qt.AlignCenter)
        self.Label_Unidade = QLabel(self.frame_10)
        self.Label_Unidade.setObjectName(u"Label_Unidade")
        self.Label_Unidade.setGeometry(QRect(40, 15, 75, 30))
        self.Label_Unidade.setMinimumSize(QSize(75, 30))
        self.Label_Unidade.setMaximumSize(QSize(75, 30))
        self.Label_Unidade.setStyleSheet(u"font: 75 12pt \"System\";\n"
"border: 1px solid black;\n"
"border-radius: 5px;\n"
"background-color: 	#D3D3D3;\n"
"")
        self.Label_Unidade.setAlignment(Qt.AlignCenter)
        self.Input_Unidade = QLineEdit(self.frame_10)
        self.Input_Unidade.setObjectName(u"Input_Unidade")
        self.Input_Unidade.setEnabled(False)
        self.Input_Unidade.setGeometry(QRect(110, 15, 120, 30))
        self.Input_Unidade.setMinimumSize(QSize(120, 30))
        self.Input_Unidade.setMaximumSize(QSize(120, 30))
        self.Input_Unidade.setStyleSheet(u"border: 1px solid rgba(255, 255, 255, 0.6);\n"
"border-radius: 5px;\n"
"border-left: none;\n"
"color: white;\n"
"font: 75 12pt \"MS Sans Serif\";\n"
"")
        self.Input_Unidade.setMaxLength(16)
        self.Input_Unidade.setAlignment(Qt.AlignCenter)
        self.Input_Valor = QLineEdit(self.frame_10)
        self.Input_Valor.setEnabled(False)
        self.Input_Valor.setObjectName(u"Input_Valor")
        self.Input_Valor.setGeometry(QRect(350, 15, 260, 30))
        self.Input_Valor.setMinimumSize(QSize(260, 0))
        self.Input_Valor.setMaximumSize(QSize(260, 16777215))
        self.Input_Valor.setStyleSheet(u"border: 1px solid rgba(255, 255, 255, 0.6);\n"
"border-radius: 5px;\n"
"border-left: none;\n"
"color: white;\n"
"font: 75 12pt \"MS Sans Serif\";\n"
"padding-left: 5px;\n"
"")
        self.Input_Valor.setMaxLength(16)
        self.Input_Valor.setAlignment(Qt.AlignCenter)
        self.Input_Valor.raise_()
        self.Input_Unidade.raise_()
        self.Label_Valor.raise_()
        self.Label_Unidade.raise_()

        self.verticalLayout_3.addWidget(self.frame_10)

        self.frame_11 = QFrame(self.frame_6)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setMaximumSize(QSize(16777215, 20))
        self.frame_11.setStyleSheet(u"border: none;")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.Label_Autor = QLabel(self.frame_11)
        self.Label_Autor.setObjectName(u"Label_Autor")
        self.Label_Autor.setGeometry(QRect(0, 0, 650, 20))
        self.Label_Autor.setMinimumSize(QSize(650, 0))
        self.Label_Autor.setMaximumSize(QSize(650, 20))
        self.Label_Autor.setStyleSheet(u"color: white;\n"
"font-weight: bold;")
        self.Label_Autor.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout_3.addWidget(self.frame_11)


        self.verticalLayout_2.addWidget(self.frame_6)


        self.verticalLayout.addWidget(self.frame_2)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"LogMarket v1.1.3", None))
        self.pushButton_3.setText("")
        self.pushButton_4.setText("")
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"CONSULTAR", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"CADASTRAR", None))
        self.Input_Pesquisar.setText("")
        self.Input_Pesquisar.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Pesquisar...", None))
        self.Label_Titulo.setText(QCoreApplication.translate("MainWindow", u"SOBRE O PRODUTO", None))
        self.Label_Codigo.setText(QCoreApplication.translate("MainWindow", u"CODIGO", None))
        self.Label_Nome.setText(QCoreApplication.translate("MainWindow", u"NOME", None))
        self.Input_Codigo.setText(QCoreApplication.translate("MainWindow", u"", None))
        self.Input_Nome.setText(QCoreApplication.translate("MainWindow", u"", None))
        self.Label_Marca.setText(QCoreApplication.translate("MainWindow", u"MARCA", None))
        self.Label_Modelo.setText(QCoreApplication.translate("MainWindow", u"MODELO", None))
        self.Input_Marca.setText(QCoreApplication.translate("MainWindow", u"", None))
        self.Input_Modelo.setText(QCoreApplication.translate("MainWindow", u"", None))
        self.Label_Valor.setText(QCoreApplication.translate("MainWindow", u"VALOR R$", None))
        self.Label_Unidade.setText(QCoreApplication.translate("MainWindow", u"UNIDADE", None))
        self.Input_Unidade.setText(QCoreApplication.translate("MainWindow", u"", None))
        self.Input_Valor.setText(QCoreApplication.translate("MainWindow", u"", None))
        self.Label_Autor.setText(QCoreApplication.translate("MainWindow", u"Feito por Davi Almeida ", None))
    # retranslateUi

