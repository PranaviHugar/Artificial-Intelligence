# -*- coding: utf-8 -*-
"""
Created on Tue Feb 13 11:30:30 2024

@author: Student
"""

tree= {'A':['B','C'],'B':['D','E','F'],'C':['G','H'],'D':[],'E':[],'F':[],'G':[],'H':[]}
start=input("Enter start node:")
goal=input("Enter goal node:")
print("Path:")
close=[]
def dfsg(tree,start):
    if start not in close:
        print(start)
        close.append(start)
        neighbor=tree[start]
        for i in neighbor:
            if goal in close:
                break
            else:
                dfsg(tree,i)
dfsg(tree,start)