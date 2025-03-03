from PyQt6.QtWidgets import (
    QMainWindow,
    QApplication,
    QFileDialog,
    QMessageBox,
    QFontDialog,
    QColorDialog,
)
import sys
from NotePad_Design import Ui_MainWindow
from PyQt6.QtPrintSupport import QPrinter, QPrintDialog, QPrintPreviewDialog
from PyQt6.QtCore import QFileInfo, Qt
from PyQt6.QtGui import QFont


class NotePadWindow(QMainWindow, Ui_MainWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()

        """文件菜单"""
        self.actionSave.triggered.connect(self.save_file)  # 保存文件
        self.actionNew.triggered.connect(self.new_file)  # 新建文件
        self.actionOpen.triggered.connect(self.open_file)  # 打开文件
        self.actionPrint.triggered.connect(self.print_file)  # 打印文件
        self.actionPrint_Preview.triggered.connect(self.preview_dialog)  # 打印预览
        self.actionExport_PDF.triggered.connect(self.export_pdf)  # 导出PDF
        self.actionQuite.triggered.connect(self.exit_app)  # 关闭程序

        """编辑菜单"""
        self.actionUndo.triggered.connect(self.textEdit.undo)  # 撤销
        self.actionRedo.triggered.connect(self.textEdit.redo)  # 重做
        self.actionCut.triggered.connect(self.textEdit.cut)  # 剪切
        self.actionCopy.triggered.connect(self.textEdit.copy)  # 复制
        self.actionPaste.triggered.connect(self.textEdit.paste)  # 粘贴

        """格式菜单"""
        self.actionBold.triggered.connect(self.bold_text)  # 粗体
        self.actionItalic.triggered.connect(self.italic_text)  # 斜体
        self.actionUnderline.triggered.connect(self.underline_text)  # 下划线
        self.actionLeft.triggered.connect(self.align_left)  # 左对齐
        self.actionRight.triggered.connect(self.align_right)  # 右对齐
        self.actionCenter.triggered.connect(self.align_center)  # 居中
        self.actionJustify.triggered.connect(self.align_justify)  # 居中对齐
        self.actionFont.triggered.connect(self.font_dialog)  # 字体选择
        self.actionColor.triggered.connect(self.color_dialog)  # 颜色选择

        """关于菜单"""
        self.actionAbout_App.triggered.connect(self.about_info)  # 关于

    def maybe_save(self):
        """是否保存文件"""
        if not self.textEdit.document().isModified():
            return True

        # 创建消息框实例
        msg_box = QMessageBox(
            QMessageBox.Icon.Warning,
            "应用程序",
            "文档已被修改\n是否保存？",
            QMessageBox.StandardButton.Save
            | QMessageBox.StandardButton.Discard
            | QMessageBox.StandardButton.Cancel,
            self,  # 父窗口
        )

        # 修改标准按钮的显示文本
        msg_box.button(QMessageBox.StandardButton.Save).setText("保存")
        msg_box.button(QMessageBox.StandardButton.Discard).setText("放弃")
        msg_box.button(QMessageBox.StandardButton.Cancel).setText("取消")

        # 显示消息框并获取结果
        ret = msg_box.exec()

        if ret == QMessageBox.StandardButton.Save:
            return self.save_file()

        if ret == QMessageBox.StandardButton.Cancel:
            return False

        return True

    def save_file(self):
        """保存文件"""

        filename = QFileDialog.getSaveFileName(self, "保存文件")

        if filename[0]:
            f = open(filename[0], "w", encoding="UTF-8")

            with f:
                text = self.textEdit.toPlainText()
                f.write(text)

                QMessageBox.about(self, "保存文件", "保存成功")

    def new_file(self):
        """新建文件"""
        if self.maybe_save():
            self.textEdit.clear()

    def open_file(self):
        """打开文件"""

        filename = QFileDialog.getOpenFileName(self, "打开文件")

        if filename[0]:
            with open(filename[0], "r", encoding="utf-8") as f:
                data = f.read()
                self.textEdit.setText(data)

    def print_file(self):
        """打印文件"""
        printer = QPrinter(QPrinter.PrinterMode.HighResolution)
        dialog = QPrintDialog(printer)

        if dialog.exec() == QPrintDialog.DialogCode.Accepted:
            self.textEdit.print(printer)

    def preview_dialog(self):
        """打印预览对话框"""
        printer = QPrinter(QPrinter.PrinterMode.HighResolution)
        preview_dialog = QPrintPreviewDialog(printer, self)
        preview_dialog.paintRequested.connect(self.print_preview)
        preview_dialog.exec()

    def print_preview(self, printer):
        """打印预览"""
        self.textEdit.print(printer)

    def export_pdf(self):
        """导出PDF"""
        filename, _ = QFileDialog.getSaveFileName(self, "导出PDF", "PDF 文件 (.pdf)")

        if filename != "":
            if QFileInfo(filename).suffix() == "":
                filename += ".pdf"
            printer = QPrinter(QPrinter.PrinterMode.HighResolution)
            printer.setOutputFormat(QPrinter.OutputFormat.PdfFormat)
            printer.setOutputFileName(filename)
            self.textEdit.document().print(printer)

    def exit_app(self):
        self.close()

    def bold_text(self):
        """粗体"""
        font = QFont()
        font.setBold(True)
        self.textEdit.setFont(font)

    def italic_text(self):
        """斜体"""
        font = QFont()
        font.setItalic(True)
        self.textEdit.setFont(font)

    def underline_text(self):
        """下划线"""
        font = QFont()
        font.setUnderline(True)
        self.textEdit.setFont(font)

    def align_left(self):
        """左对齐"""
        self.textEdit.setAlignment(Qt.AlignmentFlag.AlignLeft)

    def align_right(self):
        """右对齐"""
        self.textEdit.setAlignment(Qt.AlignmentFlag.AlignRight)

    def align_center(self):
        """居中"""
        self.textEdit.setAlignment(Qt.AlignmentFlag.AlignCenter)

    def align_justify(self):
        """居中对齐"""
        self.textEdit.setAlignment(Qt.AlignmentFlag.AlignJustify)

    def font_dialog(self):
        """字体选择"""
        font, ok = QFontDialog.getFont()

        if ok:
            self.textEdit.setFont(font)

    def color_dialog(self):
        """颜色选择"""
        color = QColorDialog.getColor()
        self.textEdit.setTextColor(color)

    def about_info(self):
        """关于"""

        QMessageBox.about(
            self,
            "关于",
            "你好啊~~~\n这是一个简单的文本编辑器。\n参考哔哩哔哩大学{{疯狂滴小黑}}转载的QT6教程！",
        )


if __name__ == "__main__":
    try:
        app = QApplication(sys.argv)
        Note = NotePadWindow()
        sys.exit(app.exec())
    except Exception as e:
        print(e)
