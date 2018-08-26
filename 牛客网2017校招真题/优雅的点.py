#!usr/bin/env python
# -*- coding:utf-8 -*-

import math
n = int(input())
count = 0
tag = 0
tmp = math.sqrt(n)
if int(tmp)**2 == n:
    tag =1
for i in range(1,int(tmp)+1):
    for j in range(1,int(tmp)+1):
        if i**2 + j**2 == n:
            # print(i,j)
            count+=1
if tag == 1:
    count = count*4 + 4
else:
    count = count*4
print(count)