from PyQt6.QtGui import QIcon, QFont
from PyQt6.QtWidgets import (
    QApplication,
    QDialog,
    QInputDialog,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QPushButton,
    QVBoxLayout,
)


class Window(QDialog):
    def __init__(self):
        super().__init__()
        self.setGeometry(400, 400, 500, 300)
        self.setWindowTitle("PyQt6 02_35_QInputDialog")
        self.setWindowIcon(QIcon("images/python.png"))

        self.create_dialog()

    def create_dialog(self):
        vbox: QVBoxLayout = QVBoxLayout()
        hbox1: QHBoxLayout = QHBoxLayout()
        hbox2: QHBoxLayout = QHBoxLayout()

        label: QLabel = QLabel("选择国家：")
        label.setFont(QFont("等距更纱黑体 SC", 16, 700))

        self.lineedit: QLineEdit = QLineEdit()
        self.lineedit.setFont(QFont("等距更纱黑体 SC", 16, 700))

        btn_list: QPushButton = QPushButton("选择国家(列表)")
        btn_list.setFont(QFont("等距更纱黑体 SC", 16, 700))
        btn_list.clicked.connect(self.show_dialog)

        btn_text: QPushButton = QPushButton("选择国家(输入框)")
        btn_text.setFont(QFont("等距更纱黑体 SC", 16, 700))
        btn_text.clicked.connect(self.get_text)

        btn_int: QPushButton = QPushButton("选择国家(整数)")
        btn_int.setFont(QFont("等距更纱黑体 SC", 16, 700))
        btn_int.clicked.connect(self.get_int)

        hbox1.addWidget(label)
        hbox1.addWidget(self.lineedit)

        hbox2.addWidget(btn_list)
        hbox2.addWidget(btn_text)
        hbox2.addWidget(btn_int)

        vbox.addLayout(hbox1)
        vbox.addLayout(hbox2)

        self.setLayout(vbox)

    def show_dialog(self):
        countries = [
            "中华人民共和国",
            "蒙古",
            "朝鲜",
            "韩国",
            "日本",
            "土耳其",
            "格鲁吉亚",
            "亚美尼亚",
            "阿塞拜疆",
            "伊朗",
            "阿富汗",
            "叙利亚",
            "黎巴嫩",
            "以色列",
            "巴勒斯坦",
            "约旦",
            "伊拉克",
            "科威特",
            "沙特阿拉伯",
            "巴林",
            "卡塔尔",
            "阿拉伯联合酋长国",
            "也门",
            "阿曼",
            "哈萨克斯坦",
            "乌兹别克斯坦",
            "吉尔吉斯斯坦",
            "土库曼斯坦",
            "塔吉克斯坦",
            "巴基斯坦",
            "印度",
            "尼泊尔",
            "不丹",
            "孟加拉国",
            "马尔代夫",
            "斯里兰卡",
            "缅甸",
            "泰国",
            "老挝",
            "柬埔寨",
            "越南",
            "菲律宾",
            "马来西亚",
            "文莱",
            "新加坡",
            "印度尼西亚",
            "东帝汶",
            "冰岛",
            "挪威",
            "瑞典",
            "芬兰",
            "丹麦",
            "爱尔兰",
            "英国",
            "荷兰",
            "比利时",
            "卢森堡",
            "法国",
            "摩纳哥",
            "德国",
            "瑞士",
            "列支敦士登",
            "奥地利",
            "波兰",
            "捷克",
            "斯洛伐克",
            "匈牙利",
            "爱沙尼亚",
            "拉脱维亚",
            "立陶宛",
            "白俄罗斯",
            "乌克兰",
            "摩尔多瓦",
            "俄罗斯",
            "葡萄牙",
            "西班牙",
            "安道尔",
            "意大利",
            "圣马力诺",
            "梵蒂冈",
            "马耳他",
            "斯洛文尼亚",
            "克罗地亚",
            "波黑",
            "黑山",
            "塞尔维亚",
            "罗马尼亚",
            "阿尔巴尼亚",
            "北马其顿",
            "保加利亚",
            "希腊",
            "塞浦路斯",
            "摩洛哥",
            "阿尔及利亚",
            "突尼斯",
            "利比亚",
            "埃及",
            "佛得角",
            "毛里塔尼亚",
            "马里",
            "布基纳法索",
            "尼日尔",
            "塞内加尔",
            "冈比亚",
            "几内亚比绍",
            "几内亚",
            "塞拉利昂",
            "利比里亚",
            "科特迪瓦",
            "加纳",
            "多哥",
            "贝宁",
            "尼日利亚",
            "圣多美和普林西比",
            "喀麦隆",
            "赤道几内亚",
            "加蓬",
            "刚果（布）",
            "乍得",
            "中非",
            "刚果（金）",
            "苏丹",
            "南苏丹",
            "乌干达",
            "卢旺达",
            "布隆迪",
            "厄立特里亚",
            "埃塞俄比亚",
            "吉布提",
            "索马里",
            "肯尼亚",
            "坦桑尼亚",
            "塞舌尔",
            "安哥拉",
            "赞比亚",
            "马拉维",
            "纳米比亚",
            "博茨瓦纳",
            "津巴布韦",
            "南非",
            "莱索托",
            " 斯威士兰",
            "莫桑比克",
            "科摩罗",
            "马达加斯加",
            "毛里求斯",
            "澳大利亚",
            "新西兰",
            "帕劳",
            "密克罗尼西亚联邦",
            "马绍尔群岛",
            "瑙鲁",
            "基里巴斯",
            "巴布亚新几内亚",
            "所罗门群岛",
            "瓦努阿图",
            "斐济",
            "图瓦卢",
            "萨摩亚",
            "汤加",
            "纽埃",
            "库克群岛",
            "加拿大",
            "美国",
            "墨西哥",
            "危地马拉",
            "伯利兹",
            "萨尔瓦多",
            "洪都拉斯",
            "尼加拉瓜",
            "哥斯达黎加",
            "巴拿马",
            "巴哈马",
            "古巴",
            "牙买加",
            "海地",
            "多米尼加",
            "圣基茨和尼维斯",
            "安提瓜和巴布达",
            "多米尼克",
            "圣卢西亚",
            "巴巴多斯",
            "圣文森特和格林纳丁斯",
            "格林纳达",
            "特立尼达和多巴哥",
            "哥伦比亚",
            "委内瑞拉",
            "圭亚那",
            "苏里南",
            "厄瓜多尔",
            "秘鲁",
            "玻利维亚",
            "巴西",
            "智利",
            "阿根廷",
            "巴拉圭",
            "乌拉圭",
        ]

        country, ok = QInputDialog.getItem(
            self, "输入对话框", "国家列表", countries, 0, False
        )

        if ok and country:
            self.lineedit.setText(country)

    def get_text(self):
        my_text, ok = QInputDialog.getText(self, "获取用户名", "输入你的名字：")

        if ok and my_text:
            self.lineedit.setText(my_text)

    def get_int(self):
        my_number, ok = QInputDialog.getInt(
            self, "订单数量", "输入数量：", value=1, min=2, max=30, step=50
        )

        if ok and my_number:
            self.lineedit.setText(str(my_number))


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())
