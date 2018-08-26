#!usr/bin/env python
# -*- coding:utf-8 -*-

line = input()

store = {}

for i in line:
    if i.isalpha() and i not in store:
        store[i] = 1
    elif i.isalpha() and i in store:
        store[i] += 1
        if store[i] == 3:
            print(i)
            break