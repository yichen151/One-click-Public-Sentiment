"""进度条"""
import sys
from PyQt5.Qt import *
from PyQt5.QtCore import *
import math


class chart_widget(QWidget):
    def __init__(self, parent=None):
        desktop = QApplication.desktop()
        super(chart_widget, self).__init__(parent)
        self.resize(int(desktop.width() / 4), int(desktop.height() / 2))
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.layout = QGridLayout(self)
        self.setAutoFillBackground(True)
        p = QPalette()
        p.setColor(QPalette.Background, Qt.gray)
        self.setPalette(p)
        self.bg_color = QColor(255, 0, 0)
        self.time_id = self.startTimer(80)
        self.m_waterOffset = 0.05
        self.m_offset = 50
        self.m_borderwidth = 10
        self.per_num = 0

    def paintEvent(self, event):
        painter = QPainter()
        painter.setRenderHint(QPainter.Antialiasing)
        painter.begin(self)
        width, height = self.width(), self.height()
        percentage = 1 - self.per_num / 100
        w = 2 * math.pi / width
        A = height * self.m_waterOffset
        k = height * percentage

        water1 = QPainterPath()
        water2 = QPainterPath()
        water1.moveTo(5, height)
        water2.moveTo(5, height)
        self.m_offset += 0.6

        if self.m_offset > (width / 2):
            self.m_offset = 0
        i = 5
        while i < width - 5:
            waterY1 = A * math.sin(w * i + self.m_offset) + k
            waterY2 = (-1) * A * math.sin(w * i + self.m_offset) + k

            water1.lineTo(i, waterY1)
            water2.lineTo(i, waterY2)
            i += 1

        water1.lineTo(width - 5, height)
        water2.lineTo(width - 5, height)
        totalpath = QPainterPath()
        totalpath.addRect(QRectF(5, 5, self.width() - 10, self.height() - 10))
        painter.setBrush(Qt.gray)
        painter.drawRect(self.rect())
        painter.save()

        painter.setPen(Qt.NoPen)

        watercolor1 = QColor(self.bg_color)
        watercolor1.setAlpha(100)
        watercolor2 = QColor(self.bg_color)
        watercolor2.setAlpha(150)

        path = totalpath.intersected(water1)
        painter.setBrush(watercolor1)
        painter.drawPath(path)

        path = totalpath.intersected(water2)
        painter.setBrush(watercolor2)
        painter.drawPath(path)
        painter.restore()

        m_font = QFont()
        m_font.setFamily("Agency FB")
        m_font.setPixelSize(int(self.width() / 8))
        painter.setPen(Qt.white)
        painter.setFont(m_font)
        painter.drawText(self.rect(), Qt.AlignCenter, "{}%".format(self.per_num))
        painter.end()

    def timerEvent(self, event):
        self.per_num += 1
        if self.per_num == 100:
            self.killTimer(self.time_id)
            self.close()
        self.update()


if __name__ == '__main__':
    QCoreApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
    app = QApplication(sys.argv)
    win = chart_widget()
    win.show()
    sys.exit(app.exec())
