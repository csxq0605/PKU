# -*- coding: utf-8 -*-
"""
Created on Fri Dec  1 20:41:32 2023

@author: Lenovo
"""

from collections import defaultdict
n=int(input())
num=list(map(int,input().split()))
dic=defaultdict(int)
ans,res=0,[]
for i in range(n):
    dic[num[i]]=dic[num[i]-1]+1
    if dic[num[i]]>ans:
        ans=dic[num[i]]
        end=num[i]
print(ans)
for i in range(n-1,-1,-1):
    if num[i]==end:
        res.append(i+1)
        end-=1
        ans-=1
    if ans==0:
        print(*res[::-1])
        break