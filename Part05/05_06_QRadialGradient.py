from PyQt6.QtGui import QIcon, QRadialGradient, QPainter, QPen, QBrush
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QWidget


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(200, 200, 700, 500)
        self.setWindowTitle("Python 05_06_QRadialGradient")
        self.setWindowIcon(QIcon("images/python.png"))

    def paintEvent(self, event):
        painter: QPainter = QPainter(self)
        painter.setPen(QPen(Qt.GlobalColor.black, 4, Qt.PenStyle.SolidLine))

        radial_gradient: QRadialGradient = QRadialGradient(100, 100, 100)
        radial_gradient.setColorAt(0.4, Qt.GlobalColor.darkGray)
        radial_gradient.setColorAt(0.8, Qt.GlobalColor.green)
        radial_gradient.setColorAt(1.0, Qt.GlobalColor.yellow)
        painter.setBrush(QBrush(radial_gradient))

        painter.drawRect(10, 10, 200, 200)


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())
