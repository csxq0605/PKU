# -*- coding: utf-8 -*-
"""
Created on Fri Dec  1 18:26:05 2023

@author: Lenovo
"""

import heapq
def bfs(tree):
    queue=[]
    heapq.heappush(queue,[0,1])
    while True:
        step,position=map(int,heapq.heappop(queue))
        l,r,dir=tree[position][1],tree[position][2],tree[position][3]
        if l==0 and r==0:
            return step
        if l!=0:    
            heapq.heappush(queue,[step+(dir!="L"),l])
        if r!=0:
            heapq.heappush(queue,[step+(dir!="R"),r])            

for _ in range(int(input())):
    n=int(input())
    line=[0]+list(input())
    tree=[[0,0,0,0] for i in range(n+1)]
    for i in range(1,n+1):
        l,r=map(int,input().split())
        tree[i][1],tree[i][2],tree[i][3]=l,r,line[i]
        tree[l][0]=tree[r][0]=i
    print(bfs(tree))