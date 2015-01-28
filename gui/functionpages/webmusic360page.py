#!/usr/bin/python
# -*- coding: utf-8 -*-

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from gui.dwidgets import DWebkitBasePage
from config import constants
from gui.utils import collectView


class WebMusic360Page(DWebkitBasePage):

    viewID = 'WebMusic360Page'

    @collectView
    def __init__(self, parent=None):
        super(WebMusic360Page, self).__init__(parent)
        self.setObjectName(self.viewID)
        self.parent = parent
        self.initData()
        self.initUI()

    def initData(self):
        pass

    def initUI(self):
        url = QUrl('http://10.0.0.153:8093/')
        self.view.load(url)
