#!/usr/bin/python
# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import *
from gui import MainWindow
from log import logger
import config


class DeepinPlayer(object):

    def __init__(self):
        self.initApplication()
        self.loadDB()
        self.initMainWindow()

    def initApplication(self):
        qApp.setApplicationName(config.applicationName)
        qApp.setApplicationVersion(config.applicationVersion)
        qApp.setOrganizationName(config.organizationName)

    def loadDB(self):
        pass

    def initMainWindow(self):
        self.mainWindow = MainWindow()
        self.mainWindow.guimanger.globals = globals()
        self.mainWindow.guimanger.locals = locals()

    def show(self):
        self.mainWindow.show()
