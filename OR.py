# -*- coding: utf-8 -*-
"""
Created on Sun Apr 28 23:25:46 2024

@author: prach
"""

import numpy as np
def activation(v):
    if v<=0.5 :
        return 0
    else:
        return 1

def percepton(x,w,b):
    r=np.dot(x,w)+b
    return activation(r)

def orgate(x):
    w=np.array([1,1])
    b=0.5
    return percepton(x, w, b)
example1=np.array([0,0])
example2=np.array([0,1])
example3=np.array([1,0])
example4=np.array([1,1])

print("OR(0,0):",orgate(example1))
print("OR(0,1):",orgate(example2))
print("OR(1,0):",orgate(example3))
print("OR(1,1):",orgate(example4))

