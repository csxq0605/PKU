# -*- coding: utf-8 -*-
"""
Created on Mon Dec  4 10:29:11 2023

@author: Lenovo
"""

p=int(input())
weapon=list(map(int,input().split()))
weapon.sort()
l,r=0,len(weapon)-1
ans=tmp=0
while l<=r:
    if p>=weapon[l]:
        p-=weapon[l]
        l+=1
        tmp+=1
    elif p<weapon[l] and tmp>0:
        tmp-=1
        p+=weapon[r]
        r-=1
    else:
        break
    ans=max(ans,tmp)
print(ans)