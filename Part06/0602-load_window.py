from PyQt6.QtQml import QQmlApplicationEngine
from PyQt6.QtCore import QObject
from PyQt6.QtWidgets import QApplication


class Window(QObject):
    def __init__(self):
        super().__init__()


if __name__ == "__main__":
    import sys

    app: QApplication = QApplication(sys.argv)
    engine: QQmlApplicationEngine = QQmlApplicationEngine()
    window: Window = Window()

    engine.rootContext().setContextProperty("window", window)
    engine.load("0602-window.qml")

    sys.exit(app.exec())
