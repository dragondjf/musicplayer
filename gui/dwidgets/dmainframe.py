#!/usr/bin/python
# -*- coding: utf-8 -*-

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class DMainFrame(QFrame):


    def __init__(self, parent=None):
        super(DMainFrame, self).__init__(parent)
        self._initFlags()
        self._initWindowFlags()
        self._initMainWindow()
        self._initSystemTray()

        self.setAttribute(Qt.WA_Hover)
        self.installEventFilter(self)

        self.isSideClicked = False
        self.isCusorLeftSide = False
        self.isCusorRightSide = False
        self.isCusorDownSide = False
        self.isCusorBottomLeftSide = False

    def _initFlags(self):
        self._framelessflag = True  # 无系统边框标志
        desktopWidth = QDesktopWidget().availableGeometry().width()
        desktopHeight = QDesktopWidget().availableGeometry().height()
        self.default_size = QSize(desktopWidth * 0.8, desktopHeight * 0.8)
        self.oldPosition = QPoint(0, 0)

    def _initWindowFlags(self, flag=True):
        framelessflag = flag
        if framelessflag:
            # 无边框， 带系统菜单， 可以最小化
            self.setWindowFlags(
                Qt.FramelessWindowHint)
        self._framelessflag = framelessflag

    def _initMainWindow(self):
        self.moveCenter()
        self.oldPosition = self.pos()
        self.setAttribute(Qt.WA_DeleteOnClose)
        mainLayout = QVBoxLayout()
        self.setLayout(mainLayout)
        self.layout().setContentsMargins(0, 0, 0, 0)

    def setCentralWidget(self, widget):
        self.layout().addWidget(widget)

    def _initSystemTray(self):
        self.systemTray = QSystemTrayIcon(self)
        self.systemTray.activated.connect(self.onSystemTrayIconClicked)

    def onSystemTrayIconClicked(self, reason):
        if reason == QSystemTrayIcon.Unknown:
            pass
        elif reason == QSystemTrayIcon.Context:
            pass
        elif reason == QSystemTrayIcon.DoubleClick:
            pass
        elif reason == QSystemTrayIcon.Trigger:
            self.setVisible(not self.isVisible())
        elif reason == QSystemTrayIcon.MiddleClick:
            pass
        else:
            pass

    def setSystemTrayMenu(self, menu):
        if isinstance(menu, QMenu) and \
                hasattr(self, 'systemTray') and self.systemTray:
            self.systemTray.setContextMenu(menu)

    def setWindowIcon(self, icon):
        if not isinstance(icon, QIcon):
            qicon = QIcon(icon)
        else:
            qicon = icon
        super(DMainFrame, self).setWindowIcon(qicon)

        self.systemTray.setIcon(qicon)
        self.systemTray.show()

    def setWindowTitle(self, title):
        super(DMainFrame, self).setWindowTitle(title)

    def moveCenter(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def mousePressEvent(self, event):
        self.setFocus()
        # 鼠标点击事件
        if event.button() == Qt.LeftButton:
            self.dragPosition = event.globalPos() - \
                self.frameGeometry().topLeft()
            event.accept()

        self.xPos = self.x()
        self.yPos = self.y()
        self.rdragx = event.x()
        self.rdragy = event.y()
        self.currentWidth = self.width()
        self.currentHeight = self.height()
        self.isSideClicked = True

    def mouseReleaseEvent(self, event):
        # 鼠标释放事件
        if hasattr(self, "dragPosition"):
            del self.dragPosition
            self.isSideClicked = False
            self.setCursor(Qt.ArrowCursor)

    def mouseMoveEvent(self, event):
        self.oldPosition = self.pos()
        if self.isSideClicked and self.isCusorRightSide:
            w = max(self.minimumWidth(),
                    self.currentWidth + event.x() - self.rdragx)
            h = self.currentHeight
            self.resize(w, h)
        elif self.isSideClicked and self.isCusorDownSide:
            w = self.currentWidth
            h = max(self.minimumHeight(),
                    self.currentHeight + event.y() - self.rdragy)
            self.resize(w, h)
        elif self.isSideClicked and self.isCusorBottomLeftSide:
            w = max(self.minimumWidth(),
                    self.currentWidth + event.x() - self.rdragx)
            h = max(self.minimumHeight(),
                    self.currentHeight + event.y() - self.rdragy)
            self.resize(w, h)
        else:
            # 鼠标移动事件
            if self.isMaximized():
                event.ignore()
            else:
                if hasattr(self, "dragPosition"):
                    if event.buttons() == Qt.LeftButton:
                        self.move(
                            event.globalPos() - self.dragPosition)
                        event.accept()

    def eventFilter(self, obj, event):
        if event.type() == QEvent.HoverMove:
            if self.width() - event.pos().x() < 10 and self.height() - event.pos().y() > 10:
                self.setCursor(Qt.SizeHorCursor)
                self.isCusorRightSide = True
            elif self.height() - event.pos().y() < 10 and self.width() - event.pos().x() > 10:
                self.setCursor(Qt.SizeVerCursor)
                self.isCusorDownSide = True
            elif self.width() - event.pos().x() <= 10 and self.height() - event.pos().y() <= 10:
                self.setCursor(Qt.SizeFDiagCursor)
                self.isCusorBottomLeftSide = True
                self.isCusorRightSide = False
                self.isCusorDownSide = False
            elif not self.isSideClicked:
                self.setCursor(Qt.ArrowCursor)
                self.isCusorLeftSide = False
                self.isCusorRightSide = False
                self.isCusorDownSide = False
                self.isCusorBottomLeftSide = False
            return True
        return super(DMainFrame, self).eventFilter(obj, event)

    # def resizeEvent(self, event):
    #     image = QImage(self.size(), QImage.Format_Mono)
    #     image.fill(0)
    #     image.setPixel(0, 0, 1)
    #     image.setPixel(1, 0, 1)
    #     image.setPixel(2, 0, 1)
    #     image.setPixel(3, 0, 1)
    #     image.setPixel(0, 1, 1)
    #     image.setPixel(1, 1, 1)
    #     image.setPixel(0, 2, 1)
    #     image.setPixel(0, 3, 1)

    #     image.setPixel(self.width() - 4, 0, 1) 
    #     image.setPixel(self.width() - 3, 0, 1) 
    #     image.setPixel(self.width() - 2, 0, 1) 
    #     image.setPixel(self.width() - 1, 0, 1)                                                    
    #     image.setPixel(self.width() - 2, 1, 1) 
    #     image.setPixel(self.width() - 1, 1, 1)
    #     image.setPixel(self.width() - 1, 2, 1)
    #     image.setPixel(self.width() - 1, 3, 1)

    #     image.setPixel(0, self.height() - 4, 1)
    #     image.setPixel(0, self.height() - 3, 1)
    #     image.setPixel(0, self.height() - 2, 1) 
    #     image.setPixel(1, self.height() - 2, 1)
    #     image.setPixel(0, self.height() - 1, 1) 
    #     image.setPixel(1, self.height() - 1, 1) 
    #     image.setPixel(2, self.height() - 1, 1) 
    #     image.setPixel(3, self.height() - 1, 1)

    #     image.setPixel(self.width() - 1, self.height() - 3, 1)                                                               
    #     image.setPixel(self.width() - 2, self.height() - 2, 1)
    #     image.setPixel(self.width() - 1, self.height() - 2, 1)
    #     image.setPixel(self.width() - 4, self.height() - 1, 1)
    #     image.setPixel(self.width() - 3, self.height() - 1, 1) 
    #     image.setPixel(self.width() - 2, self.height() - 1, 1) 
    #     image.setPixel(self.width() - 1, self.height() - 1, 1)
    #     self.setMask(QBitmap.fromImage(image))
    #     super(DMainFrame, self).resizeEvent(event)
