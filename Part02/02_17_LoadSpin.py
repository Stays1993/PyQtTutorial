from PyQt6.QtWidgets import QApplication, QWidget, QLineEdit, QDoubleSpinBox
from PyQt6 import uic


class UI(QWidget):
    def __init__(self):
        super().__init__()

        uic.loadUi("02_17_DoubleSpinBoxDemo.ui", self)

        self.lineEdit_price = self.findChild(QLineEdit, "lineEdit_price")

        self.DoubleSpinBox = self.findChild(QDoubleSpinBox, "doubleSpinBox")
        self.DoubleSpinBox.valueChanged.connect(self.spin_selected)

        self.lineEdit_total = self.findChild(QLineEdit, "lineEdit_total")

    def spin_selected(self):
        try:
            if self.lineEdit_price.text() != 0:
                price = int(self.lineEdit_price.text())
                total = price * self.DoubleSpinBox.value()
                self.lineEdit_total.setStyleSheet("QLineEdit {color:black}")
                self.lineEdit_total.setText(str(total))

        except Exception:
            self.lineEdit_total.setStyleSheet("QLineEdit {color:red}")
            self.lineEdit_total.setText("输入的值错误！")


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    window = UI()
    window.show()
    app.exec()
