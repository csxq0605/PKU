# -*- coding: utf-8 -*-
"""
Created on Tue Dec 19 17:12:59 2023

@author: Lenovo
"""

import copy,sys
sys.setrecursionlimit(1<<30)

def dfs(martix,step):
    if step==p:
        result.append(max(max(martix[i]) for i in range(m)))
        return
    for i in range(4):
        dfs(move(martix,i),step+1)
        
def move(martix,dir):
    new_martix=copy.deepcopy(martix)
    if dir==0:
        for i in range(m):
            new_martix[i]=change(martix[i])
    elif dir==1:
        for i in range(m):
            new_martix[i]=change(martix[i][::-1])[::-1]
    elif dir==2:
        for i in range(n):
            changeline=change([martix[j][i] for j in range(m)])
            for j in range(m):
                new_martix[j][i]=changeline[j]
    else:
        for i in range(n):
            changeline=change([martix[j][i] for j in range(m-1,-1,-1)])[::-1]
            for j in range(m):
                new_martix[j][i]=changeline[j]
    return new_martix            

def change(row):
    line=row.copy()
    l=len(line)
    for i in range(l-1,-1,-1):
        if line[i]==0:
            continue
        for j in range(i-1,-1,-1):
            if line[i]==line[j]:
                line[i],line[j]=2*line[i],0
                break
            elif line[j]==0:
                continue
            else:
                break
    newline=[0]*l
    cnt=l-1
    for i in range(l-1,-1,-1):
        if line[i]!=0:
            newline[cnt]=line[i]
            cnt-=1
    return newline
    
m,n,p=map(int,input().split())
martix=[list(map(int,input().split()))for i in range(m)]
result=[]
dfs(martix,0)
print(max(result))