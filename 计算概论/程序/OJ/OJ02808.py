# -*- coding: utf-8 -*-
"""
Created on Sun Oct 15 17:28:47 2023

@author: Lenovo
"""

tree,n=map(int,input().split())
line=[]
for i in range(n): 
    line.append([int(i) for i in input().split()])
road=[1]*(tree+1)
for i in range(n):
    for j in range(line[i][0]-1,line[i][1]):
        road[j]=0
print(sum(road))