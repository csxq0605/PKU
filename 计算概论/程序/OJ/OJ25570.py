# -*- coding: utf-8 -*-
"""
Created on Wed Nov 22 23:18:49 2023

@author: Lenovo
"""

n=int(input())
l=[]
for _ in range(n):
    l.append(list(map(int,input().split())))
indexn,indexs,indexw,indexe=0,n-1,0,n
ans=0
for i in range((n+1)//2):
    if indexn!=indexs:
        tmp=sum(l[indexn][indexw:indexe])+sum(l[indexs][indexw:indexe])
        for j in range(indexn+1,indexs):  
            tmp+=l[j][indexw]+l[j][indexe-1]
    else:
        tmp=sum(l[indexn][indexw:indexe])
    ans=max(ans,tmp)
    indexn+=1
    indexs-=1
    indexw+=1
    indexe-=1
print(ans)