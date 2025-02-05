from PyQt6.QtWidgets import QApplication, QWidget  # 导入QWidget类
from PyQt6 import uic  # 导入uic模块
import sys


class UI(QWidget):  # 定义UI类，继承自QWidget
    def __init__(self):  # 定义构造函数
        super().__init__()  # 调用父类构造函数

        uic.loadUi("1.8_WindowUI.ui", self)  # 加载UI文件


app = QApplication(sys.argv)
window = UI()
window.show()
sys.exit(app.exec())
