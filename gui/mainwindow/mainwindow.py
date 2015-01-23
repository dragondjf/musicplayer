#!/usr/bin/python
# -*- coding: utf-8 -*-

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


from ..menus import SettingsMenu, SkinMenu
from ..functionpages import MusicLeftBar, MusicBottomBar, MusicStackPage
from ..dwidgets import DMainWindow, DTitleBar
from ..utils import collectView, setSkinForApp
from .guimanger import GuiManger
from ..uiconfig import constants
import gui.uiconfig as uiconfig


class MainWindow(DMainWindow):

    viewID = "MainWindow"

    @collectView
    def __init__(self):
        super(MainWindow, self).__init__()
        self.initUI()
        self.setskin()
        self.guimanger = GuiManger()

    def initUI(self):
        self.initSize()

        self.setWindowIcon(uiconfig.windowIcon)
        self.setWindowTitle(uiconfig.windowTitle)

        self.initMenus()
        self.initCentralWidget()

        self.initSizeGrip()
        self.setSystemTrayMenu(self.settingsMenu)

    def initSize(self):
        self.resize(constants.MainWindow_Width, constants.MainWindow_Height)
        self.moveCenter()

    def initMenus(self):
        self.settingsMenu = SettingsMenu(self)

    def initCentralWidget(self):
        self.initTitleBar()
        self.initLeftBar()
        self.initMusicStackPage()
        self.initBottomBar()

        centralWidget = QFrame(self)

        pageLayout = QVBoxLayout()
        pageLayout.addWidget(self.musicTitleBar)
        pageLayout.addWidget(self.musicStackPage)
        pageLayout.setContentsMargins(0, 0, 0, 0)
        pageLayout.setSpacing(0)

        controlLayout = QHBoxLayout()
        controlLayout.addWidget(self.musicLeftBar)
        controlLayout.addLayout(pageLayout)
        controlLayout.setContentsMargins(0, 0, 0, 0)
        controlLayout.setSpacing(0)

        mainLayout = QVBoxLayout()
        mainLayout.addLayout(controlLayout)
        mainLayout.addWidget(self.musicBottomBar)
        mainLayout.setContentsMargins(0, 0, 0, 0)
        mainLayout.setSpacing(0)
        centralWidget.setLayout(mainLayout)
        self.setCentralWidget(centralWidget)

    def initTitleBar(self):
        self.musicTitleBar = DTitleBar(self)
        self.musicTitleBar.settingDownButton.setMenu(self.settingsMenu)

    def initLeftBar(self):
        self.musicLeftBar = MusicLeftBar(self)

    def initMusicStackPage(self):
        self.musicStackPage = MusicStackPage(self)

    def initBottomBar(self):
        self.musicBottomBar = MusicBottomBar(self)

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
