#!/usr/bin/python
# -*- coding: utf-8 -*-

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class CoverArtistItem(QFrame):


    def __init__(self, parent=None):
        super(CoverArtistItem, self).__init__(parent)
        self.initData()
        self.initUI()

    def initData(self):
        pass

    def initUI(self):
        self.coverLabel = QLabel()
        self.coverLabel.setFixedSize(100, 100)
        self.artistLabel = QLabel()
        self.countLabel = QLabel()

        mainLayout = QVBoxLayout()
        mainLayout.addWidget(self.coverLabel)
        mainLayout.addWidget(self.artistLabel)
        mainLayout.addWidget(self.countLabel)
        mainLayout.setContentsMargins(25, 5, 25, 5)
        mainLayout.setSpacing(0)
        self.setLayout(mainLayout)


    def updateContent(self, info):
        cover = info['cover']
        artist = info['artist']
        count = info['count']
        self.coverLabel.setStyleSheet('''
            border-image: url(%s);
            ''' % cover)
        self.artistLabel.setText(artist)
        self.countLabel.setText(count)


class CoverAlbumItem(QFrame):


    def __init__(self, parent=None):
        super(CoverAlbumItem, self).__init__(parent)
        self.initData()
        self.initUI()

    def initData(self):
        pass

    def initUI(self):
        self.coverlabel = QLabel()
        self.albumlabel = QLabel()
        self.artistlabel = QLabel()

        mainLayout = QVBoxLayout()
        mainLayout.addWidget(self.coverlabel)
        mainLayout.addWidget(self.albumlabel)
        mainLayout.addWidget(self.artistlabel)
        self.setLayout(mainLayout)

    def updateContent(self, info):
        cover = info['cover']
        album = info['album']
        artist = info['count']
        self.coverLabel.setStyleSheet('''
            border-image: url(%s);
            ''' % cover)
        self.albumlabel.setText(album)
        self.artistLabel.setText(artist)
