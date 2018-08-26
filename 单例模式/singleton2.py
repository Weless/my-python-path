#!usr/bin/env python
# -*- coding:utf-8 -*-

from functools import wraps
def singleton(cls):
    instance = {}
    @wraps(cls)
    def getinstance(*args,**kw):
        if cls not in instance:
            instance[cls] = cls(*args,**kw)
        return instance[cls]
    return getinstance

@singleton
class Myclass(object):
    a = 1

one = Myclass()
two = Myclass()
print(one)
print(two)