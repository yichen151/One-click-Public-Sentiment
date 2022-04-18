"""项目关于窗口"""
from PyQt5.Qt import *
from PyQt5.QtCore import *


class Ui_Form(QWidget):
    def __init__(self, parent=None):
        desktop = QApplication.desktop()
        width, height = int(desktop.width() / 4), int(desktop.height() / 3)
        super(Ui_Form, self).__init__(parent)
        self.setObjectName("Form")
        self.resize(width, height)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setStyleSheet("QWidget\n"
                           "{\n"
                           "    background-color: rgba(155, 255, 247, 255);\n"
                           "}\n"
                           "")
        self.label = QLabel(self)
        self.label.setGeometry(QRect(int(0.01 * width), int(0.01 * height), int(0.5 * width), int(0.1 * height)))
        font = QFont()
        font.setFamily("Agency FB")
        font.setPixelSize(int(0.06 * height))
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QLabel(self)
        self.label_2.setGeometry(QRect(0, int(0.15 * height), width, int(0.1 * height)))
        self.label_2.setAlignment(Qt.AlignCenter)
        font = QFont()
        font.setFamily("黑体")
        font.setPixelSize(int(0.08 * height))
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QLabel(self)
        self.label_3.setGeometry(QRect(int(0.15 * width), int(0.3 * height), int(0.5 * width), int(0.1 * height)))
        font = QFont()
        font.setFamily("幼圆")
        font.setPixelSize(int(0.05 * height))
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QLabel(self)
        self.label_4.setGeometry(QRect(int(0.15 * width), int(0.45 * height), int(0.5 * width), int(0.1 * height)))
        font = QFont()
        font.setFamily("幼圆")
        font.setPixelSize(int(0.05 * height))
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QLabel(self)
        self.label_5.setGeometry(QRect(int(0.15 * width), int(0.6 * height), int(0.5 * width), int(0.1 * height)))
        font = QFont()
        font.setFamily("幼圆")
        font.setPixelSize(int(0.05 * height))
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.pushButton = QPushButton(self)
        self.pushButton.setGeometry(QRect(int(0.45 * width), int(0.8 * height), int(0.1 * width), int(0.1 * height)))
        font = QFont()
        font.setFamily("Agency FB")
        font.setPointSize(12)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setStyleSheet("QPushButton\n"
                                      "{\n"
                                      "    background-color: rgba(255, 255, 255, 255);\n"
                                      "}\n"
                                      "QPushButton:hover\n"
                                      "{\n"
                                      "    background-color:rgba(255, 255, 255, 200);\n"
                                      "}\n"
                                      "")
        self.pushButton.clicked.connect(lambda: self.close())

        self.retranslateUi(self)
        QMetaObject.connectSlotsByName(self)

    def retranslateUi(self, Form):
        _translate = QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "关于一键舆情"))
        self.label_2.setText(_translate("Form", "一键舆情"))
        self.label_3.setText(_translate("Form", "版本号：1.0.0"))
        self.label_4.setText(_translate("Form", "爬虫程序及数据处理：郭毅"))
        self.label_5.setText(_translate("Form", "UI制作：刘恒坤"))
        self.pushButton.setText(_translate("Form", "确定"))
