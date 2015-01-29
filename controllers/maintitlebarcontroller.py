#!/usr/bin/python
# -*- coding: utf-8 -*-

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from gui.utils import views
from database import signal_DB
from log import logger


class MainTitleBarController(QObject):

    """docstring for MainTitleBarController"""

    def __init__(self, parent=None):
        super(MainTitleBarController, self).__init__()
        self.parent = parent
        self.initConnect()

    def initConnect(self):
        titleBar = views['MainWindow'].mainTitleBar
        mainWindow = views['MainWindow']
        titleBar.settingMenuShowed.connect(
            titleBar.settingDownButton.showMenu)
        titleBar.modeChanged.connect(signal_DB.modeChanged)
        titleBar.minimized.connect(mainWindow.showMinimized)
        titleBar.maximized.connect(self.switchWindow)
        titleBar.closed.connect(signal_DB.closed)

    def switchWindow(self, flag):
        mainWindow = views['MainWindow']
        if flag:
            mainWindow.showMaximized()
        else:
            mainWindow.showNormal()

        mainWindow.setskin()
