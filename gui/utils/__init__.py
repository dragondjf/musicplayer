#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import functools

views = {}


def collectView(func):

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        self = args[0]
        if hasattr(self, 'viewID'):
            views.update({self.viewID: self})
        func(*args, **kwargs)
    return wrapper


def setSkinForApp(qssfile):
    from PyQt5.QtWidgets import QApplication
    if os.path.exists(qssfile):
        fd = open(qssfile, "r")
        style = fd.read()
        fd.close()
        QApplication.instance().setStyleSheet(style)
    else:
        QApplication.instance().setStyleSheet("")
