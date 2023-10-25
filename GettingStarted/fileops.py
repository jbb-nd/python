# -*- coding: utf-8 -*-
"""
Created on Tue May 26 09:12:52 2020

@author: jaybr
"""

import os
import shutil
import re

def atoi(text):
    return int(text) if text.isdigit() else text

def natural_keys(text):
    '''
    alist.sort(key=natural_keys) sorts in human order
    http://nedbatchelder.com/blog/200712/human_sorting.html
    (See Toothy's implementation in the comments)
    '''
    return [ atoi(c) for c in re.split(r'(\d+)', text) ]

# shutil.copy2('functions.py', 'morefunctions.py')
    
flist = os.listdir()
flist.sort(key=natural_keys)

for i, f in flist:
    root, ext = os.path.splitext(f)
    print(root)
