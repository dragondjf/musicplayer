#!/usr/bin/python
# -*- coding: utf-8 -*-

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from qframer.animationwidget import FAnimationFrame


class AboutPage(FAnimationFrame):

    style = '''
        QFrame#About{
            border-image: url(gui/skin/images/bear.jpg);
        }
    '''

    def __init__(self, parent=None):
        super(AboutPage, self).__init__(parent)
        self.setObjectName("About")
        self.setStyleSheet(self.style)
