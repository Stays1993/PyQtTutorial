from PyQt6.QtWidgets import QApplication, QMainWindow  # 导入QApplication和QMainWindow类
import sys  # 导入sys模块

app = QApplication(sys.argv)  # 创建QApplication对象

window = QMainWindow()  # 创建QMainWindow对象

window.statusBar().showMessage("Welcome to PyQt6 Course")  # 设置状态栏消息

window.menuBar().addMenu("File")  # 添加菜单栏

window.show()  # 显示窗体

sys.exit(app.exec())  # 进入应用程序的主循环，并等待退出
