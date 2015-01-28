#!/usr/bin/python
# -*- coding: utf-8 -*-

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from gui.utils import views
from database import signal_DB
from log import logger


class SettingMenuController(QObject):

    """docstring for SettingMenuController"""

    def __init__(self, parent=None):
        super(SettingMenuController, self).__init__()
        self.parent = parent
        self.initConnect()

    def initConnect(self):
        for name, action in views['MainWindow'].settingsMenu.qactions.items():
                if hasattr(self, 'action%s' % name):
                    action.triggered.connect(
                        getattr(self, 'action%s' % name)
                    )
                else:
                    action.triggered.connect(
                        getattr(self, 'actionNotImplement')
                    )

    def actionAbout(self):
        pass

    def actionExit(self):
        signal_DB.closed.emit()

    def actionNotImplement(self):
        logger.info("actionNotImplement")
