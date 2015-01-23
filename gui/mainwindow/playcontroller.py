#!/usr/bin/python
# -*- coding: utf-8 -*-

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from gui.utils import views
from database import signal_DB
from log import logger


class PlayController(QObject):

    """docstring for PlayController"""

    def __init__(self, parent=None):
        super(PlayController, self).__init__()
        self.parent = parent
        self.initConnect()
        self.test()

    def initConnect(self):
        signal_DB.songInfo.connect(views['MusicInfoFrame'].updateContent)

    def test(self):
        info = {
            'cover': 'gui/skin/images/bg2.jpg',
            'title': 'dragon',
            'artist': 'unknown'
        }
        signal_DB.songInfo.emit(info)
