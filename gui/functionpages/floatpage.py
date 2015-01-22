#!/usr/bin/python
# -*- coding: utf-8 -*-

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from qframer import FFloatWidget


class FloatPage(FFloatWidget):

    def __init__(self, parent=None):
        super(FloatPage, self).__init__(parent)
        self.setObjectName("FloatWidget")
        self.isShowed = False
