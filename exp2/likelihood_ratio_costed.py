"""
Created on Wed Apr 22 15:21:11 2015

@author: tc

Code to compute costed threshold.
"""

from __future__ import division
import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
from scipy import stats
from compute_costed_threshold import compute_costed_threshold

meanS1 = 5
sdS1 = 0.5
meanS2 = 7
sdS2 = 1
weight = 2.0

thresh_test = [5.830, 5.667, 5.978, 2.69]

opt_thresh = compute_costed_threshold(weight, thresh_test, meanS1, sdS1, meanS2, sdS2)

print "Optimum Costed Threshold = %s" % opt_thresh

rv = stats.norm(loc = meanS1, scale = sdS1)
rv1 = stats.norm(loc = meanS2, scale = sdS2)

x = np.arange(0, 10, .1)
plt.plot(x, rv.pdf(x), x, rv1.pdf(x))
plt.axvline(x=opt_thresh, ymin=0, ymax=1, linewidth=1, color = 'r')
plt.plot(opt_thresh, 0.3, 'x', color='purple')
plt.xlabel('Firing Rate')
plt.ylabel('Probability')
plt.title('Threshold Test')
plt.show()