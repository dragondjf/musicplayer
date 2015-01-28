#!/usr/bin/python
# -*- coding: utf-8 -*-

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from gui.utils import views
from database import signal_DB
from log import logger


class PageController(QObject):

    """docstring for PageController"""

    def __init__(self, parent=None):
        super(PageController, self).__init__()
        self.parent = parent
        self.initConnect()

    def initConnect(self):
        pageButtons = views['MusicLeftBar'].pageButtons
        musicStackPage = views['MusicStackPage']
        for button in pageButtons:
            button.clicked.connect(self.swicthPage)

    def swicthPage(self):
        pageButtons = views['MusicLeftBar'].pageButtons
        index = pageButtons.index(self.sender())
        musicStackPage = views['MusicStackPage']
        musicStackPage.setCurrentIndex(index)
