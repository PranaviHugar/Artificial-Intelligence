# -*- coding: utf-8 -*-
"""
Created on Tue Feb 20 12:18:08 2024

@author: Student
"""
tree={'A':[('B',12),('C',4)],
      'B':[('D',7),('E',3)],'C':[('F',8),('G',2)],
      'E':[('H',0)],'F':[('H',0)],'G':[('H',0)],'D':[],'H':[]}
start=input("Enter start node:")
goal=input("Enter goal node:")
open=[]
close=[]
print("Path is:")
def bestfs(start,goal,tree,open,close):
    if start not in close:
        print(start)
        close.append(start)
        neighbor=tree[start]
        for i in neighbor:
            if i[0] not in open:
                open.append(i)
    open.sort(key=lambda i:i[1])
    if open[0][0]==goal:
        print(open[0][0])
    else:
        node=open[0]
        open.remove(node)
        bestfs(node[0], goal, tree, open, close)
bestfs(start, goal, tree, open, close)


