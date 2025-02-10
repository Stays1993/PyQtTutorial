from PyQt6.QtGui import QIcon  # 导入QIcon类
from PyQt6.QtWidgets import QApplication, QWidget  # 导入QApplication和QWidget类

import sys  # 导入sys模块


class Window(QWidget):  # 定义Window类，继承自QWidget
    def __init__(self):  # 定义构造函数
        super().__init__()  # 调用父类构造函数

        # 设置窗口X位置，Y位置，高度，宽度
        self.setGeometry(0, 0, 800, 600)

        # 设置窗口标题
        self.setWindowTitle("PyQt6 QLineEdit")  # 设置窗体标题

        # 设置窗口图标
        self.setWindowIcon(QIcon("images/python.png"))  # 设置窗体图标

        # 调用单行文本函数
        self.create_line_edit()

    # ----------------------------
    # 1. 创建单行文本
    # ----------------------------
    def create_line_edit(self):
        """
        创建单行文本
        :return:
        """
        from PyQt6.QtWidgets import QLineEdit
        from PyQt6.QtGui import QFont

        line_edit = QLineEdit(self)  # 创建单行文本对象
        line_edit.setFont(QFont('Sanserif', 15))  # 设置字体样式，大小
        # line_edit.setText('Default Text')  # 设置默认文本
        line_edit.setPlaceholderText('请输入您的用户名')  # 设置提示文本/占位符
        # line_edit.setEnabled(False)  # 设置禁用编辑，默认为启用编辑
        # line_edit.setEchoMode(QLineEdit.EchoMode.Password)  # 设置文本框的回显模式为密码模式，


app = QApplication(sys.argv)  # 创建QApplication对象
window = Window()  # 创建Window对象
window.show()  # 显示窗体
sys.exit(app.exec())  # 进入应用程序的主循环，并等待退出
