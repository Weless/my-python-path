#!usr/bin/env python
# -*- coding:utf-8 -*-

m,n = list(map(int,input().split()))

result = []
for i in range(m,n+1):
    if (i//100)**3 + (i//10%10)**3 + (i%10)**3 == i:
        result.append(str(i))
if result:
    print(' '.join(result))
else:
    print('no')



