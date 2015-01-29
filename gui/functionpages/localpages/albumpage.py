#!/usr/bin/python
# -*- coding: utf-8 -*-

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from gui.utils import collectView
from .coveritem import CoverAlbumItem


class AlbumPage(QFrame):

    viewID = 'AlbumPage'

    @collectView
    def __init__(self, parent=None):
        super(AlbumPage, self).__init__(parent)
        self.setObjectName(self.viewID)
        self.initData()
        self.initUI()

    def initData(self):
        pass

    def initUI(self):
        self.label = QLabel("Album")
        mainLayout = QVBoxLayout()
        mainLayout.addWidget(self.label)
        self.setLayout(mainLayout)
