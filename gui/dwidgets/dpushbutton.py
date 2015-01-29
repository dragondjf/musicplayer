#!/usr/bin/python
# -*- coding: utf-8 -*-

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QCursor
from PyQt5.QtWidgets import QPushButton


class DPushButton(QPushButton):

    def __init__(self, text, parent=None):
        super(DPushButton, self).__init__(text, parent)
        self.setFocusPolicy(Qt.NoFocus)

    def setMenu(self, menu):
        super(DPushButton, self).setMenu(menu)
        menu.aboutToHide.connect(self.recover)

    def recover(self):
        import sys
        if sys.platform == "linux2":
            self.setAttribute(Qt.WA_UnderMouse, self.rect().contains(self.mapFromGlobal(QCursor.pos())))
            self.update()
