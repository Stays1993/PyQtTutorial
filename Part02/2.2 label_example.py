from PyQt6.QtGui import QIcon  # 导入QIcon类
from PyQt6.QtWidgets import QApplication, QWidget  # 导入QApplication和QWidget类

import sys  # 导入sys模块


class Window(QWidget):  # 定义Window类，继承自QWidget
    def __init__(self):  # 定义构造函数
        super().__init__()  # 调用父类构造函数

        # 设置窗口X位置，Y位置，高度，宽度
        self.setGeometry(2500, 400, 800, 600)

        # 设置窗口标题
        self.setWindowTitle("PyQt6 QLabel")  # 设置窗体标题

        # 设置窗口图标
        self.setWindowIcon(QIcon("images/python.png"))  # 设置窗体图标

        # ----------------------------
        # 1. 添加文本标签
        # ----------------------------
        """
        from PyQt6.QtWidgets import QLabel
        from PyQt6.QtGui import QFont
        text_label = QLabel('Python GUI Development', self)
        text_label.setText('New Text is Here')  # 设置文本内容
        text_label.move(100, 100)  # 移动文本位置X, Y
        text_label.setFont(QFont('Sanserif', 15))  # 设置文本字体样式及大小
        text_label.setStyleSheet("color:red")  # 设置文字颜色

        # text_label.setNum(15)  # 设置内容为数字
        # text_label.clear()  # 清除标签内容
        """

        # ----------------------------
        # 2. 添加图像标签
        # ----------------------------
        """
        from PyQt6.QtGui import QPixmap
        pix_label = QLabel(self)
        pixmap = QPixmap('images/python.png')  # 设置图片对象

        pix_label.setPixmap(pixmap)  # 设置标签内容为 pixmap 对象
        """

        # ----------------------------
        # 3. 添加GIF图像标签
        # ----------------------------
        """
        from PyQt6.QtGui import QMovie
        movie_label = QLabel(self)
        movie = QMovie('images/1.gif')  # 设置GIF图片对象
        movie.setSpeed(500)  # 设置播放速度
        movie_label.setMovie(movie)  # 设置标签内容为 movie 对象
        movie.start()  # 播放GIF图片
        """


app = QApplication(sys.argv)  # 创建QApplication对象
window = Window()  # 创建Window对象
window.show()  # 显示窗体
sys.exit(app.exec())  # 进入应用程序的主循环，并等待退出
