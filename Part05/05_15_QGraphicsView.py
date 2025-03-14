from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QApplication, QWidget, QGraphicsView


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(200, 200, 700, 500)
        self.setWindowTitle("PyQt6 05_15_QGraphicsView")
        self.setWindowIcon(QIcon("images/python.png"))


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())
