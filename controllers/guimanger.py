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
        self.test()

    def initControllers(self):
        self.titleBarController = TitleBarController()
        self.settingMenuController = SettingMenuController()
        self.pageController = PageController()
        self.playController = PlayController()

    def initGlobalConnect(self):
        signal_DB.closed.connect(self.close)
        signal_DB.backgroundimageChanged.connect(self.setBackgroundImage)

    def setBackgroundImage(self, imagepath):
        mainWindow = views['MainWindow']
        mainWindow.setStyleSheet('''
            QFrame#MainWindow{
                border-image: url(gui/skin/images/bear.jpg);
            }
        ''')

    def close(self):
        app = QApplication.instance()
        app.closeAllWindows()
        app.quit()

    def test(self):
        self.test_BackgroundImage()
        self.test_SongInfo()

    def test_BackgroundImage(self):
        url = 'gui/skin/images/bg2.jpg'
        signal_DB.backgroundimageChanged.emit(url)

    def test_SongInfo(self):
        info = {
            'cover': 'gui/skin/images/bg2.jpg',
            'title': 'dragon',
            'artist': 'unknown'
        }
        signal_DB.songInfo.emit(info)
