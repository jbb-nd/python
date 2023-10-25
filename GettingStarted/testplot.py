# -*- coding: utf-8 -*-
"""
Created on Sat Jul  6 10:43:18 2019

@author: Jay Brockman
"""

import numpy as np
import matplotlib.pyplot as plt
s = np.array([0, 1, 2, 3, 4, 5])
x = 2**s
y2 = 2*x
y3 = 3*x
#plt.hold(True) # keep adding plots to axes
plt.plot(x, y2, '-o')
plt.plot(x, y3, '-o')
plt.xscale('log', basex=2)
plt.text(x[5], y2[5], '2*x')
plt.text(x[5], y3[5], '3*x')
plt.legend([2, 3])
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.title('Example Plot')
plt.savefig('myplot.png') # also pdf, eps, ps, and svg formats
plt.show() # opens a window and shows plot
#plt.hold(False)