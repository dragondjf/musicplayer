#!/usr/bin/python
# -*- coding: utf-8 -*-

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from config import constants
from gui.utils import collectView


class BaseToolButton(QToolButton):

    w = 45
    h = 45

    def __init__(self, parent=None):
        super(BaseToolButton, self).__init__(parent)
        self.setFocusPolicy(Qt.NoFocus)
        iconBaseSize = QSize(self.w, self.h)
        self.setFixedSize(self.w, self.h)


class MusicBottomBar(QFrame):

    viewID = 'MusicBottomBar'

    @collectView
    def __init__(self, parent=None):
        super(MusicBottomBar, self).__init__(parent)
        self.setObjectName(self.viewID)
        self.initData()
        self.initUI()

    def initData(self):
        pass

    def initUI(self):
        self.setFixedHeight(constants.Bottom_Height)

        self.musicSlider = QSlider(Qt.Horizontal, self)
        self.musicSlider.setRange(0, 100)
        self.musicSlider.setPageStep(5)
        self.musicSlider.setSingleStep(1)
        self.musicSlider.setFixedHeight(5)
        self.musicInfoFrame = MusicInfoFrame(self)
        self.musicPlayBar = MusicPlayBar(self)
        self.musicToolBar = MusicToolBar(self)

        musicLayout = QHBoxLayout()
        musicLayout.addSpacing(25)
        musicLayout.addWidget(self.musicInfoFrame)
        musicLayout.addStretch()
        musicLayout.addWidget(self.musicPlayBar)
        musicLayout.addStretch()
        musicLayout.addWidget(self.musicToolBar)
        musicLayout.addSpacing(25)
        musicLayout.setContentsMargins(0, 0, 0, 0)
        musicLayout.setSpacing(0)

        mainLayout = QVBoxLayout()
        mainLayout.addWidget(self.musicSlider)
        mainLayout.addLayout(musicLayout)
        mainLayout.setContentsMargins(0, 0, 0, 0)
        mainLayout.setSpacing(0)
        self.setLayout(mainLayout)


class CoverLabel(QLabel):

    viewID = 'CoverLabel'

    @collectView
    def __init__(self, parent=None):
        super(CoverLabel, self).__init__(parent)

    def setPixmap(self, pic):
        qpic = None
        if isinstance(pic, QPixmap):
            qpic = pic
        else:
            qpic = QPixmap(pic)
        super(CoverLabel, self).setPixmap(qpic)


class MusicInfoFrame(QFrame):

    viewID = 'MusicInfoFrame'

    @collectView
    def __init__(self, parent=None):
        super(MusicInfoFrame, self).__init__(parent)
        self.initData()
        self.initUI()

    def initData(self):
        pass

    def initUI(self):
        self.setFixedWidth(300)

        self.coverLabel = CoverLabel(self)
        self.coverLabel.setFixedWidth(60)

        self.titleLabel = QLabel(self)
        self.titleLabel.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)

        self.artistLabel = QLabel(self)
        self.artistLabel.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)


        self.songTimeFrame = QFrame(self)
        self.songTimeLabel = QLabel('01:21/04:39', self)
        self.songTimeLabel.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        timeLayout = QHBoxLayout()
        timeLayout.addWidget(self.songTimeLabel)
        timeLayout.setContentsMargins(0, 0, 0, 0)
        timeLayout.setSpacing(0)
        self.songTimeFrame.setLayout(timeLayout)

        infoLayout = QVBoxLayout()
        infoLayout.addWidget(self.titleLabel)
        infoLayout.addWidget(self.artistLabel)
        infoLayout.addWidget(self.songTimeFrame)
        infoLayout.setContentsMargins(0, 0, 0, 0)
        infoLayout.setSpacing(0)

        mainLayout = QHBoxLayout()
        mainLayout.addWidget(self.coverLabel)
        mainLayout.addSpacing(10)
        mainLayout.addLayout(infoLayout)
        mainLayout.addStretch()
        mainLayout.setContentsMargins(0, 20, 0, 20)
        mainLayout.setSpacing(0)

        self.setLayout(mainLayout)

    def updateContent(self, info):
        cover = info['cover']
        title = info['title']
        artist = info['artist']
        self.coverLabel.setStyleSheet('''
            border-image: url(%s);
            ''' % cover)
        self.titleLabel.setText(title)
        self.artistLabel.setText(artist)


class MusicPlayBar(QFrame):

    viewID = 'MusicPlayBar'

    @collectView
    def __init__(self, parent=None):
        super(MusicPlayBar, self).__init__(parent)
        self.initData()
        self.initUI()

    def initData(self):
        pass

    def initUI(self):
        self.preButton = BaseToolButton()
        self.preButton.setObjectName('PreButton')

        self.playButton = BaseToolButton()
        self.playButton.setObjectName('PlayButton')

        self.nextButton = BaseToolButton()
        self.nextButton.setObjectName('NextButton')

        toolLayout = QHBoxLayout()
        toolLayout.addWidget(self.preButton)
        toolLayout.addWidget(self.playButton)
        toolLayout.addWidget(self.nextButton)
        toolLayout.setContentsMargins(0, 0, 0, 0)
        toolLayout.setSpacing(0)

        mainLayout = QVBoxLayout()
        mainLayout.addStretch()
        mainLayout.addLayout(toolLayout)
        mainLayout.addStretch()
        mainLayout.setContentsMargins(0, 0, 0, 0)
        mainLayout.setSpacing(0)

        self.setLayout(mainLayout)


class MusicToolBar(QFrame):

    viewID = 'MusicToolBar'

    @collectView
    def __init__(self, parent=None):
        super(MusicToolBar, self).__init__(parent)
        self.initData()
        self.initUI()

    def initData(self):
        pass

    def initUI(self):

        self.setFixedWidth(300)

        self.volumeButton = BaseToolButton()
        self.volumeButton.setObjectName('VolumeButton')

        self.playOrderButton = BaseToolButton()
        self.playOrderButton.setObjectName('PlayOrderButton')

        self.lrcButton = BaseToolButton()
        self.lrcButton.setObjectName('LrcButton')

        self.playListButton = BaseToolButton()
        self.playListButton.setObjectName('PlayListButton')

        toolLayout = QHBoxLayout()
        toolLayout.addStretch()
        toolLayout.addWidget(self.volumeButton)
        toolLayout.addWidget(self.playOrderButton)
        toolLayout.addWidget(self.lrcButton)
        toolLayout.addWidget(self.playListButton)
        

        mainLayout = QVBoxLayout()
        mainLayout.addStretch()
        mainLayout.addLayout(toolLayout)
        mainLayout.addStretch()
        mainLayout.setContentsMargins(0, 0, 0, 0)
        mainLayout.setSpacing(0)

        self.setLayout(mainLayout)
