#!/usr/bin/python
# -*- coding: utf-8 -*-

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from qframer import collectView
from qframer import FWebkitBasePage


class WebKitPage(FWebkitBasePage):

    viewID = "WebKitPage"

    @collectView
    def __init__(self, parent=None):
        super(WebKitPage, self).__init__(parent)
        self.setObjectName("WebKitPage")
        self.parent = parent
        self.initData()
        self.initUI()

    def initData(self):
        pass

    def initUI(self):
        url = QUrl("http://www.baidu.com")
        self.view.load(url)
