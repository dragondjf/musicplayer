#!/usr/bin/python
# -*- coding: utf-8 -*-


from gui.dwidgets import DMenu


class ClassifyMenu(DMenu):

    """docstring for ClassifyMenu"""

    def __init__(self, parent=None):
        super(ClassifyMenu, self).__init__(parent)
        self.parent = parent
        self.menuItems = [
            {
                'name': self.tr('按歌手'),
                'icon': u'',
                'shortcut': u'',
                'trigger': 'Artist',
            },
            {
                'name': self.tr('按专辑'),
                'icon': u'',
                'shortcut': u'',
                'trigger': 'Album',
            },
            {
                'name': self.tr('按歌曲'),
                'icon': u'',
                'shortcut': u'',
                'trigger': 'Song',
            },
            {
                'name': self.tr('按文件夹'),
                'icon': u'',
                'shortcut': u'',
                'trigger': 'Folder',
            },
        ]
        self.creatMenus(self.menuItems)
