"""
Created on Wed May 22 15:21:11 2015

@author: tc

Code to compute the costed threshold of two spike responses to
two independent stimuli.
"""

from __future__ import division
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab


def compute_costed_threshold(weight, thresholds, meanS1, sdS1, meanS2, sdS2):
    """Compute the costed threshold of two spike responses to
two independent stimuli.
    
    Args:
        weight: costed threshold multiplier 
        thresholds: values to test for suitability
        meanS1: mean of firing rate distribution triggered by stimulus 1
        sdS1: standard deviation of firing rate distribution triggered by stimulus 1
        meanS2: mean of firing rate distribution triggered by stimulus 2
        sdS1: standard deviation of firing rate distribution triggered by stimulus 1
        
    Returns:
        neuronal firing tate as which to set optimum costed threshold"""
    
    opt_thresh = 0.0
    
    for threshold in thresholds:
        Ps1 = mlab.normpdf(threshold, meanS1, sdS1)
        Ps2 = mlab.normpdf(threshold, meanS2, sdS2)

        ratio_raw = Ps1 / Ps2
        ratio = round(ratio_raw, 2)

        print "Ps1 = %s, Ps2 = %s. Threshold = %s. Ratio raw = %s Weight = %s\n" % (Ps1, Ps2, threshold, ratio_raw, ratio)
        if ratio == weight:
            opt_thresh = threshold

    return opt_thresh