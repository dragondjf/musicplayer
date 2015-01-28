#!/usr/bin/python
# -*- coding: utf-8 -*-

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from config import constants
from gui.utils import collectView


class LocalMusicPage(QFrame):

    viewID = 'LocalMusicPage'

    @collectView
    def __init__(self, parent=None):
        super(LocalMusicPage, self).__init__(parent)
        self.setObjectName(self.viewID)

    def initData(self):
        pass

    def initUI(self):
        pass
