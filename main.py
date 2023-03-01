import sys
from random import randint

from PyQt5.QtGui import QPainter, QPen, QColor
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton


class Init(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUi()
    
    def initUi(self):
        self.setGeometry(100, 100, 600, 450)
        self.setWindowTitle('rainbow circles')
        self.pushButton = QPushButton('Хочу радугу', self)


class Circles(Init):
    def __init__(self):
        super().__init__()
        self.initUi()
        
        self.pushButton.clicked.connect(self.run)
        self.do_paint = False
    
    def run(self):
        self.do_paint = True
        self.repaint()
        self.do_paint = False

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw_flag(qp)
            qp.end()

    def draw_flag(self, qp):
        qp.setPen(QPen(QColor(randint(0, 255), randint(0, 255), randint(0, 255)), 2))
        size = randint(20, 150)
        qp.drawEllipse(randint(0, 450), randint(0, 300), size, size)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Circles()
    ex.show()
    sys.exit(app.exec())