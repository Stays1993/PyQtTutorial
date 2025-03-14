from PyQt6.QtGui import QIcon, QFont, QMouseEvent
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QHBoxLayout


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(200, 200, 700, 500)
        self.setWindowTitle("PyQt6 05_08_Mouse_Move")
        self.setWindowIcon(QIcon("images/python.png"))

        self.setMouseTracking(True)

        hbox: QHBoxLayout = QHBoxLayout()

        self.label: QLabel = QLabel("鼠标轨迹")
        self.label.setFont(QFont("Times", 15, 800))

        hbox.addWidget(self.label)

        self.setLayout(hbox)

    def mouseMoveEvent(self, event: QMouseEvent):
        x = event.pos().x()
        y = event.pos().y()

        text = f"X: {x}, Y: {y}"

        self.label.setText(text)
        self.update()


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())
