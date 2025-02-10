from PyQt6.QtGui import QHelpEvent, QIcon  # 导入QIcon类
from PyQt6.QtWidgets import QApplication,  QWidget  # 导入QApplication和QWidget类

import sys  # 导入sys模块


class Window(QWidget):  # 定义Window类，继承自QWidget
    def __init__(self):  # 定义构造函数
        super().__init__()  # 调用父类构造函数

        # 设置窗口X位置，Y位置，高度，宽度
        self.setGeometry(0, 0, 800, 600)

        # 设置窗口标题
        self.setWindowTitle("PyQt6 QHboxLayout")  # 设置窗体标题

        # 设置窗口图标
        self.setWindowIcon(QIcon("images/python.png"))  # 设置窗体图标

        # 调用函数创建QHBoxLayout布局
        self.create_hbox()

    # ----------------------------
    # 1. 创建水平对齐布局
    # ----------------------------
    def create_hbox(self):
        """
        创建QHBoxLayout布局
        :return:
        """
        from PyQt6.QtWidgets import QHBoxLayout, QPushButton

        hbox = QHBoxLayout()  # 创建QHBoxLayout对象

        btn1 = QPushButton('Click One')  # 创建按钮控件对象
        btn2 = QPushButton('Click Two')  # 创建按钮控件对象
        btn3 = QPushButton('Click Three')  # 创建按钮控件对象
        btn4 = QPushButton('Click Four')  # 创建按钮控件对象

        hbox.addWidget(btn1)  # 添加按钮控件到hbox布局中
        hbox.addWidget(btn2)  # 添加按钮控件到hbox布局中
        hbox.addWidget(btn3)  # 添加按钮控件到hbox布局中
        hbox.addWidget(btn4)  # 添加按钮控件到hbox布局中

        # hbox.addSpacing(100)  # 添加固定间距
        # hbox.addStretch(100)  # 添加弹性间距，适合需要动态调整布局的场景。

        self.setLayout(hbox)  # 设置主窗口布局为hbox


app = QApplication(sys.argv)  # 创建QApplication对象
window = Window()  # 创建Window对象
window.show()  # 显示窗体
sys.exit(app.exec())  # 进入应用程序的主循环，并等待退出
