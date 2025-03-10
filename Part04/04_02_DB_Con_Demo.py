# Form implementation generated from reading ui file '04_02_DB_Con_Demo.ui'
#
# Created by: PyQt6 UI code generator 6.8.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets
import mysql.connector as mc
import pymysql


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(600, 300)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(parent=Form)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.lineEdit = QtWidgets.QLineEdit(parent=Form)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit.setFont(font)
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout)
        spacerItem = QtWidgets.QSpacerItem(
            20,
            40,
            QtWidgets.QSizePolicy.Policy.Minimum,
            QtWidgets.QSizePolicy.Policy.Expanding,
        )
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButton_createdb = QtWidgets.QPushButton(parent=Form)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_createdb.setFont(font)
        self.pushButton_createdb.setObjectName("pushButton_createdb")
        self.horizontalLayout_2.addWidget(self.pushButton_createdb)
        self.pushButton_dbcon = QtWidgets.QPushButton(parent=Form)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_dbcon.setFont(font)
        self.pushButton_dbcon.setObjectName("pushButton_dbcon")
        self.horizontalLayout_2.addWidget(self.pushButton_dbcon)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.label_result = QtWidgets.QLabel(parent=Form)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.label_result.setFont(font)
        self.label_result.setObjectName("label_result")
        self.verticalLayout.addWidget(self.label_result)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        # connect signal
        self.pushButton_createdb.clicked.connect(self.create_database)
        self.pushButton_dbcon.clicked.connect(self.connect_database)

    def create_database(self):
        """创建数据库"""
        try:
            # my_db = mc.connect(
            #     host="localhost", user="root", password="123456", port="3306"
            # )
            # cursor = my_db.cursor()
            # db_name = self.lineEdit.text()
            # cursor.execute(f"CREATE DATABASE {db_name}")
            # self.label_result.setText(f"{db_name} 数据库创建成功！")

            db = pymysql.connect(
                host="localhost",
                user="root",
                password="123456",
            )
            cursor = db.cursor()
            db_name = self.lineEdit.text()
            cursor.execute(f"CREATE DATABASE {db_name}")
            self.label_result.setText(f"{db_name} 数据库创建成功！")

        except pymysql.Error as error:
            self.label_result.setText(f"创建数据失败：\n{error}")

    def connect_database(self):
        try:
            db_name = self.lineEdit.text()
            db = pymysql.connect(
                host="localhost", user="root", password="123456", database=db_name
            )

            self.label_result.setText(f"连接成功")
        except pymysql.Error as error:
            print(f"连接错误\n{error}")

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "数据库名称："))
        self.pushButton_createdb.setText(_translate("Form", "创建数据库"))
        self.pushButton_dbcon.setText(_translate("Form", "连接数据库"))
        self.label_result.setText(_translate("Form", ""))


if __name__ == "__main__":
    import sys

    try:
        app = QtWidgets.QApplication(sys.argv)
        Form = QtWidgets.QWidget()
        ui = Ui_Form()
        ui.setupUi(Form)
        Form.show()
        sys.exit(app.exec())
    except Exception as e:
        print(f"ERROR \n{e}")
