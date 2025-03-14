from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import (
    QApplication,
    QGraphicsView,
    QGraphicsScene,
    QGraphicsRectItem,
)


class Window(QGraphicsView):
    def __init__(self):
        super().__init__()
        self.setFixedSize(800, 600)

        self.setWindowTitle("PyQt6 05_16_QGraphicsRectItem")
        self.setWindowIcon(QIcon("images/python.png"))

        scene: QGraphicsScene = QGraphicsScene()

        # Create Rect Item
        rect: QGraphicsRectItem = QGraphicsRectItem()
        rect.setRect(0, 0, 100, 100)
        scene.addItem(rect)

        self.setScene(scene)


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())
