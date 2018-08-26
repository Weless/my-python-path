#!usr/bin/env python
# -*- coding:utf-8 -*-

# metaclass
#元类（metaclass）可以控制类的创建过程，它主要做三件事：

# 拦截类的创建
# 修改类的定义
# 返回修改后的类
class Singleton(type):
    _instance = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instance:
            cls._instance[cls] = super(Singleton, cls).__call__(*args,**kwargs)
        return cls._instance[cls]
class Myclass(metaclass = Singleton):
    pass

one = Myclass()
two = Myclass()
print(one)
print(two)