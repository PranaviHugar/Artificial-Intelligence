tree = { 'A':['B','C'], 'B':['D','E'],'C':['F','G'],'D':[],'E':[],'F':[],'G':[]}

start= input("enter the start node : ")

def dfs_traversal(tree):
    close=[]
    open1=[start]
    while open1 :
        node = open1.pop()
        if node not in close:
            close.append(node)
            neighbour = tree[node]
            for i in neighbour:
                 open1.append(i)
    return close

print("dfs traversal is : ",dfs_traversal(tree))
