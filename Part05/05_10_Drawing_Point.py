from PyQt6.QtGui import QIcon, QFont, QPainter, QPen, QMouseEvent
from PyQt6.QtWidgets import QApplication, QWidget
from PyQt6.QtCore import Qt


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(200, 200, 700, 500)
        self.setWindowTitle("PyQt6 05_10_Drawing_Point")
        self.setWindowIcon(QIcon("images/python.png"))

        self.pos_1 = [0, 0]
        self.setMouseTracking(True)

    """通过单击绘制点"""

    def paintEvent(self, event):
        painter: QPainter = QPainter()
        painter.begin(self)

        pen: QPen = QPen(Qt.GlobalColor.red, 15)
        painter.setPen(pen)

        painter.drawPoint(self.pos_1[0], self.pos_1[1])

        painter.end()

    def mousePressEvent(self, event: QMouseEvent):
        if event.buttons() & Qt.MouseButton.LeftButton:
            self.pos_1[0], self.pos_1[1] = event.pos().x(), event.pos().y()
            self.update()


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())
