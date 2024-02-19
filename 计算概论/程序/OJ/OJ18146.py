# -*- coding: utf-8 -*-
"""
Created on Tue Nov 28 10:08:18 2023

@author: Lenovo
"""

n,k=map(int,input().split())
l=list(map(int,input().split()))
count=[0]*5
for i in l:
    count[4]+=i//4
    count[i%4]+=1
if count[3]:
    count[2]+=count[3]
    count[1]+=count[3]
    count[3]=0
if count[4]>n:
    if (count[4]-n)*2+count[2]+count[1]<=n*2:
        print("YES")
    else:
        print("NO")
else:
    left=n-count[4]
    can=min(left,count[1],count[2])
    count[2]-=can
    count[1]-=can
    left-=can
    if not count[2]:
        if count[1]<=(left+n)*2:
            print("YES")
        else:
            print("NO")
    elif not count[1]:
        if count[2]<=int(left*1.5)+n*2:
            print("YES")
        else:
            print("NO")
    else:
        if count[2]+count[1]<=n*2:
            print("YES")
        else:
            print("NO")