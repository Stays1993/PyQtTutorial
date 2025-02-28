from PyQt6.QtWidgets import (
    QApplication,
    QWidget,
    QLineEdit,
    QDoubleSpinBox,
    QLabel,
    QComboBox,
    QSlider,
)
from PyQt6 import uic


class UI(QWidget):
    def __init__(self):
        super().__init__()

        uic.loadUi("02_22_ComboBoxDemo.ui", self)

        self.label_result: QLabel = self.findChild(QLabel, "label_result")
        self.comboBox: QComboBox = self.findChild(QComboBox, "comboBox")
        self.comboBox.currentTextChanged.connect(self.combo_changed)

    def combo_changed(self):
        item = self.comboBox.currentText()
        self.label_result.setText(f"你选择的是：{item}")
        self.label_result.setStyleSheet("color:red")


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    window = UI()
    window.show()
    app.exec()
