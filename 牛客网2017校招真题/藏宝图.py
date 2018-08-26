#!usr/bin/env python
# -*- coding:utf-8 -*-

s = input().strip()
t = input().strip()

def check_subsequence(s,t):
    if t == '':
        return True
    for i in t:
        if i in s:
            s = s[s.index(i)+1:]
        else:
            return False
    return True
if check_subsequence(s,t):
    print('Yes')
else:
    print('No')


# similiar solution

# 贪心
s1,s2=input(),input()
for i in s1:
    if s2 and i==s2[0]:
        s2=s2[1:]
print("No" if s2 else "Yes")