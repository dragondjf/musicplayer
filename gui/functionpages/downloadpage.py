#!/usr/bin/python
# -*- coding: utf-8 -*-

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from config import constants
from gui.utils import collectView


class DownLoadPage(QFrame):

    viewID = 'DownLoadPage'

    @collectView
    def __init__(self, parent=None):
        super(DownLoadPage, self).__init__(parent)
        self.setObjectName(self.viewID)

    def initData(self):
        pass

    def initUI(self):
        pass
