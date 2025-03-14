from PyQt6.QtGui import QIcon, QKeyEvent
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QApplication,
    QGraphicsView,
    QGraphicsScene,
    QGraphicsRectItem,
    QGraphicsItem,
)


class Window(QGraphicsView):
    def __init__(self):
        super().__init__()
        self.setFixedSize(800, 600)

        self.setWindowTitle("PyQt6 05_16_QGraphicsRectItem")
        self.setWindowIcon(QIcon("images/python.png"))

        scene: QGraphicsScene = QGraphicsScene()

        # Create Rect Item
        # rect: QGraphicsRectItem = QGraphicsRectItem()

        rect = MyRect()

        rect.setRect(0, 0, 100, 100)
        scene.addItem(rect)

        # Make Rect Focusable
        rect.setFlag(QGraphicsItem.GraphicsItemFlag.ItemIsFocusable)
        rect.setFocus()

        self.setScene(scene)


class MyRect(QGraphicsRectItem):
    def __init__(self):
        super().__init__()

    def keyPressEvent(self, event: QKeyEvent):
        if event.key() == Qt.Key.Key_Left:
            self.setPos(self.x() - 10, self.y())
            print(f"X: {self.x()}, Y: {self.y()}")

        elif event.key() == Qt.Key.Key_Right:
            self.setPos(self.x() + 10, self.y())
            print(f"X: {self.x()}, Y: {self.y()}")

        elif event.key() == Qt.Key.Key_Up:
            self.setPos(self.x(), self.y() - 10)
            print(f"X: {self.x()}, Y: {self.y()}")

        elif event.key() == Qt.Key.Key_Down:
            self.setPos(self.x(), self.y() + 10)
            print(f"X: {self.x()}, Y: {self.y()}")


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())
