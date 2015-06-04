from __future__ import print_function
"""
Created on Wed Apr 22 16:02:53 2015

Basic integrate-and-fire neuron
TC

Experiment to simulate noise in signal
at varying amplitudes to show effect on
information

translated to Python by tc 2015
"""

import numpy as np
import matplotlib.pyplot as plt


# input current
I = 1  # nA

# capacitance and leak resistance
C = 1  # nF
R = 40  # M ohms

# I & F implementation dV/dt = - V/RC + I/C
# Using h = 1 ms step size, Euler method

V = 0
tstop = 20000
abs_ref = 5  # absolute refractory period
ref = 0  # absolute refractory period counter
V_trace = []  # voltage trace for plotting
V_th = 10  # spike threshold
spiketimes = []  # list of spike times

# input current
noiseamp = 5  # amplitude of added noise
I += noiseamp * np.random.normal(0, 1, (tstop,))  # nA; Gaussian noise

for t in range(tstop):

    if not ref:
        V = V - (V / (R * C)) + (I[t] / C)
    else:
        ref -= 1
        V = 0.2 * V_th  # reset voltage

    if V > V_th:
        V = 50  # emit spike
        spiketimes.append(t)  # append spike time to spiketimes
        ref = abs_ref  # set refractory counter

    V_trace += [V]


diff = np.diff(spiketimes)  # create array of interspike intervals
nobins = len(np.unique(diff))  # set number of bins to unique intervals

plt.hist(diff, bins=nobins)
plt.show()

plt.plot(V_trace)
plt.show()
