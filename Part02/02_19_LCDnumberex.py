from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import (
    QApplication,
    QWidget,
    QVBoxLayout,
    QLCDNumber,
)
from PyQt6.QtCore import QTime, QTimer


class Window(QWidget):  # 定义Window类，继承自QWidget
    def __init__(self):  # 定义构造函数
        super().__init__()  # 调用父类构造函数
        # 设置窗口标题
        self.setWindowTitle("PyQt6 QLCDNumber")  # 设置窗体标题
        # 设置窗口图标
        self.setWindowIcon(QIcon("images/python.png"))  # 设置窗体图标
        # 设置窗口大小及位置
        self.setGeometry(300, 300, 700, 400)

        timer = QTimer()
        timer.timeout.connect(self.show_lcd)
        timer.start(1000)

        self.show_lcd()

    def show_lcd(self):
        vbox = QVBoxLayout()
        lcd = QLCDNumber()
        lcd.setStyleSheet("background:red")
        vbox.addWidget(lcd)
        time = QTime.currentTime()
        text = time.toString("hh:mm")

        lcd.display(text)

        self.setLayout(vbox)


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)  # 创建QApplication对象
    window = Window()  # 创建Window对象
    window.show()  # 显示窗体
    sys.exit(app.exec())  # 进入应用程序的主循环，并等待退出
