# -*- coding: utf-8 -*-
"""
Created on Tue Nov 14 17:22:20 2023

@author: Lenovo
"""

n=int(input())
line=list(map(int,input().split()))
dp=[0]+[float("inf")]*n
l=r=0
for i in range(1,n+1):
    l=max(1,i-line[i-1])
    r=min(n,i+line[i-1])
    if dp[r]>dp[l-1]+1:
        for j in range(l,r+1):
            dp[j]=min(dp[j],dp[l-1]+1)
print(dp[n])

n=int(input())
a=list(map(int,input().split()))
intervals=[(max(0,i-a[i]),min(n-1,i+a[i])) for i in range(n)]
intervals.sort()
ans,right,temp,i=0,0,0,0
while i<n and right<n:
    while i<n and intervals[i][0]<=right:
        temp=max(temp,intervals[i][1])
        i+=1
    right=temp+1
    ans+=1
print(ans)