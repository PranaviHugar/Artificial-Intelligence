# -*- coding: utf-8 -*-
"""
Created on Sun Apr 28 23:24:15 2024

@author: prach
"""

import numpy as np
def activation(v):
    if v<=0.5 :
        return 1
    else:
        return 0

def percepton(x,w,b):
    r=np.dot(x,w)+b
    return activation(r)

def notgate(x):
    w=1
    b=0.5
    return percepton(x, w, b)
print("NOT(0):",notgate(0))

