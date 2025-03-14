from PyQt6.QtGui import QIcon, QLinearGradient, QPainter, QPen, QBrush
from PyQt6.QtWidgets import QApplication, QWidget
from PyQt6.QtCore import Qt


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(200, 200, 700, 500)
        self.setWindowTitle("PyQt6 05_05_QLinearGradient")
        self.setWindowIcon(QIcon("images/python.png"))

    def paintEvent(self, event):
        painter: QPainter = QPainter(self)
        painter.setPen(QPen(Qt.GlobalColor.black, 4, Qt.PenStyle.SolidLine))

        grad_1: QLinearGradient = QLinearGradient(25, 100, 150, 175)

        grad_1.setColorAt(0.0, Qt.GlobalColor.red)
        grad_1.setColorAt(0.5, Qt.GlobalColor.green)
        grad_1.setColorAt(1.0, Qt.GlobalColor.yellow)

        painter.setBrush(QBrush(grad_1))

        painter.drawRect(10, 10, 200, 200)


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())
