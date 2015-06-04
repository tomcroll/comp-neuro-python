#%matplotlib inline
import numpy as np
import pandas as pd
import statsmodels.api as sm
import sympy as sp
#import pymc
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
from mpl_toolkits.mplot3d import Axes3D
from scipy import stats
from scipy.special import gamma

from sympy.interactive import printing
printing.init_printing()


# Simulate data
np.random.seed(123)

nobs = 100
theta = 0.3
Y = np.random.binomial(1, theta, nobs)

# Plot the data
fig = plt.figure(figsize=(7, 3))
gs = gridspec.GridSpec(1, 2, width_ratios=[5, 1])
ax1 = fig.add_subplot(gs[0])
ax2 = fig.add_subplot(gs[1])

ax1.plot(range(nobs), Y, 'x')
ax2.hist(-Y, bins=2)

ax1.yaxis.set(ticks=(0, 1), ticklabels=('Failure', 'Success'))
ax2.xaxis.set(ticks=(-1, 0), ticklabels=('Success', 'Failure'))

ax1.set(title=r'Bernoulli Trial Outcomes $(\theta=0.3)$',
        xlabel='Trial', ylim=(-0.2, 1.2))
ax2.set(ylabel='Frequency')

fig.tight_layout()
fig.show()

t, T, s = sp.symbols('theta, T, s')

# Create the functions symbolically
likelihood = (t**s) * (1 - t)**(T - s)
loglike = s * sp.log(t) + (T - s) * sp.log(1 - t)
score = (s / t) - (T - s) / (1 - t)
hessian = -s / (t**2) - (T - s) / ((1 - t)**2)
information = T / (s * (1 - s))
var = 1 / information

# Convert them to Numpy-callable functions
_likelihood = sp.lambdify((t, T, s), likelihood, modules='numpy')
_loglike = sp.lambdify((t, T, s), loglike, modules='numpy')
_score = sp.lambdify((t, T, s), score, modules='numpy')
_hessian = sp.lambdify((t, T, s), hessian, modules='numpy')
