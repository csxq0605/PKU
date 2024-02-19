# -*- coding: utf-8 -*-
"""
Created on Sun Dec 10 00:35:47 2023

@author: Lenovo
"""

n,w=map(int,input().split())
p,q=map(int,input().split())
l=[list(map(int,input().split()))for i in range(n)]
l.sort(key=lambda x:(x[1]))
ans=0
for i in range(n):
    if p+q>=l[i][0] and w>=l[i][1]:
        ans+=1
        w-=l[i][1]
print(ans)