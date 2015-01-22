#!/usr/bin/python
# -*- coding: utf-8 -*-

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from qframer import views, collectView
from qframer import FMainWindow
from qframer import FSuspensionWidget
from qframer import setSkinForApp

from gui.uiconfig import windowsoptions
from gui.menus import SettingsMenu, SkinMenu
from gui.floatwindows import LogWindow, HistoryWindow
from gui.floatwindows import InitHistoryWindow, FloatWindow
from gui.functionpages import LeftBar, BottomBar
from gui.dwidgets import DMainWindow, DTitleBar
from .guimanger import GuiManger
from gui.uiconfig import constants


class MainWindow(DMainWindow):

    viewID = "MainWindow"

    @collectView
    def __init__(self):
        super(MainWindow, self).__init__()
        self.initUI()
        self.setskin()
        self.guimanger = GuiManger()

    def initUI(self):
        mainwindow = windowsoptions['mainwindow']
        self.initSize()

        self.setWindowIcon(mainwindow['icon'])
        self.setWindowTitle(mainwindow['title'])

        self.initMenus()

        self.setCentralWidget(QLabel(self))

        self.initSizeGrip()
        self.setSystemTrayMenu(self.settingsMenu)

    def initSize(self):
        mainwindow = windowsoptions['mainwindow']
        desktopWidth = QDesktopWidget().availableGeometry().width()
        desktopHeight = QDesktopWidget().availableGeometry().height()
        self.resize(
            desktopWidth * mainwindow['size'][0],
            desktopHeight * mainwindow['size'][1])
        self.moveCenter()

    def initMenus(self):
        self.settingsMenu = SettingsMenu(self)

    def initTitleBar(self):
        self.titleBar = DTitleBar(self)
        self.titleBar.settingDownButton.setMenu(self.settingsMenu)

    def initLeftBar(self):
        self.leftBar = LeftBar(self)

    def initBottomBar(self):
        self.bottomBar = BottomBar(self)

    def setCentralWidget(self, widget):

        self.initTitleBar()
        self.initLeftBar()
        self.initBottomBar()

        centralWidget = QFrame(self)

        pageLayout = QVBoxLayout()
        pageLayout.addWidget(self.titleBar)
        pageLayout.addWidget(widget)
        pageLayout.setContentsMargins(0, 0, 0, 0)
        pageLayout.setSpacing(0)

        controlLayout = QHBoxLayout()
        controlLayout.addWidget(self.leftBar)
        controlLayout.addLayout(pageLayout)
        controlLayout.setContentsMargins(0, 0, 0, 0)
        controlLayout.setSpacing(0)

        mainLayout = QVBoxLayout()
        mainLayout.addLayout(controlLayout)
        mainLayout.addWidget(self.bottomBar)
        mainLayout.setContentsMargins(0, 0, 0, 0)
        mainLayout.setSpacing(0)
        centralWidget.setLayout(mainLayout)
        super(MainWindow, self).setCentralWidget(centralWidget)

    def initSizeGrip(self):
        self.sizeGrip = QSizeGrip(self)
        self.sizeGrip.show()

    def setskin(self, skinID="default"):
        setSkinForApp('gui/skin/qss/%s.qss' % skinID)  # 设置主窗口样式

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Escape:
            self.guimanger.actionExit()
        elif event.key() == Qt.Key_F11:
            pass
        elif event.key() == Qt.Key_F9:
            pass
        elif event.key() == Qt.Key_F8:
            pass
        elif event.key() == Qt.Key_F12:
            self.guimanger.actionObjectView()
        else:
            super(MainWindow, self).keyPressEvent(event)

    def resizeEvent(self, event):
        super(MainWindow, self).resizeEvent(event)
        self.sizeGrip.move(
            self.size().width() - 100, self.size().height() - 30)
