from PyQt6.QtQml import QQmlApplicationEngine
from PyQt6.QtCore import QObject, pyqtSlot
from PyQt6.QtWidgets import QApplication


class Window(QObject):
    def __init__(self):
        super().__init__()

    @pyqtSlot()
    def hello(self):
        print("Hello World!")


if __name__ == "__main__":
    import sys

    app: QApplication = QApplication(sys.argv)
    engine: QQmlApplicationEngine = QQmlApplicationEngine()
    window: Window = Window()

    engine.rootContext().setContextProperty("window", window)
    engine.load("0603-Button.qml")

    sys.exit(app.exec())
