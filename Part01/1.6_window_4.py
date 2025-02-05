from PyQt6.QtGui import QIcon  # 导入QIcon类
from PyQt6.QtWidgets import QApplication, QWidget  # 导入QApplication和QWidget类

import sys  # 导入sys模块


class Window(QWidget):  # 定义Window类，继承自QWidget
    def __init__(self):  # 定义构造函数
        super().__init__()  # 调用父类构造函数

        # 设置窗口X位置，Y位置，高度，宽度
        # self.setGeometry(200, 200, 700, 400)

        # 设置窗口标题
        self.setWindowTitle("Python GUI Development")  # 设置窗体标题

        # 设置窗口图标
        self.setWindowIcon(QIcon("images/python.png"))  # 设置窗体图标

        # 固定窗口大小
        # self.setFixedWidth(700)
        # self.setFixedHeight(400)

        # 设置窗口背景颜色
        self.setStyleSheet("background-color:green")  # 设置窗体背景颜色

        # 设置窗口透明度：0 - 1
        self.setWindowOpacity(0.5)  # 设置窗体透明度


app = QApplication(sys.argv)  # 创建QApplication对象
window = Window()  # 创建Window对象
window.show()  # 显示窗体
sys.exit(app.exec())  # 进入应用程序的主循环，并等待退出
