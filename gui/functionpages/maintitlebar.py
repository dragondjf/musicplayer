#!/usr/bin/python
# -*- coding: utf-8 -*-

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

baseHeight = 25


class BaseToolButton(QToolButton):

    def __init__(self, parent=None):
        super(BaseToolButton, self).__init__(parent)
        self.setFocusPolicy(Qt.NoFocus)
        iconBaseSize = QSize(baseHeight, baseHeight)
        self.setIconSize(iconBaseSize)
        self.setFixedSize(30, baseHeight)

    def setMenu(self, menu):
        super(BaseToolButton, self).setMenu(menu)
        menu.aboutToHide.connect(self.recover)

    def recover(self):
        import sys
        if sys.platform == "linux2":
            self.setAttribute(Qt.WA_UnderMouse, self.rect().contains(self.mapFromGlobal(QCursor.pos())))
            self.update()


class MainTitleBar(QFrame):

    settingMenuShowed = Signal()
    modeChanged = Signal(str)
    minimized = Signal()
    maximized = Signal(bool)
    closed = Signal()

    def __init__(self, parent=None):
        super(MainTitleBar, self).__init__(parent)
        self.initData()
        self.initUI()

    def initData(self):
        self.max_flag = False
        self.mode_flag = True

    def initUI(self):
        self.setFixedHeight(baseHeight)

        self.settingDownButton = BaseToolButton()
        self.settingDownButton.setObjectName("settingDownButton")

        self.modeButton = BaseToolButton()
        self.modeButton.setObjectName("fullModeButton")

        self.minButton = BaseToolButton()
        self.minButton.setObjectName("minButton")

        self.maxButton = BaseToolButton()
        self.maxButton.setObjectName("normalButton")

        self.closeButton = BaseToolButton()
        self.closeButton.setObjectName("closeButton")

        mainLayout = QHBoxLayout()
        mainLayout.addStretch()
        mainLayout.addWidget(self.settingDownButton)
        mainLayout.addWidget(self.modeButton)
        mainLayout.addWidget(self.minButton)
        mainLayout.addWidget(self.maxButton)
        mainLayout.addWidget(self.closeButton)
        mainLayout.setContentsMargins(0, 0, 5, 0)
        mainLayout.setSpacing(0)
        self.setLayout(mainLayout)

        self.settingDownButton.clicked.connect(self.settingMenuShowed)
        self.modeButton.clicked.connect(self.changeMode)
        self.minButton.clicked.connect(self.minimized)
        self.maxButton.clicked.connect(self.swicthMax)
        self.closeButton.clicked.connect(self.closed)

    def changeMode(self):
        self.modeChanged.emit('simple')

    def swicthMax(self):
        if self.max_flag:
            self.maxButton.setObjectName("normalButton")
        else:
            self.maxButton.setObjectName("maxButton")
        self.max_flag = not self.max_flag
        self.maximized.emit(self.max_flag)

    def mouseDoubleClickEvent(self, event):
        self.maxButton.click()

    def setLogo(self, icon):
        if isinstance(icon, QIcon):
            logoIcon = icon
        else:
            logoIcon = QIcon(icon)
        self.logoButton.setIcon(logoIcon)

    def setTitle(self, text):
        self.titleLabel.setText(text)

    def getTitle(self):
        return self.titleLabel.text()

    def isMax(self):
        return self.max_flag
