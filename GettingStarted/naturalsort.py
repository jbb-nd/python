# -*- coding: utf-8 -*-
"""
Created on Wed May 27 12:58:13 2020

@author: jaybr
"""


import re
import os

def atoi(text):
    return int(text) if text.isdigit() else text

def natural_keys(text):
    '''
    alist.sort(key=natural_keys) sorts in human order
    http://nedbatchelder.com/blog/200712/human_sorting.html
    (See Toothy's implementation in the comments)
    '''
    return [ atoi(c) for c in re.split(r'(\d+)', text) ]

# alist=[
#     "something1",
#     "something12",
#     "something17",
#     "something2",
#     "something25",
#     "something29"]
    
alist = os.listdir()

alist.sort(key=natural_keys)
print(alist)
