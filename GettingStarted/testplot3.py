# -*- coding: utf-8 -*-
"""
Created on Sat Jul  6 10:59:07 2019

@author: Jay Brockman
"""

from numpy import *
from matplotlib.pyplot import *

s = array([0, 1, 2, 3, 4, 5])
x = 2**s
y2 = 2*x
y3 = 3*x
hold(True) # keep adding plots to axes
plot(x, y2, '-o')
plot(x, y3, '-o')
xscale('log', basex=2)
text(x[5], y2[5], '2*x')
text(x[5], y3[5], '3*x')
legend([2, 3])
xlabel('x-axis')
ylabel('y-axis')
title('Example Plot')
savefig('myplot.png') # also pdf, eps, ps, and svg formats
show() # opens a window and shows plot
hold(False)