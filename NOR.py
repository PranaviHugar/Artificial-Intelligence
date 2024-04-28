# -*- coding: utf-8 -*-
"""
Created on Sun Apr 28 23:27:02 2024

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

def norgate(x):
    w=np.array([1,1])
    b=0.5
    return percepton(x, w, b)
example1=np.array([0,0])
example2=np.array([0,1])
example3=np.array([1,0])
example4=np.array([1,1])

print("NOR(0,0):",norgate(example1))
print("NOR(0,1):",norgate(example2))
print("NOR(1,0):",norgate(example3))
print("NOR(1,1):",norgate(example4))

