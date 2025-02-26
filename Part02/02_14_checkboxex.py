import sys  # 导入sys模块

from PyQt6.QtCore import QSize
from PyQt6.QtGui import QIcon, QFont
from PyQt6.QtWidgets import (
    QApplication,
    QWidget,
    QCheckBox,
    QLabel,
    QVBoxLayout,
    QHBoxLayout,
)


class Window(QWidget):  # 定义Window类，继承自QWidget
    def __init__(self):  # 定义构造函数
        super().__init__()  # 调用父类构造函数
        # 设置窗口标题
        self.setWindowTitle("Python QCheckBox")  # 设置窗体标题
        # 设置窗口图标
        self.setWindowIcon(QIcon("images/python.png"))  # 设置窗体图标

        """
        复选框
        """
        hbox = QHBoxLayout()
        vbox = QVBoxLayout()

        self.check1 = QCheckBox("Python")
        self.check1.setIcon(QIcon("./images/python.png"))
        self.check1.setIconSize(QSize(20, 20))
        self.check1.setFont(QFont("微软雅黑", 16))
        self.check1.stateChanged.connect(self.item_selected)

        self.check2 = QCheckBox("Java")
        self.check2.setIcon(QIcon("./images/java.png"))
        self.check2.setIconSize(QSize(20, 20))
        self.check2.setFont(QFont("微软雅黑", 16))
        self.check2.stateChanged.connect(self.item_selected)

        self.check3 = QCheckBox("JavaScript")
        self.check3.setIcon(QIcon("./images/JavaScript.png"))
        self.check3.setIconSize(QSize(20, 20))
        self.check3.setFont(QFont("微软雅黑", 16))
        self.check3.stateChanged.connect(self.item_selected)

        hbox.addWidget(self.check1)
        hbox.addWidget(self.check2)
        hbox.addWidget(self.check3)

        self.label = QLabel("")
        self.label.setFont(QFont("黑体", 16))

        vbox.addWidget(self.label)
        vbox.addLayout(hbox)

        self.setLayout(vbox)

    def item_selected(self):
        value = ""

        # 判断复选框是否选中
        if self.check1.isChecked():
            value = self.check1.text()

        if self.check2.isChecked():
            value = self.check2.text()

        if self.check3.isChecked():
            value = self.check3.text()

        self.label.setText(f"选择项为：{value}")


app = QApplication(sys.argv)  # 创建QApplication对象
window = Window()  # 创建Window对象
window.show()  # 显示窗体
sys.exit(app.exec())  # 进入应用程序的主循环，并等待退出
