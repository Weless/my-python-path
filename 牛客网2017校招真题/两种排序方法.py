#!usr/bin/env python
# -*- coding:utf-8 -*-

n = int(input().strip())

rem = []

for i in range(n):
    rem.append(input().strip())

tmp = rem[::]
tmp1 = sorted(tmp)
tmp2 = sorted(tmp,key=len)

if rem == tmp1 and rem == tmp2:
    print('both')
elif rem == tmp1:
    print('lexicographically')
elif rem == tmp2:
    print('lengths')
else:
    print('None')