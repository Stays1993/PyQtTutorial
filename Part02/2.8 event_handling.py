import sys  # 导入sys模块

from PyQt6.QtGui import QIcon  # 导入QIcon类
from PyQt6.QtWidgets import QApplication, QWidget  # 导入QApplication和QWidget类


class Window(QWidget):  # 定义Window类，继承自QWidget
    def __init__(self):  # 定义构造函数
        super().__init__()  # 调用父类构造函数

        # 设置窗口X位置，Y位置，高度，宽度
        self.setGeometry(2500, 400, 800, 600)

        # 设置窗口标题
        self.setWindowTitle("PyQt6 Event Handling")  # 设置窗体标题

        # 设置窗口图标
        self.setWindowIcon(QIcon("images/python.png"))  # 设置窗体图标

        self.create_widget()

    def create_widget(self):
        """
        创建水平布局并添加按钮和标签
        :return:
        """
        from PyQt6.QtWidgets import QHBoxLayout, QPushButton, QLabel

        hbox = QHBoxLayout()  # 创建水平布局

        bth = QPushButton('Change Text')  # 创建按钮并设置默认文本

        bth.clicked.connect(self.clicked_btn)  # 连接按钮的信号，点击按钮后调用clicked_btn函数

        self.label = QLabel('Default Text')  # 创建标签并设置初始文本

        hbox.addWidget(bth)  # 添加按钮到布局中
        hbox.addWidget(self.label)  # 添加标签到布局中

        self.setLayout(hbox)  # 设置GUI布局为hbox

    def clicked_btn(self):
        """
        按钮点击信息函数
        :return:
        """
        from PyQt6.QtGui import QFont
        self.label.setText('Another Text')  # 修改标签内容
        self.label.setFont(QFont('Times', 15))  # 修改标签字体和大小
        self.label.setStyleSheet('color:red')  # 修改标签文本颜色


app = QApplication(sys.argv)  # 创建QApplication对象
window = Window()  # 创建Window对象
window.show()  # 显示窗体
sys.exit(app.exec())  # 进入应用程序的主循环，并等待退出
