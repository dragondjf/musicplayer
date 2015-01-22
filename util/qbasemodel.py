#!/usr/bin/python
# -*- coding: utf-8 -*-
from PySide import QtCore


class FieldExpection(Exception):
    pass


class ValidForMatExpection(Exception):
    pass


class SetJsonExpection(Exception):
    pass


class SetJsonKeyExpection(Exception):
    pass


class ModelMetaclass(type):

    def __new__(cls, clsname, clsbases, clsdict):
        if 'Fields' in clsdict:
            Fields = clsdict['Fields']
        else:
            Fields = ()

        formatFields = []

        for field in Fields:
            if len(field) < 2:
                raise FieldExpection("Each Field length must be large than 1")
            elif len(field) == 2:
                newfield = (field[0], field[1], field[1]())
            elif len(field) == 3:
                newfield = (field[0], field[1], field[2])
            else:
                raise FieldExpection(
                    "Each Field length must be smaller than 4")
            formatFields.append(newfield)

        Fields = formatFields

        class Object(QtCore.QObject):

            def __init__(self, *args, **kwargs):
                super(Object, self).__init__()
                for key, Type, default in Fields:
                    self.__dict__['_' + key] = kwargs.get(key, default)

                self.valid_message = {}

                self.setJsoning = False

            def __repr__(self):
                values = ('%s=%r' % (key, self.__dict__['_' + key])
                          for key, value, default in Fields)
                return '<%s (%s)>' % (clsname, ', '.join(values))

            def setJson(self, obj):
                self.setJsoning = True
                self.valid_message = {}
                if isinstance(obj, dict):
                    for key, value, default in Fields:
                        if key in obj:
                            setattr(self, key, obj[key])
                    self.setJsoning = False
                    return self.valid_message
                else:
                    self.setJsoning = False
                    raise SetJsonExpection("obj's type must be dict")

            def getJson(self):
                ret = {}
                for key, value, default in Fields:
                    ret[key] = self.__dict__['_' + key]
                return ret

            for key, Type, default in Fields:
                nfy = locals()[key + "_changed"] = QtCore.Signal(Type)

                def _get(key):
                    def f(self):
                        return self.__dict__['_' + key]
                    return f

                def _set(key):
                    def f(self, value):
                        if not self.setJsoning:
                            self.valid_message = {}
                        validmethod = 'valid_' + key
                        if validmethod in clsdict:
                            method = clsdict[validmethod]
                        else:
                            def valid_defaut(self, v):
                                return True
                            locals()['valid_defaut'] = valid_defaut
                            method = valid_defaut
                        valid_return = method(self, value)

                        if valid_return is True:
                            error, validFlag = (
                                "set %s=%s valid ok" % (key, value), True)
                        elif valid_return is False:
                            error, validFlag = (
                                "set %s=%s valid error" % (key, value), False)
                        else:
                            if(len(valid_return) == 2):
                                validFlag, error = valid_return
                                if isinstance(validFlag, bool) and \
                                        isinstance(error, str):
                                    pass
                                else:
                                    error, validFlag = (
                                        "def valid_%s function error." % key,
                                        False)
                                    raise ValidForMatExpection(
                                        "def valid_%s function error." % key)
                            else:
                                error, validFlag = (
                                    "def valid_%s function error." % key,
                                    False)
                                raise ValidForMatExpection(
                                    "def valid_%s function error." % key)

                        if validFlag:
                            self.__dict__['_' + key] = value
                            self.__dict__[key + "_changed"].emit(value)
                        else:
                            self.valid_message[key] = error
                    return f

                set = locals()['_set_' + key] = _set(key)
                get = locals()['_get_' + key] = _get(key)

                locals()[key] = QtCore.Property(Type, get, set, notify=nfy)

        return Object


class Object_Dict(dict):

    '''
        Makes a dictionary behave like an object.
    '''

    def __init__(self, *args, **kw):
        dict.__init__(self, *args, **kw)
        self.__dict__ = self


class Car(object):

    __metaclass__ = ModelMetaclass

    Fields = (
        ('model', str, "123"),
        ('brand', str, "456"),
        ('year', int),
        ('inStock', bool),
        ('d', dict, {'a': 1111})
    )

    def valid_model(self, value):
        return True

    def valid_brand(self, value):
        return False


def slot(n):
    print("get data from signal:", n)


def test(func):
    import functools

    @functools.wraps(func)
    def wrapper(*args, **kwagrs):
        print("============ %s start =============" % func.func_name)
        func(*args, **kwagrs)
        print("============ %s end   =============\n" % func.func_name)
    return wrapper


@test
def test_Json():
    car = Car(model="1111")
    obj = {
        'model': "8888",
        'brand': "+++"
    }
    car.setJson(obj)
    print(car.valid_message)
    print(car.getJson())
    print(car)


@test
def test_attr():
    car = Car(model="1111")
    car.model = "333"
    print(car.valid_message)
    print(car)


@test
def test_slot():
    car = Car(model="1111")
    car.model_changed.connect(slot)
    car.model = "111"
    print(car)

if __name__ == '__main__':
    test_Json()
    test_attr()
    test_slot()
