from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QMainWindow, QProgressBar, QSizePolicy, QVBoxLayout,
    QWidget)
import logo

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(700, 600)
        MainWindow.setStyleSheet(u"-background-color: rgb(0, 150, 170);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"QWidget{\n"
"	background-color: rgba(0, 60, 90,1);\n"
"	color: #fff\n"
"}")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(100, 100))
        self.label.setMaximumSize(QSize(250, 250))
        self.label.setStyleSheet(u"QLabel{\n"
"	image: url(:/logo/logo.png);\n"
"	\n"
"	border-radius: 50px;\n"
"	\n"
"}")
        self.label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.label)


        self.verticalLayout.addWidget(self.frame)

        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_2 = QLabel(self.frame_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"font: 18pt \"Arial\";")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_2)

        self.label_3 = QLabel(self.frame_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setStyleSheet(u"font: 12pt \"Arial\";")
        self.label_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_3)

        self.frame_3 = QFrame(self.frame_2)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMaximumSize(QSize(16777215, 50))
        self.frame_3.setSizeIncrement(QSize(0, 500))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_3)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(30, -1, 30, -1)
        self.label_4 = QLabel(self.frame_3)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setStyleSheet(u"font: 8pt \"Arial\";")
        self.label_4.setAlignment(Qt.AlignBottom|Qt.AlignHCenter)

        self.verticalLayout_3.addWidget(self.label_4)

        self.progressBar = QProgressBar(self.frame_3)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setMaximumSize(QSize(16777215, 10))
        self.progressBar.setStyleSheet(u"QProgressBar {\n"
"background: rgba(255,255,255,180);\n"
"border-style: none;\n"
"border-radius: 5px;\n"
"color: rgba(200,200,200,0);\n"
"text-align: center;\n"
"\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"border-radius: 5px;\n"
"background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(0, 85, 255, 255))\n"
"}")
        self.progressBar.setValue(0)

        self.verticalLayout_3.addWidget(self.progressBar)


        self.verticalLayout_2.addWidget(self.frame_3)

        self.frame_4 = QFrame(self.frame_2)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMaximumSize(QSize(16777215, 40))
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        #self.label_5 = QLabel(self.frame_4)
        #self.label_5.setObjectName(u"label_5")
        #self.label_5.setStyleSheet(u"font: 12pt \"Arial\";")

        #self.horizontalLayout_2.addWidget(self.label_5)

        self.label_6 = QLabel(self.frame_4)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setStyleSheet(u"font: 10pt \"Arial\";")
        self.label_6.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_2.addWidget(self.label_6)


        self.verticalLayout_2.addWidget(self.frame_4)


        self.verticalLayout.addWidget(self.frame_2)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Controle de Estoque e Vendas", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Organize, controle e venda com eficiência", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Carregando...", None))
        #self.label_5.setText(QCoreApplication.translate("MainWindow", u"N", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Feito por Davi Almeida", None))
    # retranslateUi

