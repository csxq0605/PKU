# -*- coding: utf-8 -*-
"""
Created on Thu Nov  2 15:16:37 2023

@author: Lenovo
"""

l,ans=[],[]
for _ in range(5):
    l.append([int(i) for i in input().split()])
for i in range(5):
    maxn=max(l[i])
    index=l[i].index(maxn)
    minn=min(l[0][index],l[1][index],l[2][index],l[3][index],l[4][index])
    if minn==maxn:
        ans.append(str(i+1)+" "+str(index+1)+" "+str(maxn))
if ans:
    for i in ans:
        print(i)
else:
    print("not found")