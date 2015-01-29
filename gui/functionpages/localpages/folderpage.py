#!/usr/bin/python
# -*- coding: utf-8 -*-

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from gui.dwidgets import DPushButton
from gui.menus import ClassifyMenu
from gui.utils import collectView


class FolderPage(QFrame):

    viewID = 'FolderPage'

    @collectView
    def __init__(self, parent=None):
        super(FolderPage, self).__init__(parent)
        self.setObjectName(self.viewID)
        self.initData()
        self.initUI()

    def initData(self):
        pass

    def initUI(self):
        self.label = QLabel("Folder")
        mainLayout = QVBoxLayout()
        mainLayout.addWidget(self.label)
        self.setLayout(mainLayout)
