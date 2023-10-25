# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 22:47:30 2020

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

# import excel and csv files from sakai, zybook, and gradescope
sk = pd.read_csv('sakai.csv')
zy = pd.read_csv('zybook.csv')
gs = pd.read_csv('gradescope.csv')
gs.fillna(0)

# get the Student ID and Student Name columns from sakai
sk_for_merge = sk.iloc[:, 0:2]


# process zybook
# extract Student ID from email and fix special cases
zy['Primary email'] = zy['Primary email'].str.replace('@nd.edu','')
zy['Primary email'] = zy['Primary email'].str.replace('spencerwells@gmail.com', 'swells3')
zy = zy.rename(columns={'Primary email':'Student ID'})

# get the total participation, rename column, and round
zy = zy.rename(columns={'Participation total (256)':'H2 zyBook [100]'})
zy['H2 zyBook [100]'] = zy['H2 zyBook [100]'].round(2)
zy_for_merge = zy[['Student ID', 'H2 zyBook [100]']]

# process gradescope
# rename the Student ID column
gs = gs.rename(columns={'SID':'Student ID'})

# get the counts of the self-tests completed
st = gs[['Self-Test Intro FSM',
             'Self-Test FSM Preferred Implementation',
             'Self-Test RTL with Tables',
             'Self-Test RTL Tables to Verilog',
             'Self-Test Observations',
             'Self-Test: Memory, MaxFinder, and albaCore HLSM',
             'Self-Test albaCore Controller',
             'Self-Test albaCore Processor'
             ]]
gs['Self Test [8]'] = st.count(axis=1)

# rename the columns for HW3, HW4A, and HW4B
gs = gs.rename(columns={'Homework 3:  Finite State Machines':'HW3 [70]'})
gs = gs.rename(columns={'Homework 4A: HLSM Tables':'HW4A [40]'})
gs = gs.rename(columns={'Homework 4B: HLSM Verilog':'HW4B [40]'})
gs = gs.rename(columns={'Final Exam':'Final Exam [31]'})
# calculate proper scores for HW3 and HW4
# prepare DataFrame for merge
gs_for_merge = gs[['Student ID', 
                   'Self Test [8]',
                   'HW3 [70]', 
                   'HW4A [40]',
                   'HW4B [40]',
                   'Final Exam [31]']]


# merge DataFrames
final_merged = sk_for_merge.merge(
    zy_for_merge, how='left', on='Student ID').merge(
        gs_for_merge, how='left', on='Student ID')
        
final_merged = final_merged.set_index('Student ID')

final_merged.to_csv('sakai_upload.csv')

"""
gs3 = gs.iloc[:, [2,5]]
gs3 = gs3.rename(columns={'SID':'Student ID'})

merged = pd.merge(sk3, gs3, how='left', on='Student ID')
"""



