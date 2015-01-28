#!/usr/bin/python
# -*- coding: utf-8 -*-

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from gui.utils import views
from database import signal_DB
from .titlebarcontroller import TitleBarController
from .settingmenucontroller import SettingMenuController
from .pagecontroller import PageController
from .playcontroller import PlayController
from log import logger


class GuiManger(QObject):

    """docstring for GuiManger"""

    def __init__(self, parent=None):
        super(GuiManger, self).__init__()
        self.parent = parent
        self.initControllers()
        self.initGlobalConnect()

    def initControllers(self):
        self.titleBarController = TitleBarController()
        self.settingMenuController = SettingMenuController()
        self.pageController = PageController()
        self.playController = PlayController()

    def initGlobalConnect(self):
        signal_DB.closed.connect(self.close)

    def close(self):
        app = QApplication.instance()
        app.closeAllWindows()
        app.quit()
