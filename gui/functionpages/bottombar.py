#!/usr/bin/python
# -*- coding: utf-8 -*-

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from gui.uiconfig import constants


class BottomBar(QFrame):

    def __init__(self, parent=None):
        super(BottomBar, self).__init__(parent)
        self.setObjectName("bottomBar")
        self.setFixedHeight(constants.Bottom_Height)
