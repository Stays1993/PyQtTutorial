from PyQt6.QtGui import QIcon, QPainter, QTextDocument
from PyQt6.QtWidgets import QApplication, QWidget
from PyQt6.QtCore import QRect, Qt, QRectF


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(400, 400, 500, 300)
        self.setWindowTitle("PyQt6 05_04_QPainter_Text")
        self.setWindowIcon(QIcon("images/python.png"))

    def paintEvent(self, event):
        painter: QPainter = QPainter(self)

        painter.drawText(50, 50, "PyQt6 Course")

        rect: QRect = QRect(100, 150, 250, 25)
        painter.drawRect(rect)
        painter.drawText(rect, Qt.AlignmentFlag.AlignCenter, "Hello World !")

        document: QTextDocument = QTextDocument()
        rect_f: QRectF = QRectF(0, 0, 250, 250)
        document.setTextWidth(rect_f.width())
        document.setHtml(
            "<b>Welcome to PyQt6 Course</b>"
            "<i>Hello Python !</i>"
            "<font size='15' color='red'>Welcome to Python</font>"
        )
        document.drawContents(painter, rect_f)


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())
