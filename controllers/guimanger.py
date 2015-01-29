#!/usr/bin/python
# -*- coding: utf-8 -*-

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from gui.utils import views
from database import signal_DB
from .maintitlebarcontroller import MainTitleBarController
from .simpletitlebarcontroller import SimpleTitleBarController
from .settingmenucontroller import SettingMenuController
from .classifymenuController import ClassifyMenuController
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
        self.mainTitleBarController = MainTitleBarController()
        self.simpleTitleBarController = SimpleTitleBarController()
        self.settingMenuController = SettingMenuController()
        self.classifyMenuController = ClassifyMenuController()
        self.pageController = PageController()
        self.playController = PlayController()

    def initGlobalConnect(self):
        signal_DB.backgroundimageChanged.connect(self.setBackgroundImage)
        signal_DB.modeChanged.connect(self.changeMode)
        signal_DB.closed.connect(self.close)

    def setBackgroundImage(self, imagepath):
        mainWindow = views['MainWindow']
        mainWindow.setStyleSheet('''
            QFrame#MainWindow{
                border-image: url(%s);
            }
        ''' % imagepath)

        simpleWindow = views['SimpleWindow']
        simpleWindow.setStyleSheet('''
            QFrame#SimpleWindow{
                border-image: url(%s);
            }
        ''' % imagepath)

    def changeMode(self, mode):
        if mode == "simple":
            views['MainWindow'].hide()
            views['SimpleWindow'].show()
            views['SimpleWindow'].move(views['MainWindow'].pos())
        elif mode == "main":
            views['MainWindow'].show()
            views['SimpleWindow'].hide()
            views['MainWindow'].move(views['SimpleWindow'].pos())
        elif mode == "mini":
            views['MainWindow'].hide()
            views['SimpleWindow'].hide()

    def close(self):
        app = QApplication.instance()
        app.closeAllWindows()
        app.quit()

    def test(self):
        self.test_BackgroundImage()
        self.test_SongInfo()

    def test_BackgroundImage(self):
        url = 'gui/skin/images/bg4.jpg'
        signal_DB.backgroundimageChanged.emit(url)

    def test_SongInfo(self):
        info = {
            'cover': 'gui/skin/images/bg2.jpg',
            'title': 'dragon',
            'artist': 'unknown'
        }
        signal_DB.songInfo.emit(info)
