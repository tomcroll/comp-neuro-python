from __future__ import print_function
"""
Created on Wed Apr 22 16:02:53 2015

Basic integrate-and-fire neuron
TC

Experiment to find max firing rate of neuron

translated to Python by tc 2015
"""

import numpy as np
import matplotlib.pyplot as plt


# input current
I = 20  # nA
# capacitance and leak resistance
C = 1  # nF
R = 40  # M ohms

# I & F implementation dV/dt = - V/RC + I/C
# Using h = 1 ms step size, Euler method

V = 0
tstop = 1000
abs_ref = 5  # absolute refractory period
ref = 0  # absolute refractory period counter
V_trace = []  # voltage trace for plotting
V_th = 10  # spike threshold
Vmax = 0  # initiate maximum voltage reached
Spike_count = 0  # initiate spike count

for t in range(tstop):

    if not ref:
        V = V - (V / (R * C)) + (I / C)
    else:
        ref -= 1
        V = 0.2 * V_th  # reset voltage

    if V > Vmax:
        Vmax = V

    if V > V_th:
        V = 50  # emit spike
        Spike_count += 1
        ref = abs_ref  # set refractory counter

    V_trace += [V]

print('V threshold = 10')
print('Vmax = %s' % max(V_trace))
print('Spike count = %s' % Spike_count)
plt.plot(V_trace)
plt.show()
