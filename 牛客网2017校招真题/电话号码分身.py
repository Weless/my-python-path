#!usr/bin/env python
# -*- coding:utf-8 -*-


from collections import Counter
n = int(input())

numbers = {
    'ZERO': Counter('ZERO'),
    'ONE': Counter('ONE'),
    'TWO': Counter('TWO'),
    'THREE': Counter('THREE'),
    'FOUR': Counter('FOUR'),
    'FIVE': Counter('FIVE'),
    'SIX': Counter('SIX'),
    'SEVEN': Counter('SEVEN'),
    'EIGHT': Counter('EIGHT'),
    'NINE': Counter('NINE')
}

def deal(alist):
    return ''.join(sorted(alist))


for i in range(n):
    line = input()
    store= []

    counter = Counter(line)
    while 'X' in counter:
        counter = counter - numbers['SIX']
        store.append('8')
    if list(counter.elements()) == []:
        print(deal(store))
        continue
    while 'S' in counter:
        counter = counter - numbers['SEVEN']
        store.append('9')
    if list(counter.elements()) == []:
        print(deal(store))
        continue
    while 'V' in counter:
        counter = counter - numbers['FIVE']
        store.append('7')
    if list(counter.elements()) == []:
        print(deal(store))
        continue
    while 'F' in counter:
        counter = counter - numbers['FOUR']
        store.append('6')
    if list(counter.elements()) == []:
        print(deal(store))
        continue
    while 'Z' in counter:
        counter = counter - numbers['ZERO']
        store.append('2')
    if list(counter.elements()) == []:
        print(deal(store))
        continue
    while 'W' in counter:
        counter = counter - numbers['TWO']
        store.append('4')
    if list(counter.elements()) == []:
        print(deal(store))
        continue
    while 'G' in counter:
        counter = counter - numbers['EIGHT']
        store.append('0')
    if list(counter.elements()) == []:
        print(deal(store))
        continue
    while 'O' in counter:
        counter = counter - numbers['ONE']
        store.append('3')
    if list(counter.elements()) == []:
        print(deal(store))
        continue
    while 'T' in counter:
        counter = counter - numbers['THREE']
        store.append('5')
    if list(counter.elements()) == []:
        print(deal(store))
        continue
    while 'N' in counter:
        counter = counter - numbers['NINE']
        store.append('1')
    if list(counter.elements()) == []:
        print(deal(store))
        continue





