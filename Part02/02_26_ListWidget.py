from PyQt6.QtGui import QIcon, QFont
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QListWidget, QLabel


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(400, 400, 500, 300)
        self.setWindowTitle("PyQt6 02_26_ListWidget")
        self.setWindowIcon(QIcon("images/python.png"))

        vbox = QVBoxLayout()

        # 创建列表部件
        self.list_widget: QListWidget = QListWidget()
        # 插入内容
        self.list_widget.insertItem(0, "Python")
        self.list_widget.insertItem(1, "Java")
        self.list_widget.insertItem(2, "C++")
        self.list_widget.insertItem(3, "C#")
        self.list_widget.insertItem(4, "Golang")

        self.list_widget.setFont(QFont("等距更纱黑体 SC", 15, 700))
        self.list_widget.setStyleSheet("background-color: gray")

        self.list_widget.clicked.connect(self.item_clicked)

        self.label: QLabel = QLabel("")
        self.label.setFont(QFont("等距更纱黑体 SC", 15, 700))

        vbox.addWidget(self.list_widget)
        vbox.addWidget(self.label)

        self.setLayout(vbox)

    def item_clicked(self):
        item = self.list_widget.currentItem()
        self.label.setText(f"你的选择项是：{str(item.text())}")


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())
