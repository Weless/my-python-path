class Root(object):
    def __init__(self):
        print('this is Root')

class B(Root):
    def __init__(self):
        print('enter B')
        super(B, self).__init__() # C
        print('leave B')

class C(Root):
    def __init__(self):
        print('enter C')
        super(C, self).__init__() # Root
        print('leave C')

class D(B, C):
    pass

d = D()
print(D.__mro__)

# 输出结果：
# enter B
# enter C
# this is Root
# leave C
# leave B
# (<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.Root'>, <class 'object'>)

# 实际上super调用了mro表的下一个类
# # def super(cls, inst):
#     mro = inst.__class__.mro()
#     return mro[mro.index(cls) + 1]