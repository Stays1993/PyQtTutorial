from PyQt6.QtGui import QIcon, QFont
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel
from PyQt6.QtCore import Qt


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(200, 200, 700, 500)
        self.setWindowTitle("Python 05_09_Mouse_Press")
        self.setWindowIcon(QIcon("images/python.png"))

        self.setMouseTracking(True)

        vbox: QVBoxLayout = QVBoxLayout()

        self.label_press: QLabel = QLabel("鼠标按下")
        self.label_press.setFont(QFont("Times", 15))

        self.label_release: QLabel = QLabel("鼠标释放")
        self.label_release.setFont(QFont("Times", 15))

        vbox.addWidget(self.label_press)
        vbox.addWidget(self.label_release)
        self.setLayout(vbox)

    def mousePressEvent(self, event):
        """鼠标按下事件"""
        if event.buttons() & Qt.MouseButton.LeftButton:
            x = self.x()
            y = self.y()

            text = f"X: {x}, Y: {y}"
            self.label_press.setText(text)

    def mouseReleaseEvent(self, event):
        """鼠标释放事件"""
        x = self.x()
        y = self.y()

        text = f"X: {x}, Y: {y}"
        self.label_release.setText(text)
        self.update()


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())
