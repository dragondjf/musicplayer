#!/usr/bin/python
# -*- coding: utf-8 -*-

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


from gui.menus import SettingsMenu, SkinMenu
from gui.dwidgets import DTitleBar, DMainFrame
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
        # self.setskin()

    def initUI(self):
        self.initSize()

        self.setWindowIcon(config.windowIcon)
        self.setWindowTitle(config.windowTitle)

        self.initMenus()
        # self.initCentralWidget()

    def initSize(self):
        self.resize(constants.SimpleWindow_Width, constants.SimpleWindow_Height)
        self.moveCenter()

    def initMenus(self):
        self.settingsMenu = SettingsMenu(self)

    def _initSystemTray(self):
        pass
