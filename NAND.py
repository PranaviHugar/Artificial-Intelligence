# -*- coding: utf-8 -*-
"""
Created on Sun Apr 28 23:26:14 2024

@author: prach
"""

import numpy as np
def activation(v):
    if v<=1.5 :
        return 1
    else:
        return 0

def percepton(x,w,b):
    r=np.dot(x,w)+b
    return activation(r)

def nandgate(x):
    w=np.array([1,1])
    b=0.5
    return percepton(x, w, b)
example1=np.array([0,0])
example2=np.array([0,1])
example3=np.array([1,0])
example4=np.array([1,1])

print("NAND(0,0):",nandgate(example1))
print("NAND(0,0):",nandgate(example2))
print("NAND(0,0):",nandgate(example3))
print("NAND(0,0):",nandgate(example4))
