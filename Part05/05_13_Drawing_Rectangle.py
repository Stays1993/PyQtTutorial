from PyQt6.QtGui import QIcon, QFont, QPainter, QPen, QMouseEvent, QPaintEvent
from PyQt6.QtWidgets import QApplication, QWidget
from PyQt6.QtCore import Qt, QRect


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(200, 200, 700, 500)
        self.setWindowTitle("Python 05_13_Drawing_Rectangle.py")
        self.setWindowIcon(QIcon("images/python.png"))

        self.pos_1: list = [0, 0]
        self.pos_2: list = [0, 0]

    """通过鼠标绘制矩形"""

    def paintEvent(self, event: QPaintEvent):
        width = self.pos_2[0] - self.pos_1[0]
        height = self.pos_2[1] - self.pos_1[1]

        painter: QPainter = QPainter()
        painter.begin(self)

        pen: QPen = QPen(Qt.GlobalColor.red, 5)
        painter.setPen(pen)

        painter.drawRect(self.pos_1[0], self.pos_1[1], width, height)

        print(f"绘图：{(self.pos_1[0], self.pos_1[1], width, height)}")

        painter.end()

    def mousePressEvent(self, event: QMouseEvent):
        if event.buttons() & Qt.MouseButton.LeftButton:
            self.pos_1[0], self.pos_1[1] = event.pos().x(), event.pos().y()
            print(f"鼠标点击：{self.pos_1}")

    def mouseReleaseEvent(self, event: QMouseEvent):
        self.pos_2[0], self.pos_2[1] = event.pos().x(), event.pos().y()
        print(f"鼠标释放：{self.pos_2}")
        self.update()


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())
