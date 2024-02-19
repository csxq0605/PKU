# -*- coding: utf-8 -*-
"""
Created on Tue Nov 14 10:06:08 2023

@author: Lenovo
"""

n,m=map(int,input().split())
l=list(map(int,input().split()))
check=[0]*10001
ans,cnt=1,0
for i in range(n):
    if not check[l[i]]:
        check[l[i]]=1
        cnt+=1
        if cnt==m:
            ans+=1
            cnt,check=0,[0]*10001
print(ans)