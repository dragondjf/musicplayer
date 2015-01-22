#!/usr/bin/python
# -*- coding: utf-8 -*-

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from qframer import views
from gui.functionpages import LoginPage, AboutPage, ExitPage
from database import signal_DB
from log import logger


class GuiManger(QObject):

    """docstring for GuiManger"""

    def __init__(self, parent=None):
        super(GuiManger, self).__init__()
        self.parent = parent
        self.titleBarConnect()
        self.settingMenuActionConnect()
        self.createControllers()

    def titleBarConnect(self):
        titleBar = views['MainWindow'].titleBar
        mainWindow = views['MainWindow']
        titleBar.settingMenuShowed.connect(
            titleBar.settingDownButton.showMenu)
        titleBar.minimized.connect(mainWindow.showMinimized)
        titleBar.maximized.connect(self.switchWindow)
        titleBar.closed.connect(self.actionExit)

    def settingMenuActionConnect(self):
        for name, action in views['MainWindow'].settingsMenu.qactions.items():
                if hasattr(self, 'action%s' % name):
                    action.triggered.connect(
                        getattr(self, 'action%s' % name)
                    )
                else:
                    action.triggered.connect(
                        getattr(self, 'actionNotImplement')
                    )

    def createControllers(self):
        pass

    def switchWindow(self, flag):
        mainWindow = views['MainWindow']
        if flag:
            mainWindow.showMaximized()
        else:
            mainWindow.showNormal()

        mainWindow.setskin()

    def actionSuspension(self):
        sw = views['MainWindow'].suspensionWidget
        sw.setVisible(not sw.isVisible())
        if sw.isVisible():
            self.sender().setText('Hide suspension window')
        else:
            self.sender().setText('Show suspension window')

    def actionObjectView(self):
        from qframer import FGlobalSearchWidget
        if hasattr(self, 'searchBar'):
            self.searchBar.hide()
            self.searchBar.deleteLater()
        self.searchBar = FGlobalSearchWidget(views['MainWindow'])
        self.searchBar.searchEdit.setPlaceholderText(self.tr("Search object"))
        self.searchBar.animationShow()
        self.searchBar.setFocus()
        self.searchBar.searchEdit.returnPressed.connect(self.browserObj)

    def browserObj(self):
        from objbrowser import browse
        objstr = self.sender().text()

        def getRootObj(objstr):
            if objstr in self.locals:
                return self.locals[objstr]
            elif objstr in self.globals:
                return self.globals[objstr]
            else:
                return None

        if '.' not in objstr:
            obj = getRootObj(objstr)
            if obj:
                browse(obj)
            else:
                print("root obj not found")
        else:
            objlist = objstr.split('.')
            ret = getRootObj(objlist[0])
            if ret:
                try:
                    for attr in objlist[1:]:
                        ret = getattr(ret, attr)
                    browse(ret)
                except Exception as e:
                    print(e)
            else:
                print("root obj not found")

    def actionAbout(self):
        if hasattr(self, 'aboutPage'):
            self.aboutPage.hide()
            self.aboutPage.deleteLater()
        self.aboutPage = AboutPage(views['MainWindow'])
        self.aboutPage.animationShow()

    def actionExit(self):
        # if hasattr(self, 'exitPage'):
        #     self.exitPage.hide()
        #     self.exitPage.deleteLater()
        # self.exitPage = ExitPage(views['MainWindow'])
        # self.exitPage.exited.connect(self.close)
        # self.exitPage.animationShow()
        self.close()

    def actionNotImplement(self):
        logger.info("actionNotImplement")

    def close(self):
        app = QApplication.instance()
        app.closeAllWindows()
        app.quit()
