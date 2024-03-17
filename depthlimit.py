# -*- coding: utf-8 -*-
"""
Created on Tue Feb 13 12:45:41 2024

@author: Student
"""

tree={'A':['B','C'],'B':['D','E','F'],'C':['G','H'],'D':[],'E':[],'F':[],'G':[],'H':[]}
start=input("Enter start node:")
goal=input("Enter goal node:")
maxd=int(input("Enter max depth limit:"))
path=[]
level=0
def depthlimit(start,goal,tree,level,path,maxd):
    print("Current level is:",level)
    path.append(start)
    if start==goal:
        print("Goal found")
        return path
    if level==maxd:
        return False
    print("Expanding the node ",start)
    neighbor=tree[start]
    for i in neighbor:
        if depthlimit(i, goal, tree, level+1 , path, maxd):
            return path
        path.pop()
    return False
if depthlimit(start, goal, tree, level, path, maxd):
    print("Goal is present")
    print(path)
else:
    print("Goal is not  found")      
