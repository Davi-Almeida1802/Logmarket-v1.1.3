from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import QTimer, QPropertyAnimation, QPoint, QEasingCurve, QRect
from PySide6.QtGui import QPainterPath, QRegion, QIcon
from apresentacao import Ui_MainWindow 
from tela_login import MeuApp
import ctypes

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # Aplicar bordas arredondadas na janela
        path = QPainterPath()
        rect = QRect(0, 0, self.width(), self.height())
        path.addRoundedRect(rect, 20, 20)
        region = QRegion(path.toFillPolygon().toPolygon())
        self.setMask(region)
        self.setup_animations()

        # Forçar Alteração do Icone
        myappid = u"icone_projeto"
        ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
        self.setWindowIcon(QIcon("logo_principal.ico"))

    def setup_animations(self):
        # Delay para animar elementos depois da janela aparecer
        QTimer.singleShot(300, self.animate_entry_elements)
        QTimer.singleShot(1200, self.start_progress_animation)

    def animate_entry_elements(self):
        elements = [self.label, self.label_2, self.label_3]
        self.animations = []

        for widget in elements:
            anim = QPropertyAnimation(widget, b"pos")
            anim.setDuration(800)
            anim.setStartValue(widget.pos() + QPoint(0, 40))  
            anim.setEndValue(widget.pos())                 
            anim.setEasingCurve(QEasingCurve.OutCubic)
            anim.start()
            self.animations.append(anim)

    def start_progress_animation(self):
        self.progress_value = 0
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_progress)
        self.timer.start(30)

    def update_progress(self):
        if self.progress_value >= 100:
            self.timer.stop()
            self.label_4.setText("Concluído!")

            # Abre a tela de login
            self.login_window = MeuApp()
            self.login_window.show()

            self.close()  # Fecha a tela de Apresentação
        else:
            self.progress_value += 1
            self.progressBar.setValue(self.progress_value)

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("logo_principal.ico"))
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
