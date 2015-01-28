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
from gui.dwidgets import QSingleApplication
from app import DeepinPlayer
import config


if __name__ == '__main__':
    if sys.platform == "linux2":
        QApplication.addLibraryPath(
            '/usr/lib/%s-linux-gnu/qt5/plugins/' % platform.machine())
    app = QSingleApplication(config.applicationName, sys.argv)

    if app.isRunning():
        sys.exit(0)

    deepinPlayer = DeepinPlayer()
    app.setActivationWindow(deepinPlayer.mainWindow)
    deepinPlayer.show()

    exitCode = app.exec_()
    sys.exit(exitCode)
