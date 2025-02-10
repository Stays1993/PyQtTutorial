from PyQt6.QtGui import QIcon  # 导入QIcon类
from PyQt6.QtWidgets import QApplication, QWidget  # 导入QApplication和QWidget类

import sys  # 导入sys模块


class Window(QWidget):  # 定义Window类，继承自QWidget
    def __init__(self):  # 定义构造函数
        super().__init__()  # 调用父类构造函数

        # 设置窗口X位置，Y位置，高度，宽度
        self.setGeometry(0, 0, 800, 600)

        # 设置窗口标题
        self.setWindowTitle("PyQt6 QPushButton")  # 设置窗体标题

        # 设置窗口图标
        self.setWindowIcon(QIcon("images/python.png"))  # 设置窗体图标

        # 调用按钮函数
        self.create_button()

    # ----------------------------
    # 1. 创建按钮
    # ----------------------------
    def create_button(self):
        """
        创建一个按钮
        :return:
        """
        from PyQt6.QtWidgets import QPushButton, QMenu
        from PyQt6.QtGui import QFont, QIcon
        from PyQt6.QtCore import QSize

        btn = QPushButton('Click', self)  # 创建按钮对象
        btn.setGeometry(100, 100, 130, 130)  # 设置按钮的X, Y位置以及按钮的宽度和高度
        btn.setFont(QFont('Times', 20, QFont.Weight.ExtraBold))  # 设置字体样式，大小，加粗
        btn.setIcon(QIcon('images/python.png'))  # 设置按钮图标
        btn.setIconSize(QSize(36, 36))  # 设置图标宽度，高度

        # 设置点击后出现菜单
        menu = QMenu()  # 创建菜单对象
        menu.setFont(QFont('Times', 14, QFont.Weight.ExtraBold))  # 设置菜单字体样式，大小，加粗
        menu.setStyleSheet('background-color:green')  # 设置菜单背景颜色
        menu.addAction('Copy/复制')  # 添加菜单内容
        menu.addAction('Cut/剪切')  # 添加菜单内容
        menu.addAction('Paste/粘贴')  # 添加菜单内容

        btn.setMenu(menu)  # 按钮添加菜单对象


app = QApplication(sys.argv)  # 创建QApplication对象
window = Window()  # 创建Window对象
window.show()  # 显示窗体
sys.exit(app.exec())  # 进入应用程序的主循环，并等待退出
