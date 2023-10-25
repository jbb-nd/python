# -*- coding: utf-8 -*-
"""
Created on Sun Apr 26 17:18:03 2020

@author: jaybr
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#pd.set_option('max_columns', 50)

grades = pd.read_excel('grades.xlsx')
grades['hw3_avg'] = grades['hw1']/grades['hw1 max']


