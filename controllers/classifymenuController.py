#!/usr/bin/python
# -*- coding: utf-8 -*-

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from gui.utils import views
from database import signal_DB
from log import logger


class ClassifyMenuController(QObject):

    """docstring for ClassifyMenuController"""

    def __init__(self, parent=None):
        super(ClassifyMenuController, self).__init__()
        self.parent = parent
        self.initConnect()

    def initConnect(self):
        for name, action in views['LocalMusicPage'].classifyMenu.qactions.items():
                if hasattr(self, 'action%s' % name):
                    action.triggered.connect(
                        getattr(self, 'action%s' % name)
                    )
                else:
                    action.triggered.connect(
                        getattr(self, 'actionNotImplement')
                    )

    def actionArtist(self):
        views['LocalMusicPage'].stackLayout.setCurrentIndex(0)

    def actionAlbum(self):
        views['LocalMusicPage'].stackLayout.setCurrentIndex(1)

    def actionSong(self):
        views['LocalMusicPage'].stackLayout.setCurrentIndex(2)

    def actionFolder(self):
        views['LocalMusicPage'].stackLayout.setCurrentIndex(3)

    def actionNotImplement(self):
        logger.info("actionNotImplement")
