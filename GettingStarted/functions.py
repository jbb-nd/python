# -*- coding: utf-8 -*-
"""
Created on Tue May 26 08:43:25 2020

@author: jaybr
"""

def printme(str):
    print(str)
    return

def mymax(a):
    m = 0
    for i in a:
        if i > m:
            m = i
    return m

mylist = ['a', 'b', 'c']

def enumerator(x, n):
    for i, item in enumerate(x, n):
        print(i, item)

