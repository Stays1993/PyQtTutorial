from PyQt6.QtGui import QIcon, QFont
from PyQt6.QtWidgets import QApplication, QWidget, QCalendarWidget, QVBoxLayout, QLabel


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(400, 400, 500, 300)
        self.setWindowTitle("PyQt6 02_33_QCalendarWidget")
        self.setWindowIcon(QIcon("images/python.png"))

        vbox = QVBoxLayout()

        self.calendar: QCalendarWidget = QCalendarWidget()
        # 显示网格
        self.calendar.setGridVisible(True)
        # connected signal
        self.calendar.selectionChanged.connect(self.calendar_date)

        self.label: QLabel = QLabel("")
        self.label.setFont(QFont("等距更纱黑体 SC", 16, 700))

        self.setStyleSheet("color:green")

        vbox.addWidget(self.calendar)
        vbox.addWidget(self.label)

        self.setLayout(vbox)

    def calendar_date(self):
        date_selected = self.calendar.selectedDate()
        date_string = str(date_selected.toPyDate())

        self.label.setText(f"日期：{date_string}")


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())
