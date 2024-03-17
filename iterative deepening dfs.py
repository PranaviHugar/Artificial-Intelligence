# -*- coding: utf-8 -*-
"""
Created on Tue Feb 20 11:30:57 2024

@author: Student
"""

tree={'A':['B','C'],'B':['D','E','F'],'C':['G','H'],'D':['K'],'E':[],'F':[],'G':[],'H':[]}
start=input("Enter start node:")
goal=input("Enter goal node:")

path=[]
level=0


def depthlimit(start,goal,tree,level,path,maxd):
    path.append(start)
    print("Current level is:",level)
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
        path.pop();
    return False

maxid=100

def iterativedfs(start,goal,tree,maxid):
    for i in range(maxid):
        print("Iteration:",i+1)
        path=[]
        if depthlimit(start, goal, tree,level,path,i):
            print("Path to goal node availaible")
            print("Path is ",path)
            return tree
    return False
iterativedfs(start, goal, tree, maxid)