from PyQt6.QtGui import QIcon, QConicalGradient, QPen, QPainter, QBrush
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QWidget


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(200, 200, 700, 500)
        self.setWindowTitle("PyQt6 05_07_QConicalGRadient")
        self.setWindowIcon(QIcon("images/python.png"))

    def paintEvent(self, event):
        painter: QPainter = QPainter(self)
        painter.setPen(QPen(Qt.GlobalColor.red, 5, Qt.PenStyle.SolidLine))

        conical_gradient = QConicalGradient(100, 100, 10)

        conical_gradient.setColorAt(0.0, Qt.GlobalColor.red)
        conical_gradient.setColorAt(0.8, Qt.GlobalColor.green)
        conical_gradient.setColorAt(1.0, Qt.GlobalColor.yellow)

        painter.setBrush(QBrush(conical_gradient))

        painter.drawRect(10, 10, 200, 200)


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())
