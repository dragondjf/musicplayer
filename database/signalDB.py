# -*- coding: utf-8 -*-


from PyQt5.QtCore import *


class SignalDB(QObject):

    su_logsin = Signal(dict)

    uu_initAdd = Signal(dict)
    uu_initAddBatch = Signal(list)
    uu_initEdit = Signal(dict)

    def __init__(self):
        super(SignalDB, self).__init__()

signal_DB = SignalDB()
