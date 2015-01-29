#!/usr/bin/python
# -*- coding: utf-8 -*-

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


from gui.menus import SettingsMenu
from gui.dwidgets import DMainFrame
from gui.functionpages import SimpleTitleBar, SimpleMusicBottomBar
from gui.utils import collectView, setSkinForApp
from config import constants
import config


class SimpleWindow(DMainFrame):

    viewID = "SimpleWindow"

    @collectView
    def __init__(self):
        super(SimpleWindow, self).__init__()
        self.setObjectName(self.viewID)
        self.initUI()

    def initUI(self):
        self.initSize()

        self.setWindowIcon(config.windowIcon)
        self.setWindowTitle(config.windowTitle)

        self.initMenus()
        self.initCentralWidget()

    def initSize(self):
        self.resize(constants.SimpleWindow_Width, constants.SimpleWindow_Height)
        self.moveCenter()

    def initMenus(self):
        self.settingsMenu = SettingsMenu(self)

    def _initSystemTray(self):
        pass

    def initCentralWidget(self):
        self.initTitleBar()
        self.initSimpleStackPage()
        self.initBottomBar()

        centralWidget = QFrame(self)

        mainLayout = QVBoxLayout()
        mainLayout.addWidget(self.simpleTitleBar)
        # mainLayout.addWidget(self.simpleStackPage)
        mainLayout.addStretch()
        mainLayout.addWidget(self.simpleMusicBottomBar)
        mainLayout.setContentsMargins(0, 0, 0, 0)
        mainLayout.setSpacing(0)
        centralWidget.setLayout(mainLayout)
        self.setCentralWidget(centralWidget)

    def initTitleBar(self):
        self.simpleTitleBar = SimpleTitleBar(self)
        self.simpleTitleBar.settingDownButton.setMenu(self.settingsMenu)

    def initSimpleStackPage(self):
        pass

    def initBottomBar(self):
        self.simpleMusicBottomBar = SimpleMusicBottomBar()
