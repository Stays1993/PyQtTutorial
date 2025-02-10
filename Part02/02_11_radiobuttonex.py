import sys

from PyQt6.QtCore import QSize
from PyQt6.QtGui import QFont, QIcon
from PyQt6.QtWidgets import QApplication, QHBoxLayout, QLabel, QRadioButton, QVBoxLayout, QWidget


class Window(QWidget):  # 定义Window类，继承自QWidget
    def __init__(self):  # 定义构造函数
        super().__init__()  # 调用父类构造函数

        # 设置窗口X位置，Y位置，高度，宽度
        self.setGeometry(0, 0, 300, 200)

        # 设置窗口标题
        self.setWindowTitle("PyQt6 QRadioButton")  # 设置窗体标题

        # 设置窗口图标
        self.setWindowIcon(QIcon("images/python.png"))  # 设置窗体图标

        # 调用函数
        self.create_radio()

    def create_radio(self):
        hbox = QHBoxLayout()  # 创建水平布局对象

        rad1 = QRadioButton('Python')  # 创建单选按钮对象，并设置默认文本
        rad1.setIcon(QIcon('images/python.png'))  # 添加选项图标
        rad1.setIconSize(QSize(32, 32))  # 修改图标大小
        rad1.setFont(QFont('Times', 18))  # 修改文字大小
        rad1.setChecked(True)  # 设置默认为选中状态
        rad1.toggled.connect(self.radio_selected)

        rad2 = QRadioButton('Java')  # 创建单选按钮对象，并设置默认文本
        rad2.setIcon(QIcon('images/java.png'))  # 添加选项图标
        rad2.setIconSize(QSize(32, 32))  # 修改图标大小
        rad2.setFont(QFont('Times', 18))  # 修改文字大小
        # rad2.setChecked(True)  # 设置默认为选中状态
        rad2.toggled.connect(self.radio_selected)

        rad3 = QRadioButton('JavaScript')  # 创建单选按钮对象，并设置默认文本
        rad3.setIcon(QIcon('images/JavaScript.png'))  # 添加选项图标
        rad3.setIconSize(QSize(32, 32))  # 修改图标大小
        rad3.setFont(QFont('Times', 18))  # 修改文字大小
        # rad3.setChecked(True)  # 设置默认为选中状态
        rad3.toggled.connect(self.radio_selected)

        hbox.addWidget(rad1)  # 添加rad1到hbox布局
        hbox.addWidget(rad2)  # 添加rad2到hbox布局
        hbox.addWidget(rad3)  # 添加rad3到hbox布局

        self.label = QLabel('')  # 创建文本标签
        self.label.setFont(QFont("Sanserif", 22))  # 设置文本标签字体及大小

        vbox = QVBoxLayout()  # 创建垂直布局对象
        vbox.addWidget(self.label)  # 添加self.label到vbox布局
        vbox.addLayout(hbox)  # 将hbox添加到vhox布局中
        self.setLayout(vbox)

    def radio_selected(self):
        radio_btn = self.sender()  # 获取单选按钮文本

        if radio_btn.isChecked():  # 检查是否选中单选按钮
            self.label.setText(f'You have selected : {radio_btn.text()}')  # 如果选中单选按钮就改变文本标签内容


app = QApplication(sys.argv)  # 创建QApplication对象
window = Window()  # 创建Window对象
window.show()  # 显示窗体
sys.exit(app.exec())  # 进入应用程序的主循环，并等待退出
