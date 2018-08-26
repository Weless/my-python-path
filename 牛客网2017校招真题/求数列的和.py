#!usr/bin/env python
# -*- coding:utf-8 -*-
import math

while True:
    try:
        n,m = list(map(int,input().split()))
        s = 0.0
        for i in range(m):
            s += math.sqrt(n**2)
            n = math.sqrt(n)
        print('%.2f' %s)
    except EOFError:
        break

