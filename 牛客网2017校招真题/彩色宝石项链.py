#!usr/bin/env python
# -*- coding:utf-8 -*-

import re

line = input()

line2 = line * 2

result = re.findall(r'.*?[ABCDE](.*?)[ABCDE](.*?)[ABCDE]()',line2)

l = len(line) - min(list(map(len,result)))
print(l)

