# -*- coding: utf-8 -*-
"""
Created on Thu Nov  9 15:38:47 2023

@author: Lenovo
"""

class Node:
    def __init__(self,Pre):
        self.Pre=Pre
        self.PreSum=0

RootSum=0 
def FindR(x):
    global RootSum
    if x==Tree[x].Pre:
        return x
    else:
        RootSum=(RootSum+Tree[x].PreSum)%3
        return FindR(Tree[x].Pre)

def FindRoot(x):
    global RootSum
    RootSum=0
    Tree[x].Pre=FindR(x)
    Tree[x].PreSum=RootSum 
    return Tree[x].Pre

def XEatY(x,y):
    x=Tree[x].PreSum
    y=Tree[y].PreSum 
    return ((x==0 and y==1)or(x==1 and y==2)or(x==2 and y==0))

N,M=map(int,input().split())
Tie=0
Tree=[Node(_) for _ in range(N+1)]
for _ in range(M):
    D,X,Y=map(int,input().split())
    if X<1 or X>N or Y<1 or Y>N:
        Tie+=1
        continue
    RootX=FindRoot(X)
    RootY=FindRoot(Y)
    if RootX==RootY:
        if D==1:
            if Tree[X].PreSum!=Tree[Y].PreSum:
                Tie+=1
        elif D==2:
            if not XEatY(X,Y):
                Tie+=1
    else:    
        if D==1:
            Tree[RootY].Pre=RootX
            Tree[RootY].PreSum=(Tree[X].PreSum-Tree[Y].PreSum+3)%3
        elif D==2:
            Tree[RootY].Pre=RootX
            Tree[RootY].PreSum=(Tree[X].PreSum+1-Tree[Y].PreSum+3)%3
print(Tie)