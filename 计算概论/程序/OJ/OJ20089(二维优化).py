# -*- coding: utf-8 -*-
"""
Created on Thu Dec 21 15:25:16 2023

@author: Lenovo
"""

n=int(input())
if n%50!=0:
    print("Fail")
    quit()
n//=50
l=list(map(int,input().split()))
cost=[1,2,5,10,20,50,100]
dp=[0]+[float("inf")]*n
for i in range(7):
    num,c=l[i],cost[i]
    k=1
    while num>0:
        tmp=min(num,k)
        num-=tmp
        for j in range(n,c*tmp-1,-1):
            dp[j]=min(dp[j],dp[j-tmp*c]+tmp)
        k*=2
print(dp[n] if dp[n]!=float("inf") else "Fail")