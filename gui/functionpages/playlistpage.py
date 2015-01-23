#!/usr/bin/python
# -*- coding: utf-8 -*-

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from gui.uiconfig import constants
from ..utils import collectView


class PlayListPage(QFrame):

    viewID = 'PlayListPage'

    @collectView
    def __init__(self, parent=None):
        super(PlayListPage, self).__init__(parent)
        self.setObjectName(self.viewID)

    def initData(self):
        pass

    def initUI(self):
        pass
