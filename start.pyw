#!.\venv\Scripts\python.exe
"""UI界面初始化"""
import sys
from PyQt5.Qt import *
from PyQt5.QtCore import *
from UI import interface


class Ui_LoadingWindow(QWidget):
    ProgressBarValue = 0
    LoadingLabelTextValue = 0

    def __init__(self, parent=None):
        self.timer = None
        self.open = None
        desktop = QApplication.desktop()
        width, height = int(desktop.width() / 3), int(desktop.height() / 3)
        super(Ui_LoadingWindow, self).__init__(parent)
        self.resize(width, height)
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.Tool)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.frame = QFrame(self)
        self.frame.setGeometry(QRect(0, 0, width, height))
        self.frame.setStyleSheet("\n"
                                 "QFrame {    \n"
                                 "    background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(32, 178, 170, 255), stop:1 rgba(144, 238, 144, 255));    \n"
                                 "    border-radius: 15px;\n"
                                 "}")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Sunken)
        self.frame.setObjectName("frame")
        self.ProgressBar = QProgressBar(self.frame)
        self.ProgressBar.setGeometry(QRect(int(width / 6), int(3 * height / 4), int(2 * width / 3), int(height / 9)))
        self.ProgressBar.setStyleSheet("QProgressBar\n"
                                       "{\n"
                                       "    background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(227, 227, 227, 255), stop:1 rgba(156, 156, 156, 255));\n"
                                       "    border-style:none;\n"
                                       "    border-radius:20px;\n"
                                       "}\n"
                                       "QProgressBar::chunk\n"
                                       "{\n"
                                       "    border-radius:20px;\n"
                                       "    background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(61, 255, 249, 255), stop:1 rgba(38, 197, 255, 255));\n"
                                       "}")
        self.ProgressBar.setProperty("value", 0)
        self.ProgressBar.setAlignment(Qt.AlignCenter)
        self.ProgressBar.setTextVisible(True)
        self.ProgressBar.setOrientation(Qt.Horizontal)
        self.ProgressBar.setObjectName("ProgressBar")
        self.Name = QLabel(self.frame)
        self.Name.setGeometry(QRect(0, int(height / 7), width, int(height / 4)))
        font = QFont()
        font.setFamily("黑体")
        font.setPixelSize(int(height / 3.5))
        font.setBold(False)
        font.setWeight(50)
        self.Name.setFont(font)
        self.Name.setStyleSheet("QLabel\n"
                                "{\n"
                                "    background-color: rgba(255, 255, 255, 0);\n"
                                "}")
        self.Name.setObjectName("Name")
        self.Name.setAlignment(Qt.AlignCenter)
        self.LoadingLabel = QLabel(self.frame)
        self.LoadingLabel.setGeometry(QRect(0, int(height / 2), width, int(height / 8)))
        font = QFont()
        font.setFamily("黑体")
        font.setPixelSize(int(height / 9))
        font.setBold(False)
        font.setWeight(50)
        self.LoadingLabel.setFont(font)
        self.LoadingLabel.setStyleSheet("QLabel\n"
                                        "{\n"
                                        "    background-color: rgba(255, 255, 255, 0);\n"
                                        "}")
        self.LoadingLabel.setAlignment(Qt.AlignCenter)
        self.LoadingLabel.setObjectName("LoadingLabel")

        self.retranslateUi(self)
        QMetaObject.connectSlotsByName(self)
        self.set_loader()

    def retranslateUi(self, LoadingWinodw):
        _translate = QCoreApplication.translate
        LoadingWinodw.setWindowTitle(_translate("LoadingWinodw", "Form"))
        self.Name.setText(_translate("LoadingWinodw", "一键舆情"))
        self.LoadingLabel.setText(_translate("LoadingWinodw", "加载中"))

    def set_loader(self):
        self.timer = QTimer()
        self.timer.timeout.connect(self.load_progress_bar)
        self.timer.timeout.connect(self.ChangeLoadingLabel)
        self.timer.start(20)

    def load_progress_bar(self):
        Ui_LoadingWindow.ProgressBarValue += 1
        self.ProgressBar.setValue(Ui_LoadingWindow.ProgressBarValue)
        if Ui_LoadingWindow.ProgressBarValue >= 150:
            self.timer.stop()
            self.open = interface.Ui_Form()
            self.open.show()

    def ChangeLoadingLabel(self):
        i = int(Ui_LoadingWindow.ProgressBarValue / 10)
        if i >= 10:
            self.LoadingLabel.setText("加载成功")
        elif i % 4 == 1:
            self.LoadingLabel.setText("加载中.")
        elif i % 4 == 2:
            self.LoadingLabel.setText("加载中..")
        elif i % 4 == 3:
            self.LoadingLabel.setText("加载中...")
        else:
            self.LoadingLabel.setText("加载中")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = Ui_LoadingWindow()
    win.show()
    sys.exit(app.exec())
