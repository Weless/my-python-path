#!usr/bin/env python
# -*- coding:utf-8 -*-


def check_subsequence(s):
    import re
    if re.findall(r'\w*(\w)\w*(\w)\w*\1\w*\2\w*',s):
        return True
    else:
        return False


def check_continuity(s):
    i = 0
    while i < len(s)-1:
        part = s[i:i+2]
        if len(set(part)) == 1:
            return True
        i+=1
    return False

s = input()
if s == s.upper() and not check_subsequence(s) and not check_continuity(s):
    print('Likes')
else:
    print('Dislikes')