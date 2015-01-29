#!/usr/bin/python
# -*- coding: utf-8 -*-

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from gui.utils import views
from database import signal_DB
from log import logger


class SimpleTitleBarController(QObject):

    """docstring for SimpleTitleBarController"""

    def __init__(self, parent=None):
        super(SimpleTitleBarController, self).__init__()
        self.parent = parent
        self.initConnect()

    def initConnect(self):
        titleBar = views['SimpleWindow'].simpleTitleBar
        simpleWindow = views['SimpleWindow']
        titleBar.settingMenuShowed.connect(
            titleBar.settingDownButton.showMenu)
        titleBar.modeChanged.connect(signal_DB.modeChanged)
        titleBar.minimized.connect(simpleWindow.showMinimized)
        titleBar.maximized.connect(self.switchWindow)
        titleBar.closed.connect(signal_DB.closed)

    def switchWindow(self, flag):
        simpleWindow = views['SimpleWindow']
        if flag:
            simpleWindow.showMaximized()
        else:
            simpleWindow.showNormal()
