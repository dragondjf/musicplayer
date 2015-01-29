#!/usr/bin/python
# -*- coding: utf-8 -*-

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from gui.utils import collectView
from .coveritem import CoverArtistItem

group_adjacent = lambda a, k: zip(*([iter(a)] * k))


class ArtistPage(QFrame):

    viewID = 'ArtistPage'

    @collectView
    def __init__(self, parent=None):
        super(ArtistPage, self).__init__(parent)
        self.setObjectName(self.viewID)
        self.initData()
        self.initUI()
        self.update()

    def initData(self):
        pass

    def initUI(self):
        self.artistTable = ArtistTable()
        mainLayout = QVBoxLayout()
        mainLayout.addWidget(self.artistTable)
        mainLayout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(mainLayout)

    def update(self, info=None):
        infos = {
            'cover': 'gui/skin/images/bg2.jpg',
            'count': '42',
            'artist': 'dragon'
        }
        info = group_adjacent(range(15), 5)
        self.artistTable.setRowCount(len(info))
        self.artistTable.setColumnCount(5)
        self.artistTable.setColumnWidth(0, 150)
        self.artistTable.setColumnWidth(1, 150)
        self.artistTable.setColumnWidth(2, 150)
        self.artistTable.setColumnWidth(3, 150)
        self.artistTable.setColumnWidth(4, 150)
        for row, items in enumerate(info):
            self.artistTable.setRowHeight(row, 150)
            for col, item in enumerate(items):
                self.artistTable.setColumnWidth(col, 150)
                newItem = QTableWidgetItem()
                newItem.setTextAlignment(Qt.AlignCenter)
                artistItem = CoverArtistItem(self)
                artistItem.setFixedSize(150, 150)
                artistItem.updateContent(infos)
                self.artistTable.setItem(row, col, newItem)
                self.artistTable.setCellWidget(row, col, artistItem)




class ArtistTable(QTableWidget):

    def __init__(self, rows=0, cloumns=5, parent=None):
        super(ArtistTable, self).__init__(rows, cloumns, parent)
        self.parent = parent
        self.setEditTriggers(self.NoEditTriggers)
        self.setSelectionBehavior(self.SelectItems)
        self.setSelectionMode(self.NoSelection)
        self.setFocusPolicy(Qt.NoFocus)
        self.horizontalHeader().setVisible(False)
        self.verticalHeader().setVisible(False)
        self.setShowGrid(False)
