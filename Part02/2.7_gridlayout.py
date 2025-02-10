from PyQt6.QtGui import QHelpEvent, QIcon  # 导入QIcon类
from PyQt6.QtWidgets import QApplication, QHBoxLayout, QPushButton, QWidget  # 导入QApplication和QWidget类

import sys  # 导入sys模块


class Window(QWidget):  # 定义Window类，继承自QWidget
    def __init__(self):  # 定义构造函数
        super().__init__()  # 调用父类构造函数

        # 设置窗口X位置，Y位置，高度，宽度
        self.setGeometry(0, 0, 800, 600)

        # 设置窗口标题
        self.setWindowTitle("PyQt6 QGridLayout")  # 设置窗体标题

        # 设置窗口图标
        self.setWindowIcon(QIcon("images/python.png"))  # 设置窗体图标

        # 调用函数创建QGridLayout布局
        self.create_gbox()

    # ----------------------------
    # 1. 创建网格对齐布局
    # ----------------------------
    def create_gbox(self):
        """
        创建QVGridLayout布局
        :return:
        """
        from PyQt6.QtWidgets import QGridLayout, QPushButton

        gbox = QGridLayout()  # 创建QGridLayout对象

        btn1 = QPushButton('One')  # 创建按钮控件对象
        btn2 = QPushButton('Two')  # 创建按钮控件对象
        btn3 = QPushButton('Three')  # 创建按钮控件对象
        btn4 = QPushButton('Four')  # 创建按钮控件对象
        btn5 = QPushButton('Five')  # 创建按钮控件对象
        btn6 = QPushButton('Six')  # 创建按钮控件对象
        btn7 = QPushButton('Seven')  # 创建按钮控件对象
        btn8 = QPushButton('Eight')  # 创建按钮控件对象

        gbox.addWidget(btn1, 0, 0)  # 添加按钮控件到hbox布局中, 行号，列号
        gbox.addWidget(btn2, 0, 1)  # 添加按钮控件到hbox布局中, 行号，列号
        gbox.addWidget(btn3, 0, 2)  # 添加按钮控件到hbox布局中, 行号，列号
        gbox.addWidget(btn4, 0, 3)  # 添加按钮控件到hbox布局中, 行号，列号
        gbox.addWidget(btn5, 1, 0)  # 添加按钮控件到hbox布局中, 行号，列号
        gbox.addWidget(btn6, 1, 1)  # 添加按钮控件到hbox布局中, 行号，列号
        gbox.addWidget(btn7, 1, 2)  # 添加按钮控件到hbox布局中, 行号，列号
        gbox.addWidget(btn8, 1, 3)  # 添加按钮控件到hbox布局中, 行号，列号

        '''
        | btn1 | btn2 | btn3 | btn4 |
        | btn5 | btn6 | btn7 | btn8 |
        '''

        self.setLayout(gbox)  # 设置主窗口布局为gbox


app = QApplication(sys.argv)  # 创建QApplication对象
window = Window()  # 创建Window对象
window.show()  # 显示窗体
sys.exit(app.exec())  # 进入应用程序的主循环，并等待退出
