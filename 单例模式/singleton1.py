#!usr/bin/env python
# -*- coding:utf-8 -*-

class Singleton(object):
    __instance = None
    def __new__(cls,*args,**kwargs):
        if cls.__instance is None:
            cls.__instance = super(Singleton, cls).__new__(cls,*args,**kwargs)
        return cls.__instance

class Myclass(Singleton):
    a = 1

one = Myclass()
two = Myclass()
print(one)
print(two)