from __future__ import print_function
"""
Created on Wed Apr 22 16:02:53 2015

Basic integrate-and-fire neuron
TC

Experiment to find minimum current
which will induce spike

translated to Python by tc 2015
"""

import numpy as np
import matplotlib.pyplot as plt


# input current
I = 1  # nA
I = 0.252  # nA - experiment to find minimum current
print('I = %s nA' % round(I, 2))
# capacitance and leak resistance
C = 1  # nF
R = 40  # M ohms

# I & F implementation dV/dt = - V/RC + I/C
# Using h = 1 ms step size, Euler method

V = 0
tstop = 200
abs_ref = 5  # absolute refractory period
ref = 0  # absolute refractory period counter
V_trace = []  # voltage trace for plotting
V_th = 10  # spike threshold
Vmax = 0  # max voltage reached

for t in range(tstop):

    if not ref:
        V = V - (V / (R * C)) + (I / C)
    else:
        ref -= 1
        V = 0.2 * V_th  # reset voltage

    if V > V_th:
        Vmax = V
        V = 50  # emit spike
        Spike = 1
        print('Spike generated')
        ref = abs_ref  # set refractory counter

    V_trace += [V]

print('V threshold = 10')
print('Vmax = %s' % max(V_trace))
plt.plot(V_trace)
plt.show()