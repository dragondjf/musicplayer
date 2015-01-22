#!/usr/bin/python
# -*- coding: utf-8 -*-


import os
import sys
import platform
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5 import QtCore
QtCore.Signal = QtCore.pyqtSignal
QtCore.Slot = QtCore.pyqtSlot
QtCore.Property = QtCore.pyqtProperty

from qframer import FSplashScreen

from gui import MainWindow
from gui.uiconfig import windowsoptions

from log import logger

if __name__ == '__main__':
    if sys.platform == "linux2":
        QApplication.addLibraryPath(
            '/usr/lib/%s-linux-gnu/qt5/plugins/' % platform.machine())
    app = QApplication(sys.argv)
    if windowsoptions['splashflag']:
        splash = FSplashScreen(1, windowsoptions['splashimg'])
        mainwindow = MainWindow()
        mainwindow.show()
        splash.finish(mainwindow)
    else:
        mainwindow = MainWindow()
        mainwindow.show()

    mainwindow.guimanger.globals = globals()
    mainwindow.guimanger.locals = locals()

    exitCode = app.exec_()
    sys.exit(exitCode)