from PyQt6.QtGui import QIcon, QFont
from PyQt6.QtWidgets import (
    QApplication,
    QWidget,
    QSpinBox,
    QHBoxLayout,
    QLabel,
    QLineEdit,
)


class Window(QWidget):  # 定义Window类，继承自QWidget
    def __init__(self):  # 定义构造函数
        super().__init__()  # 调用父类构造函数
        # 设置窗口标题
        self.setWindowTitle("Python QSpinBox")  # 设置窗体标题
        # 设置窗口图标
        self.setWindowIcon(QIcon("images/python.png"))  # 设置窗体图标
        # 设置窗口大小及位置
        self.setGeometry(300, 300, 700, 400)

        hbox = QHBoxLayout()

        label = QLabel("笔记本价格：")
        label.setFont(QFont("等距更纱黑体 SC", 16))

        self.lineedit = QLineEdit()
        self.lineedit.setFont(QFont("等距更纱黑体 SC", 16))

        self.spinbox = QSpinBox()
        self.spinbox.setFont(QFont("等距更纱黑体 SC", 16))
        self.spinbox.valueChanged.connect(self.spin_selected)

        self.total_result = QLineEdit()
        self.total_result.setFont(QFont("等距更纱黑体 SC", 16))

        hbox.addWidget(label)
        hbox.addWidget(self.lineedit)
        hbox.addWidget(self.spinbox)
        hbox.addWidget(self.total_result)

        self.setLayout(hbox)

    def spin_selected(self):
        try:
            if self.lineedit.text() != 0:
                price = int(self.lineedit.text())
                total_price = price * self.spinbox.value()

                self.total_result.setText(str(total_price))

        except Exception as e:
            self.total_result.setText(f"输入的价格错误！")


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)  # 创建QApplication对象
    window = Window()  # 创建Window对象
    window.show()  # 显示窗体
    sys.exit(app.exec())  # 进入应用程序的主循环，并等待退出
