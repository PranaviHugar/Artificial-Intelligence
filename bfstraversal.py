# -*- coding: utf-8 -*-
"""
Created on Fri Feb  9 18:04:38 2024

@author: prach
"""

tree = {'A':['B','C'],'B':['D'],'C':['E'],'D':['F'],'E':['F'],'F':[]}
start=input("Enter the start state:")
def bfs_traversal(tree):
    close=[]
    open=[start]
    while open :
        node= open.pop(0)
        if node not in close :
            close.append(node)
            neighbor=tree[node]
            for i in neighbor :
                open.append(i)
    return close
print("BFS traversal is ",bfs_traversal(tree))
