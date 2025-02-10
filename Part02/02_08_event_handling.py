import sys  # 导入系统模块，用于处理应用程序退出状态

# PyQt6采用按需导入原则，仅导入需要的类（最佳实践）
from PyQt6.QtWidgets import QApplication, QWidget
from PyQt6.QtGui import QIcon


class Window(QWidget):
    """主窗口类，继承自QWidget基础窗口控件"""
    def __init__(self):
        super().__init__()  # 必须调用父类初始化方法，继承QWidget属性

        # 窗口初始化设置 ------------------------------
        # setGeometry(x, y, width, height) 四参数重载方法
        # 参数1-2：窗口左上角屏幕坐标(0,0)，适用于多显示器场景
        # 参数3-4：窗口初始尺寸800x600像素
        self.setGeometry(0, 0, 800, 600)

        self.setWindowTitle("PyQt6 Event Handling")  # 设置窗口标题
        self.setWindowIcon(QIcon("images/python.png"))  # 设置任务栏图标，支持多种图片格式

        self.init_ui()  # 调用界面初始化方法

    def init_ui(self):
        """初始化用户界面组件"""
        # 局部导入：当组件仅在方法内使用时，可减少内存占用（可选策略）
        from PyQt6.QtWidgets import QHBoxLayout, QPushButton, QLabel

        # 布局管理 ------------------------------
        h_layout = QHBoxLayout()  # 创建水平布局容器，自动管理子组件排列

        # 按钮组件
        btn = QPushButton('Change Text')
        # 信号槽机制：连接按钮的clicked信号到自定义槽函数
        btn.clicked.connect(self.on_button_click)  # 注意这里不需要括号，传递函数引用

        # 标签组件（添加self前缀使其成为实例变量，便于后续访问）
        self.label = QLabel('Default Text')

        # 将组件添加到布局容器
        h_layout.addWidget(btn)
        h_layout.addWidget(self.label)

        # 关键步骤：必须将布局设置到当前窗口
        self.setLayout(h_layout)

    def on_button_click(self):
        """按钮点击事件处理函数（槽函数）"""
        # 局部导入示例（实际开发建议在文件头部统一导入）
        from PyQt6.QtGui import QFont

        # 修改标签内容
        self.label.setText('Modified Text')

        # 字体设置：使用QFont指定字体族和字号
        self.label.setFont(QFont('Times New Roman', 15))

        # 样式表：使用CSS语法设置文本颜色
        self.label.setStyleSheet('color: red')
        # 注意：样式表优先级高于单独属性设置


# 应用程序入口 ------------------------------
if __name__ == '__main__':
    app = QApplication(sys.argv)  # 每个PyQt程序必须创建QApplication实例
    window = Window()  # 创建主窗口对象
    window.show()  # 显示窗口（默认隐藏，需主动调用）

    # 进入主事件循环，等待用户操作
    # app.exec()返回退出状态码，sys.exit()确保程序完全退出
    sys.exit(app.exec())
