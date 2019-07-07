# -*- coding: utf-8 -*-
"""
Created on Sat Jul  6 11:06:45 2019

@author: Jay Brockman
"""
from numpy import *
from matplotlib.pyplot import *

sw = 150.0
h0 = 100.0
w0 = 150.0
w3 = 500.0
a = h0/w0
r = d3/d0
w1 = w0 * r**(1/3)
w2 = w0 * r**(2/3)
L1 = sqrt(sw**2 + (w1-w0)**2/4)
L2 = sqrt(sw**2 + (w2-w1)**2/4)
L3 = sqrt(sw**2 + (w3-w2)**2/4)
h1 = a*w1
h2 = a*w2
h3 = a*w3
sh1 = sqrt(L1**2 - (h1-h0)**2/4)
sh2 = sqrt(L2**2 - (h2-h1)**2/4)
sh3 = sqrt(L3**2 - (h3-h2)**2/4)

print("w:", w0, w1, w2, w3)
print("h:", h0, h1, h2, h3)
print("L:", L1, L2, L3)
print("sh:", sh1, sh2, sh3)
print("board size (mm) = ", 22*25.4, " x ", 28*25.4)
print("top dimensions (in)  = ", 3*sw/25.4, " x ", w3/25.4)
print("side dimensions (in) = ", (sh1+sh2+sh3)/25.4, " x ", h3/25.4)
# plot(array([d0, d1, d2, d3]))