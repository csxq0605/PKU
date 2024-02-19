# -*- coding: utf-8 -*-
"""
Created on Wed Nov 29 09:16:52 2023

@author: Lenovo
"""

n=int(input())
l=[list(map(int,input().split())) for i in range(n)]
l.sort(key=lambda x:(x[1],x[0]))
ans=1
right=l[0][1]
for i in range(1,n):
    if l[i][0]>right:
        ans+=1
        right=l[i][1]
print(ans)