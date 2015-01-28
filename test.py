#!/usr/bin/env python
# -*- coding:utf-8 -*-

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from math import sqrt


class MainWindow(QWidget):
    def __init__(self):

        QWidget.__init__(self)

        # 初始化position
        self.m_DragPosition = self.pos()
        self.resize(355, 542)
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
        self.setMouseTracking(True)
        self.setAttribute(Qt.WA_TranslucentBackground, True)
        self.setWindowOpacity(0.9)


        # 按钮一
        qbtn_one = QPushButton(u"开始测试", self)
        qbtn_one.setGeometry(10, 10, 120, 80)
        qbtn_one.setStyleSheet("QPushButton{background-color:#16A085;border:none;color:#ffffff;font-size:20px;}"
                               "QPushButton:hover{background-color:#333333;}")

        qbtn_close = QPushButton(u"x", self)

        qbtn_close.setGeometry(320, 10, 25, 25)
        qbtn_close.setStyleSheet("QPushButton{background-color:#D35400;border:none;color:#ffffff;font-size:20px;}"
                                 "QPushButton:hover{background-color:#333333;}")

        # 注册事件
        qbtn_close.clicked.connect(qApp.quit)

    # 支持窗口拖动,重写两个方法
    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.m_drag = True
            self.m_DragPosition = event.globalPos() - self.pos()
            event.accept()

    def mouseMoveEvent(self, QMouseEvent):
        if QMouseEvent.buttons() and Qt.LeftButton:
            self.move(QMouseEvent.globalPos() - self.m_DragPosition)
            QMouseEvent.accept()

    def mouseReleaseEvent(self, QMouseEvent):
        self.m_drag = False


    #主窗口渲染，不要动
    def paintEvent(self, QPaintEvent):
        rect = QRectF(10, 10, self.width()-20, self.height()-20)
        path = QPainterPath()
        path.setFillRule(Qt.WindingFill)
        path.addRect(rect)

        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing, True)
        painter.drawRoundedRect(rect, 0, 0)
        painter.fillPath(path, QBrush(Qt.white))

        color = QColor(0, 0, 0, 40)
        for i in range(10):
            path = QPainterPath()
            path.setFillRule(Qt.WindingFill)
            path.addRect(10-i, 10-i, self.width()-(10-i)*2, self.height()-(10-i)*2)
            alpha = 120-sqrt(i)*50 if 120-sqrt(i)*50 > 0 else 0
            color.setAlpha(alpha)
            painter.setPen(color)
            painter.drawPath(path)





if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    QApplication.setQuitOnLastWindowClosed(False)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
