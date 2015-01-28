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


from gui import MainWindow
from gui.dwidgets import QSingleApplication
import gui.uiconfig as config
from log import logger


if __name__ == '__main__':
    if sys.platform == "linux2":
        QApplication.addLibraryPath(
            '/usr/lib/%s-linux-gnu/qt5/plugins/' % platform.machine())
    app = QSingleApplication(config.applicationName, sys.argv)
    app.setApplicationName(config.applicationName)
    app.setApplicationVersion(config.applicationVersion)
    app.setOrganizationName(config.organizationName)

    if app.isRunning():
        sys.exit(0)

    mainwindow = MainWindow()
    app.setActivationWindow(mainwindow)
    mainwindow.show()

    mainwindow.guimanger.globals = globals()
    mainwindow.guimanger.locals = locals()

    exitCode = app.exec_()
    sys.exit(exitCode)
