# -*- coding: utf-8 -*-
"""
Created on Fri Feb  9 18:05:43 2024

@author: prach
"""

tree={'A':['B','C'],'B':['D','E'],'C':['F','G'],'D':[],'E':[],'F':[],'G':[]}
start=input("Enter start node:")
goal=input("Enter goal node:")
def bfs_goals(tree):
    close=[]
    open=[start]
    if start==goal:
        print("start itself is goal")
    else:
        close.append(start)
        while open:
            node=open.pop(0)
            neighbor=tree[node]
            for i in neighbor:
                open.append(i)
                close.append(i)
                if i==goal:
                    return close
        print("goal not found")
print("Path:",bfs_goals(tree))
