# -*- coding: utf-8 -*-
"""
Created on Sun Apr 28 23:34:36 2024

@author: prach
"""

import numpy as np
def activation(v):
    if v<=2.5 :
        return 0
    else:
        return 1

def percepton(x,w,b):
    r=np.dot(x,w)+b
    return activation(r)

def andgate(x):
    w=np.array([1,1,1])
    b=0.5
    return percepton(x, w, b)
a=int(input("Enter no. 1:"))
b=int(input("Enter no. 2:"))
c=int(input("Enter no. 3:"))
example=np.array([a,b,c])

print("AND:",andgate(example))

