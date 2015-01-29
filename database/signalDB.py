# -*- coding: utf-8 -*-


from PyQt5.QtCore import *


class SignalDB(QObject):

    closed = Signal()
    backgroundimageChanged = Signal(unicode)
    modeChanged = Signal(str)

    songInfo = Signal(dict) 

    def __init__(self):
        super(SignalDB, self).__init__()

signal_DB = SignalDB()
