#!usr/bin/env python
# -*- coding:utf-8 -*-

while True:
    try:
        line = input()
        line = line.replace(' ','')
        if len(line) <= 6:
            print(line)
        elif len(line) <= 14:
            print(line[:6] +' '+line[6:len(line)])
        else:
            print(line[:6] + ' ' + line[6:14] + ' '+ line[14:len(line)])
    except EOFError:
        break