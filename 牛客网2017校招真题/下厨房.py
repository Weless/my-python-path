#!usr/bin/env python
# -*- coding:utf-8 -*-


food = set()
while True:
    try:
        s = input().strip()
        if not s:
            break
        tmp = s.split()
        for i in tmp:
            food.add(i)
    except EOFError:
        break
print(len(food))