# -*- coding: utf-8 -*-
"""
Created on Tue Feb 13 11:55:38 2024

@author: Student
"""

tree={'A':['B','C'],'B':['D','E','F'],'C':['G','H'],'D':[],'E':[],'F':[],'G':[],'H':[]}
start=input("Enter start node:")
goal=input("Enter goal node:")
def dfsgr(tree,start):
    close=[]
    open=[[start]]
    if start==goal:
        print(start)
    while open:
        path=open.pop() #[A]
        node=path[-1]
        if node not in close:
            close.append(node)
        neighbor=tree[node]
        for i in neighbor:
            newpath=list(path) #[A]
            newpath.append(i) #[A,B]
            open.append(newpath)
            if i==goal:
                return newpath
print("Path:",dfsgr(tree,start))