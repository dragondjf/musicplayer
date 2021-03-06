#!/usr/bin/python
# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import *
from gui import MainWindow, SimpleWindow
from controllers import GuiManger
from log import logger
import config


class DeepinPlayer(object):

    def __init__(self):
        self.initApplication()
        self.loadDB()
        self.initView()
        self.initControllers()

    def initApplication(self):
        qApp.setApplicationName(config.applicationName)
        qApp.setApplicationVersion(config.applicationVersion)
        qApp.setOrganizationName(config.organizationName)

    def loadDB(self):
        pass

    def initView(self):
        self.mainWindow = MainWindow()
        self.simpleWindow = SimpleWindow()

        # from objbrowser import browse
        # a = {
        #     '1' : 'dfdffd',
        #     '2': 'fddffd'
        # }
        # browse(a)

    def initControllers(self):
        self.guimanger = GuiManger()

    def show(self):
        self.mainWindow.show()
