from PyQt6.QtGui import QIcon, QPen, QBrush
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QApplication,
    QWidget,
    QGraphicsView,
    QGraphicsScene,
    QGraphicsRectItem,
    QGraphicsEllipseItem,
    QGraphicsItem,
)


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(200, 200, 700, 400)
        self.setWindowTitle("PyQt6 05_15_QGraphicsView")
        self.setWindowIcon(QIcon("images/python.png"))

        scene: QGraphicsScene = QGraphicsScene()

        green_brush: QBrush = QBrush(Qt.GlobalColor.green)
        yellow_brush: QBrush = QBrush(Qt.GlobalColor.yellow)

        red_pen: QPen = QPen(Qt.GlobalColor.red)
        red_pen.setWidth(7)

        ellipse: QGraphicsEllipseItem = scene.addEllipse(
            100, 100, 200, 200, red_pen, green_brush
        )
        rect: QGraphicsRectItem = scene.addRect(
            -100, -100, 200, 200, red_pen, yellow_brush
        )

        ellipse.setFlag(QGraphicsItem.GraphicsItemFlag.ItemIsMovable)
        rect.setFlag(QGraphicsItem.GraphicsItemFlag.ItemIsMovable)

        view: QGraphicsView = QGraphicsView(scene, self)
        view.setGeometry(0, 0, 780, 500)


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())
