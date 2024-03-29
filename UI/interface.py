"""UI主界面"""
from PyQt5.Qt import *
from PyQt5.QtCore import *
from UI import about
from log.log import get_current_log, is_log, get_history_log, get_exact_log
from run import run
from re import sub, compile


class UiForm(QWidget):

    def __init__(self, parent=None):
        self.open_ = None
        self.open = None
        self.pm = None
        desktop = QApplication.desktop()
        width, height = int(desktop.width()/1.3), int(desktop.height()/1.3)
        super(UiForm, self).__init__(parent)
        self.resize(width, height)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.frame = QFrame(self)
        self.frame.setGeometry(QRect(0, 0, width, 70))
        size_policy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        size_policy.setHorizontalStretch(0)
        size_policy.setVerticalStretch(0)
        size_policy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(size_policy)
        self.frame.setStyleSheet("QFrame\n"
                                 "{\n"
                                 "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba("
                                 "255, 248, 34, 150), stop:1 rgba(254, 255, 167, 150));\n "
                                 "}\n"
                                 "")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.frame.setObjectName("frame")
        self.pushButton = QPushButton(self.frame)
        self.pushButton.setGeometry(QRect(int(0.96*width), 20, int(0.03*width), 30))
        font = QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("QPushButton\n"
                                      "{\n"
                                      "    background-color: rgba(255, 255, 255, 0);\n"
                                      "}\n"
                                      "QPushButton:hover\n"
                                      "{\n"
                                      "    background-color:rgba(254, 255, 167, 150);\n"
                                      "}\n"
                                      "")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.close)
        self.pushButton_3 = QPushButton(self.frame)
        self.pushButton_3.setGeometry(QRect(int(0.92*width), 20, int(0.03*width), 30))
        font = QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("QPushButton\n"
                                        "{\n"
                                        "    background-color: rgba(255, 255, 255, 0);\n"
                                        "}\n"
                                        "QPushButton:hover\n"
                                        "{\n"
                                        "    background-color:rgba(254, 255, 167, 150);\n"
                                        "}\n"
                                        "")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(self.showMinimized)
        self.label = QLabel(self.frame)
        self.label.setGeometry(QRect(0, 0, 180, 70))
        font = QFont()
        font.setFamily("等线")
        font.setPointSize(18)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setObjectName("label")
        self.pushButton_4 = QPushButton(self.frame)
        self.pushButton_4.setGeometry(QRect(int(0.88*width), 20, int(0.03*width), 30))
        self.pushButton_4.setMaximumSize(QSize(60, 16777215))
        font = QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setStyleSheet("QPushButton\n"
                                        "{\n"
                                        "    background-color: rgba(255, 255, 255, 0);\n"
                                        "}\n"
                                        "QPushButton:hover\n"
                                        "{\n"
                                        "    background-color:rgba(254, 255, 167, 150);\n"
                                        "}\n"
                                        "QPushButton::menu-indicator{image:none;}"
                                        "")
        menu = QMenu()
        About = QAction("关于...", parent=menu)
        menu.addAction(About)
        About.triggered.connect(self.open_about)
        self.pushButton_4.setMenu(menu)
        self.pushButton_4.setObjectName("pushButton_4")
        self.frame_2 = QFrame(self)
        height2 = height-70
        self.frame_2.setGeometry(QRect(0, 70, width, height2))
        self.frame_2.setStyleSheet("QFrame\n"
                                   "{\n"
                                   "    background-color: rgb(232, 232, 232)\n"
                                   "}\n"
                                   "")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.tabWidget = QTabWidget(self.frame_2)
        self.tabWidget.setGeometry(QRect(0, 0, width, height2))
        font = QFont()
        font.setFamily("Agency FB")
        font.setPixelSize(int(0.012*width))
        self.tabWidget.setFont(font)
        self.tabWidget.setStyleSheet("QTabWidget::tab-bar { \n"
                                     "    alignment: center; \n"
                                     "} \n"
                                     "QTabBar::tab:hover{\n"
                                     "    background:rgba(125, 125, 125,200)\n"
                                     "}\n"
                                     "QTabWidget::pane{\n"
                                     "    border:none;\n"
                                     "}\n"
                                     "QTabBar::tab {\n"
                                     "    border-color: black;\n"
                                     "    border-width: 3px;\n"
                                     "    border-bottom:none;\n"
                                     "    background:rgba(173, 173, 173,120);\n"
                                     "    color:black;\n"
                                     "    min-width:" + str(width/3 - 1) +
                                     ";\n"
                                     "    min-height:" + str(height2/11) +
                                     ";\n"
                                     "}\n"
                                     "QTabBar::tab:selected \n"
                                     "{\n"
                                     "    background-color: rgb(66, 66, 66);\n"
                                     "    color: rgb(255, 255, 127);\n"
                                     "}\n"
                                     "\n"
                                     "")
        self.tabWidget.setObjectName("tabWidget")
        height3 = height2 - height2/11
        self.tab = QWidget()
        self.tab.setObjectName("tab")
        self.label_3 = QLabel(self.tab)
        self.label_3.setGeometry(QRect(int(0.015*width), int(0.035*height3), 400, int(0.025 * height3)))
        font = QFont()
        font.setFamily("Agency FB")
        font.setPixelSize(int(0.025 * height3))
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.comboBox_2 = QComboBox(self.tab)
        self.comboBox_2.setGeometry(QRect(int(0.08*width), int(0.035*height3), int(0.3*width), int(0.032 * height3)))
        font = QFont()
        font.setFamily("Agency FB")
        font.setPixelSize(int(0.025*height3))
        self.comboBox_2.setFont(font)
        self.comboBox_2.setFocusPolicy(Qt.StrongFocus)
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.scrollArea = QScrollArea(self.tab)
        self.scrollArea.setGeometry(QRect(int(0.015*width), int(0.15*height3), int(0.45*width), int(0.75*height3)))
        self.scrollArea.setMinimumSize(QSize(0, 0))
        self.scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scrollArea.setSizeAdjustPolicy(QAbstractScrollArea.AdjustIgnored)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, int(0.6*width), int(0.8*height3)))
        self.scrollAreaWidgetContents.setMinimumSize(QSize(int(0.6*width), int(0.8*height3)))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.label_8 = QLabel(self.scrollAreaWidgetContents)
        self.label_8.setGeometry(QRect(0, 0, int(0.6*width), int(height3)))
        font = QFont()
        font.setFamily("Agency FB")
        font.setPixelSize(int(0.04*height3))
        self.label_8.setFont(font)
        self.label_8.setAlignment(Qt.AlignTop)
        self.label_8.setObjectName("label_8")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.waitinglabel = QLabel(self.tab)
        self.waitinglabel.setGeometry(
            QRect(int(0.5 * width), int(0.027 * height3), int(0.25 * width), int(0.045 * height3)))
        font = QFont()
        font.setFamily("Agency FB")
        font.setPixelSize(int(0.03 * height3))
        self.waitinglabel.setFont(font)
        self.waitinglabel.setText("爬取时间可能略长，请耐心等待哦~")
        self.pushButton_13 = QPushButton(self.tab)
        self.pushButton_13.setGeometry(QRect(int(0.4*width), int(0.027*height3), int(0.08*width), int(0.045 * height3)))
        font = QFont()
        font.setFamily("Agency FB")
        font.setPixelSize(int(0.015*width))
        self.pushButton_13.setFont(font)
        self.pushButton_13.setStyleSheet("QPushButton\n"
                                         "{\n"
                                         "background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, "
                                         "stop:0 rgba(16, 171, 255, 150), stop:1 rgba(15, 251, 255, 150));\n "
                                         "    border-top-left-radius: 20px;\n"
                                         "    border-top-right-radius: 20px;\n"
                                         "    border-bottom-right-radius: 20px;\n"
                                         "    border-bottom-left-radius: 20px;\n"
                                         "}\n"
                                         "QPushButton:hover\n"
                                         "{\n"
                                         "background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, "
                                         "stop:0 rgba(16, 171, 255, 250), stop:1 rgba(15, 251, 255, 250));\n "
                                         "}")
        self.pushButton_13.setObjectName("pushButton_13")
        self.pushButton_13.clicked.connect(self.click_run)
        self.label_6 = QLabel(self.tab)
        self.label_6.setGeometry(QRect(int(0.015*width), int(0.09*height3), int(0.45*width), int(0.045 * height3)))
        font = QFont()
        font.setFamily("Agency FB")
        font.setPixelSize(int(0.03 * height3))
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_7 = QLabel(self.tab)
        self.label_7.setGeometry(QRect(int(0.515*width), int(0.09*height3), int(0.45*width), int(0.045 * height3)))
        font = QFont()
        font.setFamily("Agency FB")
        font.setPixelSize(int(0.03 * height3))
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.picture = QLabel(self.tab)
        self.picture.setGeometry(QRect(int(0.515 * width), int(0.15 * height3), int(0.45 * width), int(0.75 * height3)))
        self.picture.setObjectName("picture")
        self.tabWidget.addTab(self.tab, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName("tab_3")
        self.label_2 = QLabel(self.tab_3)
        self.label_2.setGeometry(QRect(int(0.015*width), int(0.035*height3), 400, int(0.025 * height3)))
        font = QFont()
        font.setFamily("Agency FB")
        font.setPixelSize(int(0.025 * height3))
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.comboBox = QComboBox(self.tab_3)
        self.comboBox.setGeometry(QRect(int(0.08*width), int(0.035*height3), int(0.3*width), int(0.032 * height3)))
        font = QFont()
        font.setFamily("Agency FB")
        font.setPixelSize(int(0.025*height3))
        self.comboBox.setFont(font)
        self.comboBox.setFocusPolicy(Qt.StrongFocus)
        self.comboBox.setObjectName("comboBox_2")
        self.history_update()
        self.scrollArea_2 = QScrollArea(self.tab_3)
        self.scrollArea_2.setGeometry(QRect(int(0.015*width), int(0.15*height3), int(0.45*width), int(0.75*height3)))
        self.scrollArea_2.setMinimumSize(QSize(0, 0))
        self.scrollArea_2.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scrollArea_2.setSizeAdjustPolicy(QAbstractScrollArea.AdjustIgnored)
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName("scrollArea_8")
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, int(0.6*width), int(0.8*height3)))
        self.scrollAreaWidgetContents_2.setMinimumSize(QSize(int(0.6*width), int(0.8*height3)))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.label_36 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_36.setGeometry(QRect(0, 0, int(0.6 * width), int(height3)))
        font = QFont()
        font.setFamily("Agency FB")
        font.setPixelSize(int(0.04 * height3))
        self.label_36.setFont(font)
        self.label_36.setAlignment(Qt.AlignTop)
        self.label_36.setObjectName("label_36")
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)
        self.pushButton_14 = QPushButton(self.tab_3)
        self.pushButton_14.setGeometry(QRect(int(0.4*width), int(0.027*height3), int(0.08*width), int(0.045 * height3)))
        font = QFont()
        font.setFamily("Agency FB")
        font.setPixelSize(int(0.015*width))
        self.pushButton_14.setFont(font)
        self.pushButton_14.setStyleSheet("QPushButton\n"
                                         "{\n"
                                         "background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, "
                                         "stop:0 rgba(16, 171, 255, 150), stop:1 rgba(15, 251, 255, 150));\n "
                                         "    border-top-left-radius: 20px;\n"
                                         "    border-top-right-radius: 20px;\n"
                                         "    border-bottom-right-radius: 20px;\n"
                                         "    border-bottom-left-radius: 20px;\n"
                                         "}\n"
                                         "QPushButton:hover\n"
                                         "{\n"
                                         "background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, "
                                         "stop:0 rgba(16, 171, 255, 250), stop:1 rgba(15, 251, 255, 250));\n "
                                         "}")
        self.pushButton_14.setObjectName("pushButton_13")
        self.pushButton_14.clicked.connect(self.click_history)
        self.label_38 = QLabel(self.tab_3)
        self.label_38.setGeometry(QRect(int(0.015*width), int(0.09*height3), int(0.45*width), int(0.045 * height3)))
        font = QFont()
        font.setFamily("Agency FB")
        font.setPixelSize(int(0.03 * height3))
        self.label_38.setFont(font)
        self.label_38.setObjectName("label_38")
        self.label_22 = QLabel(self.tab_3)
        self.label_22.setGeometry(QRect(int(0.515*width), int(0.09*height3), int(0.45*width), int(0.045 * height3)))
        font = QFont()
        font.setFamily("Agency FB")
        font.setPixelSize(int(0.03 * height3))
        self.label_22.setFont(font)
        self.label_22.setObjectName("label_22")
        self.historypicture = QLabel(self.tab_3)
        self.historypicture.setGeometry(
            QRect(int(0.515 * width), int(0.15 * height3), int(0.45 * width), int(0.75 * height3)))
        self.historypicture.setObjectName("picture")
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName("tab_2")
        self.label_41 = QLabel(self.tab_2)
        self.label_41.setGeometry(
            QRect(int(0.015 * width), int(0.04 * height3), int(0.45 * width), int(0.04 * height3)))
        self.label_41.setObjectName("label_41")
        self.label_42 = QLabel(self.tab_2)
        self.label_42.setGeometry(QRect(int(0.015 * width), int(0.2 * height3), int(0.45 * width), int(0.04 * height3)))
        self.label_42.setObjectName("label_42")
        self.label_40 = QLabel(self.tab_2)
        self.label_40.setGeometry(
            QRect(int(0.015 * width), int(0.08 * height3), int(0.45 * width), int(0.04 * height3)))
        font = QFont()
        font.setFamily("Agency FB")
        font.setPointSize(14)
        self.label_40.setFont(font)
        self.label_40.setObjectName("label_40")
        self.radioButton = QRadioButton(self.tab_2)
        self.radioButton.setGeometry(int(0.015 * width), int(0.15 * height3), int(0.45 * width), int(0.04 * height3))
        font = QFont()
        font.setFamily("Agency FB")
        font.setPixelSize(int(0.03 * height3))
        self.radioButton.setFont(font)
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QRadioButton(self.tab_2)
        self.radioButton_2.setGeometry(int(0.07 * width), int(0.15 * height3), int(0.45 * width), int(0.04 * height3))
        font = QFont()
        font.setFamily("Agency FB")
        font.setPixelSize(int(0.03 * height3))
        self.radioButton_2.setFont(font)
        self.radioButton_2.setChecked(True)
        self.radioButton_2.setObjectName("radioButton_2")
        self.radioButton_3 = QRadioButton(self.tab_2)
        self.radioButton_3.setGeometry(
            QRect(int(0.125 * width), int(0.15 * height3), int(0.45 * width), int(0.04 * height3)))
        font = QFont()
        font.setFamily("Agency FB")
        font.setPixelSize(int(0.03 * height3))
        self.radioButton_3.setFont(font)
        self.radioButton_3.setObjectName("radioButton_3")
        self.tabWidget.addTab(self.tab_2, "")

        self.translate_ui(self)
        self.tabWidget.setCurrentIndex(0)
        QMetaObject.connectSlotsByName(self)

    def search_num(self):
        if self.radioButton.isChecked():
            return 5
        elif self.radioButton_2.isChecked():
            return 10
        else:
            return 15

    def click_run(self):
        """点击后运行"""
        num = self.search_num()
        name = self.comboBox_2.currentText()
        if name == "微博热门":
            if is_log('weibo'):
                pass
            else:
                run('WeiBo')
            s, pic = get_current_log('WeiBo', num)
        else:
            if is_log('xinlang'):
                pass
            else:
                run('XinLang')
            s, pic = get_current_log('XinLang', num)
        self.label_8.setText(s)
        self.pm = QPixmap(pic)
        self.picture.setPixmap(self.pm)
        self.picture.setScaledContents(True)
        self.history_update()

    def open_about(self):
        self.open = about.UiForm()
        self.open.show()

    def history_update(self):
        self.comboBox.clear()
        wei = compile(r'weibo')
        xin = compile(r'xinlang')
        s_list = get_history_log()
        for s in s_list:
            s = sub(wei, '微博热门', s)
            s = sub(xin, '新浪新闻', s)
            self.comboBox.addItem(s)

    def click_history(self):
        num = self.search_num()
        time_ = self.comboBox.currentText()
        wei = compile(r'微博热门')
        xin = compile(r'新浪新闻')
        time_ = sub(wei, 'weibo', time_)
        time_ = sub(xin, 'xinlang', time_)
        s, pic = get_exact_log(time_, num)
        self.label_36.setText(s)
        picture_file = pic
        self.pm = QPixmap(picture_file)
        self.historypicture.setPixmap(self.pm)
        self.historypicture.setScaledContents(True)

    def translate_ui(self, form):
        _translate = QCoreApplication.translate
        form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton.setText(_translate("Form", "×"))
        self.pushButton_3.setText(_translate("Form", "-"))
        self.label.setText(_translate("Form", "一键舆情"))
        self.pushButton_4.setText(_translate("Form", "三"))
        self.label_3.setText(_translate("Form", "搜索的网站："))
        self.comboBox_2.setItemText(0, _translate("Form", "微博热门"))
        self.comboBox_2.setItemText(1, _translate("Form", "新浪新闻"))
        self.label_8.setText(_translate("Form", "什么都没有，赶紧搜索吧~~~"))
        self.pushButton_13.setText(_translate("Form", "一键舆情"))
        self.label_6.setText(_translate("Form", "舆情数据："))
        self.label_7.setText(_translate("Form", "词云图："))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Form", "信息搜取"))
        self.label_2.setText(_translate("Form", "时间："))
        self.pushButton_14.setText(_translate("Form", "一键查询"))
        self.label_22.setText(_translate("Form", "词云图："))
        self.label_36.setText(_translate("Form", "什么都没有，赶紧搜索吧~~~"))
        self.label_38.setText(_translate("Form", "舆情数据："))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("Form", "历史记录"))
        self.label_41.setText(_translate("Form", "——————————————————————————————————————————————————————————————"
                                                 "————————————————————————————"))
        self.label_42.setText(_translate("Form", "——————————————————————————————————————————————————————————————"
                                                 "————————————————————————————"))
        self.label_40.setText(_translate("Form", "默认显示数据条数"))
        self.radioButton.setText(_translate("Form", "5"))
        self.radioButton_2.setText(_translate("Form", "10"))
        self.radioButton_3.setText(_translate("Form", "15"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Form", "设置"))
