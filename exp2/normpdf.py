"""
Created on Wed Apr 22 15:21:11 2015

@author: tc

Plot 2 gaussian response curves.
"""

from __future__ import division
import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt

meanAverageS1 = 5
standardDeviationS1 = 0.5
meanAverageS2 = 7
standardDeviationS2 = 1

x = np.linspace(0, 20)
plt.plot(x, mlab.normpdf(x,meanAverageS1, standardDeviationS1))
plt.plot(x, mlab.normpdf(x,meanAverageS2, standardDeviationS2))
plt.show()
