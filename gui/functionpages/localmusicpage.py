#!/usr/bin/python
# -*- coding: utf-8 -*-

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from gui.dwidgets import DPushButton
from gui.menus import ClassifyMenu
from gui.utils import collectView
from .localpages import AlbumPage, ArtistPage, SongPage, FolderPage


class LocalMusicPage(QFrame):

    viewID = 'LocalMusicPage'

    @collectView
    def __init__(self, parent=None):
        super(LocalMusicPage, self).__init__(parent)
        self.setObjectName(self.viewID)
        self.initData()
        self.initUI()

    def initData(self):
        pass

    def initUI(self):
        self.classifyButton = DPushButton(self.tr('按歌手'), self)
        self.classifyButton.setFocusPolicy(Qt.NoFocus)
        self.classifyMenu = ClassifyMenu()
        self.classifyButton.setMenu(self.classifyMenu)

        self.artistPage = ArtistPage()
        self.albumPage = AlbumPage()
        self.songPage = SongPage()
        self.folderPage = FolderPage()

        topLayout =  QHBoxLayout()
        topLayout.addSpacing(20)
        topLayout.addWidget(self.classifyButton)
        topLayout.addStretch()

        self.stackLayout = QStackedLayout()
        self.stackLayout.addWidget(self.artistPage)
        self.stackLayout.addWidget(self.albumPage)
        self.stackLayout.addWidget(self.songPage)
        self.stackLayout.addWidget(self.folderPage)

        mainLayout = QVBoxLayout()
        mainLayout.addLayout(topLayout)
        mainLayout.addLayout(self.stackLayout)
        mainLayout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(mainLayout)
