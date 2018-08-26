#!usr/bin/env python
# -*- coding:utf-8 -*-

n = int(input().strip())

for i in range(n):
    student = list(map(int,input().strip().split()))

k,d = list(map(int,input().strip().split()))

_max = 0
count = 0
for stu in student:

