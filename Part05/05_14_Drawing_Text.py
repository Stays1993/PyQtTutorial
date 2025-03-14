from PyQt6.QtGui import QIcon, QFont, QPainter, QPen, QColor, QPaintEvent
from PyQt6.QtWidgets import (
    QApplication,
    QWidget,
    QHBoxLayout,
    QPushButton,
    QLineEdit,
    QComboBox,
    QTextEdit,
)
from PyQt6.QtCore import Qt


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(200, 200, 700, 500)
        self.setWindowTitle("PyQt6 05_14_Drawing_Text.py")
        self.setWindowIcon(QIcon("images/python.png"))

        self.text_to_draw = ""
        self.font_size = 5

        hbox: QHBoxLayout = QHBoxLayout()

        self.textEdit: QTextEdit = QTextEdit()
        self.textEdit.setMaximumHeight(200)
        self.textEdit.setText("Hello World!\nHello World!\nHello World!")

        self.combo: QComboBox = QComboBox()
        self.combo.setFont(QFont("times", 18))
        self.combo.addItem("12")
        self.combo.addItem("14")
        self.combo.addItem("16")
        self.combo.addItem("18")

        btn: QPushButton = QPushButton("创建文本")
        btn.setFont(QFont("times", 18))
        # connected signal
        btn.clicked.connect(self.create_text)

        hbox.addWidget(self.textEdit)
        hbox.addWidget(self.combo)
        hbox.addWidget(btn)

        self.setLayout(hbox)

    def paintEvent(self, event: QPaintEvent):
        painter: QPainter = QPainter()
        painter.begin(self)
        painter.setPen(QColor(168, 30, 3))
        painter.setFont(QFont("times", self.font_size))
        painter.drawText(event.rect(), Qt.AlignmentFlag.AlignTop, self.text_to_draw)
        painter.end()

    def create_text(self):
        self.font_size = int(self.combo.itemText(self.combo.currentIndex()))
        self.text_to_draw = self.textEdit.toPlainText()
        self.update()


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())
