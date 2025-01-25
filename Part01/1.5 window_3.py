from PyQt6.QtWidgets import QApplication, QDialog  # 导入QApplication和QDialog类
import sys  # 导入sys模块

from wx.lib.agw.aui import aero_dock_pane_top

app = QApplication(sys.argv)  # 创建QApplication对象

window = QDialog()  # 创建QDialog对象

window.show()  # 显示窗体

sys.exit(app.exec())  # 进入应用程序的主循环，并等待退出


app.exec()
