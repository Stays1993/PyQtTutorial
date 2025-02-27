from PyQt6.QtGui import QIcon, QFont
from PyQt6.QtWidgets import (
    QApplication,
    QWidget,
    QComboBox,
    QLabel,
    QVBoxLayout,
    QHBoxLayout,
)


class Window(QWidget):  # 定义Window类，继承自QWidget
    def __init__(self):  # 定义构造函数
        super().__init__()  # 调用父类构造函数
        # 设置窗口标题
        self.setWindowTitle("Python 02_20_QComboBox")  # 设置窗体标题
        # 设置窗口图标
        self.setWindowIcon(QIcon("images/python.png"))  # 设置窗体图标
        # 设置窗口大小及位置
        self.setGeometry(400, 400, 600, 200)

        self.create_combo()

    def create_combo(self):
        hbox = QHBoxLayout()
        label = QLabel("选择账户类型：")
        label.setFont(QFont("等距更纱黑体 SC", 20, 700))

        self.combox = QComboBox()
        self.combox.setFont(QFont("等距更纱黑体 SC", 20, 700))
        self.combox.addItem("当前账户")
        self.combox.addItem("存款账户")
        self.combox.addItem("信用账户")
        self.combox.addItem("未来账户")

        self.combox.currentTextChanged.connect(self.combox_changed)

        vbox = QVBoxLayout()
        self.label_result = QLabel("")
        self.label_result.setFont(QFont("等距更纱黑体 SC", 20, 700))

        vbox.addWidget(self.label_result)
        vbox.addLayout(hbox)

        hbox.addWidget(label)
        hbox.addWidget(self.combox)

        self.setLayout(vbox)

    def combox_changed(self):
        item = self.combox.currentText()
        self.label_result.setText(f"你的账户类型是：{item}")


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)  # 创建QApplication对象
    window = Window()  # 创建Window对象
    window.show()  # 显示窗体
    sys.exit(app.exec())  # 进入应用程序的主循环，并等待退出
