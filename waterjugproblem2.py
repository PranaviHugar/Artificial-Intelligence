# -*- coding: utf-8 -*-
"""
Created on Thu Apr 18 11:22:25 2024

@author: student
"""

a=int(input("Enter the capacity of a: "))
b=int(input("Enter the capacity of b: "))
c=int(input("Enter the capacity of c: "))

af=int(input("Enter the final capacity of a: "))
bf=int(input("Enter the final capacity of b: "))

initial_state=(8,0,0)
visited={}
path=[]
def all_states(state):
    x=state[0]
    y=state[1]
    z=state[2]
    if(x==af and y==bf):
        path.append(state)
        return True
    if((x,y,z)in visited):
        return False
    visited[(x,y,z)]=1
    
    if(x>0):
        if(x+y<=b):
            if all_states((0,x+y,z)):
                path.append(state)
                return True
        else:
            if all_states((x-(b-y),b,z)):
                path.append(state)
                return True
        if(x+z<=c):
            if all_states((0,y,x+z)):
                path.append(state)
                return True
        else:
            if all_states((x-(c-z),y,c)):
                path.append(state)
                return True
    
    if(y>0):
        if(x+y<=a):
            if all_states((x+y,0,z)):
                path.append(state)
                return True
        else:
            if all_states((a,y-(a-x),z)):
                path.append(state)
                return True
        if(y+z<=c):
            if all_states((x,0,y+z)):
                path.append(state)
                return True
        else:
            if all_states((x,y-(c-z),c)):
                path.append(state)
                return True
                
                
    if(z>0):
        if(x+z<=a):
            if all_states((x+z,y,0)):
                path.append(state)
                return True
        else:
            if all_states((a,y,z-(a-x))):
                path.append(state)
                return True
        if(z+y<=b):
            if all_states((x,y+z,0)):
                path.append(state)
                return True
        else:
            if all_states((x,b,z-(c-z))):
                path.append(state)
                return True             
    return False
all_states(initial_state)
path.reverse()
for i in path:
    print(i)
        
    
    