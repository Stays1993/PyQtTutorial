from PyQt6.QtGui import QIcon, QPainter, QPen, QBrush
from PyQt6.QtWidgets import QApplication, QWidget
from PyQt6.QtCore import Qt


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(400, 400, 500, 300)
        self.setWindowTitle("Python 05_02_QPainter_Rectangle.")
        self.setWindowIcon(QIcon("images/python.png"))

    def paintEvent(self, event):
        painter: QPainter = QPainter(self)
        painter.setPen(QPen(Qt.GlobalColor.blue, 5, Qt.PenStyle.SolidLine))
        painter.setBrush(QBrush(Qt.GlobalColor.green, Qt.BrushStyle.SolidPattern))
        painter.drawRect(100, 15, 300, 100)


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())
