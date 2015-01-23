#!/usr/bin/python
# -*- coding: utf-8 -*-

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from .webmusic360page import WebMusic360Page
from .localmusicpage import LocalMusicPage
from .playlistpage import PlayListPage
from .downloadpage import DownLoadPage
from ..utils import collectView


class MusicStackPage(QStackedWidget):

    viewID = "MusicStackPage"

    @collectView
    def __init__(self, parent=None):
        super(MusicStackPage, self).__init__(parent)
        self.initData()
        self.initUI()

    def initData(self):
        self.pages = []

    def initUI(self):
        self.webMusic360Page = WebMusic360Page(self)
        self.localMusicPage = LocalMusicPage(self)
        self.playListPage = PlayListPage(self)
        self.downloadPage = DownLoadPage(self)

        self.addWidget(self.webMusic360Page)
        self.addWidget(self.localMusicPage)
        self.addWidget(self.playListPage)
        self.addWidget(self.downloadPage)
