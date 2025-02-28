from PyQt6.QtGui import QIcon, QFont
from PyQt6.QtWidgets import QApplication, QWidget, QHBoxLayout, QSlider, QLabel
from PyQt6.QtCore import Qt


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(400, 300, 500, 300)
        self.setWindowTitle("Python 02_24_QSlider")
        self.setWindowIcon(QIcon("images/python.png"))

        hbox = QHBoxLayout()

        # 创建滑块
        self.slider: QSlider = QSlider()
        # 设置水平方向
        self.slider.setOrientation(Qt.Orientation.Horizontal)
        # 设置刻度
        self.slider.setTickPosition(QSlider.TickPosition.TicksAbove)
        # 设置刻度值
        self.slider.setTickInterval(10)

        # 设置最小值
        self.slider.setMinimum(0)
        # 设置最大值
        self.slider.setMaximum(99)

        self.slider.valueChanged.connect(self.changed_slider)

        self.label: QLabel = QLabel("")
        self.label.setFont(QFont("等距更纱黑体 SC", 20, 700))

        hbox.addWidget(self.slider)
        hbox.addWidget(self.label)

        self.setLayout(hbox)

    def changed_slider(self):
        value = self.slider.value()
        self.label.setText(f"{value}")


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())
