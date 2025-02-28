from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import (
    QApplication,
    QWidget,
    QTableWidget,
    QTableWidgetItem,
    QVBoxLayout,
)


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(400, 400, 500, 300)
        self.setWindowTitle("Python 02_31_QTableWidget")
        self.setWindowIcon(QIcon("images/python.png"))

        vbox = QVBoxLayout()

        table_widget = QTableWidget()
        # 设置表格行数
        table_widget.setRowCount(3)
        # 设置表格列数
        table_widget.setColumnCount(3)

        # 向表格里添加内容
        table_widget.setItem(0, 0, QTableWidgetItem("Name"))
        table_widget.setItem(0, 1, QTableWidgetItem("Email"))
        table_widget.setItem(0, 2, QTableWidgetItem("Phone"))

        table_widget.setItem(1, 0, QTableWidgetItem("A"))
        table_widget.setItem(1, 1, QTableWidgetItem("A@qq.com"))
        table_widget.setItem(1, 2, QTableWidgetItem("123"))

        table_widget.setItem(2, 0, QTableWidgetItem("B"))
        table_widget.setItem(2, 1, QTableWidgetItem("B@qq.com"))
        table_widget.setItem(2, 2, QTableWidgetItem("456"))

        vbox.addWidget(table_widget)

        self.setLayout(vbox)


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())
