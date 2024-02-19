# -*- coding: utf-8 -*-
"""
Created on Tue Nov  7 12:02:25 2023

@author: Lenovo
"""

n=int(input())
l=[int(_) for _ in input().split()]
l.sort()
ans=[0]*100001
cnt=0
i=1
while i<=100000:
    if i==l[cnt]:
        ans[i]=max(ans[i-1],ans[i])+1
        cnt+=1
    else:
        ans[i]=max(ans[i-1],ans[i])
        i+=1
    if cnt>=n:
        break
q=int(input())
for i in range(q):
    m=int(input())
    if m<=l[-1]:    
        print(ans[m])
    else:
        print(ans[l[-1]])