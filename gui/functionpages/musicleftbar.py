#!/usr/bin/python
# -*- coding: utf-8 -*-

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from config import constants
from gui.utils import collectView

baseWidth = 60
baseHeight = 60


class BaseToolButton(QToolButton):

    def __init__(self, parent=None):
        super(BaseToolButton, self).__init__(parent)
        self.setFocusPolicy(Qt.NoFocus)
        # self.setFlat(True)
        self.setCheckable(True)
        iconBaseSize = QSize(baseWidth, baseHeight)
        self.setIconSize(iconBaseSize)
        self.setFixedSize(baseWidth, baseHeight)

    def setMenu(self, menu):
        super(BaseToolButton, self).setMenu(menu)
        menu.aboutToHide.connect(self.recover)

    def recover(self):
        import sys
        if sys.platform == "linux2":
            self.setAttribute(Qt.WA_UnderMouse, self.rect().contains(self.mapFromGlobal(QCursor.pos())))
            self.update()


class MusicLeftBar(QFrame):

    viewID = 'MusicLeftBar'

    style = '''
        QToolButton#LogoButton{
            border-image: url(gui/skin/icons/dark/appbar.music.png);
            background-color: transparent;
        }

        QToolButton#LogoButton:hover{
            border-image: url(gui/skin/icons/light/appbar.music.png);
        }

        QToolButton#LogoButton:pressed{
            border-image: url(gui/skin/icons/dark/appbar.music.png);
        }

        QToolButton#WebMusic360Button{
            border-image: url(gui/skin/icons/dark/appbar.zune.png);
            background-color: transparent;
        }

        QToolButton#WebMusic360Button:hover{
            border-image: url(gui/skin/icons/light/appbar.zune.png);
        }

        QToolButton#WebMusic360Button:pressed{
            border-image: url(gui/skin/icons/dark/appbar.zune.png);
        }
        QToolButton#WebMusic360Button:checked{
            background-color: #00CD00;
            color: white;
        }

        QToolButton#LocalMusicButton{
            border-image: url(gui/skin/icons/dark/appbar.folder.png);
            background-color: transparent;
        }

        QToolButton#LocalMusicButton:hover{
            border-image: url(gui/skin/icons/light/appbar.folder.png);
        }

        QToolButton#LocalMusicButton:pressed{
            border-image: url(gui/skin/icons/dark/appbar.folder.png);
        }
        QToolButton#LocalMusicButton:checked{
            background-color: #00CD00;
            color: white;
        }

        QToolButton#PalylistButton{
            border-image: url(gui/skin/icons/dark/appbar.list.png);
            background-color: transparent;
        }

        QToolButton#PalylistButton:hover{
            border-image: url(gui/skin/icons/light/appbar.list.png);
        }

        QToolButton#PalylistButton:pressed{
            border-image: url(gui/skin/icons/dark/appbar.list.png);
        }
        QToolButton#PalylistButton:checked{
            background-color: #00CD00;
            color: white;
        }

        QToolButton#DownloadButton{
            border-image: url(gui/skin/icons/dark/appbar.download.png);
            background-color: transparent;
        }

        QToolButton#DownloadButton:hover{
            border-image: url(gui/skin/icons/light/appbar.download.png);
        }

        QToolButton#DownloadButton:pressed{
            border-image: url(gui/skin/icons/dark/appbar.download.png);
        }
        QToolButton#DownloadButton:checked{
            background-color: #00CD00;
            color: white;
        }

        QToolButton#SearchButton{
            border-image: url(gui/skin/icons/dark/appbar.magnify.png);
            background-color: transparent;
        }

        QToolButton#SearchButton:hover{
            border-image: url(gui/skin/icons/light/appbar.magnify.png);
        }

        QToolButton#SearchButton:pressed{
            border-image: url(gui/skin/icons/dark/appbar.magnify.png);
        }
    '''

    @collectView
    def __init__(self, parent=None):
        super(MusicLeftBar, self).__init__(parent)
        self.setObjectName(self.viewID)
        self.setFixedWidth(constants.LeftBar_Width)

        self.initData()
        self.initUI()

    def initData(self):
        self.pageButtons = []

    def initUI(self):
        self.logoButton = BaseToolButton(self)
        self.logoButton.setObjectName("LogoButton")

        self.webMusic360Button = BaseToolButton(self)
        self.webMusic360Button.setObjectName("WebMusic360Button")
        self.pageButtons.append(self.webMusic360Button)
        self.webMusic360Button.setChecked(True)

        self.localMusicButton = BaseToolButton(self)
        self.localMusicButton.setObjectName("LocalMusicButton")
        self.pageButtons.append(self.localMusicButton)

        self.palylistButton = BaseToolButton(self)
        self.palylistButton.setObjectName("PalylistButton")
        self.pageButtons.append(self.palylistButton)

        self.downloadButton = BaseToolButton(self)
        self.downloadButton.setObjectName("DownloadButton")
        self.pageButtons.append(self.downloadButton)

        self.searchButton = BaseToolButton(self)
        self.searchButton.setObjectName("SearchButton")

        mainLayout = QVBoxLayout()
        mainLayout.addWidget(self.logoButton)
        mainLayout.addWidget(self.webMusic360Button)
        mainLayout.addWidget(self.localMusicButton)
        mainLayout.addWidget(self.palylistButton)
        mainLayout.addStretch()
        mainLayout.addWidget(self.downloadButton)
        mainLayout.addWidget(self.searchButton)
        mainLayout.setContentsMargins(0, 0, 0, 0)
        mainLayout.setSpacing(0)
        self.setLayout(mainLayout)

        self.setStyleSheet(self.style)

        for button in self.pageButtons:
            button.clicked.connect(self.checkedButton)

    def checkedButton(self):
        self.sender().setChecked(True)
        for button in self.pageButtons:
            if button is not self.sender():
                button.setChecked(False)
