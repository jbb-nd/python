# -*- coding: utf-8 -*-
"""
Created on Sun Apr 26 17:18:03 2020

@author: jaybr
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#pd.set_option('max_columns', 50)

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
#pd.set_option('display.max_colwidth', -1)


grades = pd.read_excel('gradescope.xlsx')

"""
thing = grades[['SID', 
                'Self-Test Intro FSM',
                'Self-Test FSM Preferred Implementation'
                ]]
"""


st = grades[['Self-Test Intro FSM',
             'Self-Test FSM Preferred Implementation',
             'Self-Test RTL with Tables',
             'Self-Test RTL Tables to Verilog',
             'Self-Test Observations',
             'Self-Test: Memory, MaxFinder, and albaCore HLSM',
             'Self-Test albaCore Controller'
             ]]

#st.to_excel('selftests.xlsx')

st_count = st.count(axis=1)

st_count_SID = pd.concat([grades['SID'], st_count], axis=1)
