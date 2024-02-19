# -*- coding: utf-8 -*-
"""
Created on Thu Nov 16 14:01:13 2023

@author: Lenovo
"""

dp=[0]*1010
kg=[1,2,3,5,10,20]
num=list(map(int,input().split()))
sum_val=0
ans=0
for i in range(6):
    sum_val+=num[i]*kg[i]
dp[0]=1
for i in range(6):
    for j in range(1,num[i]+1):
        for k in range(sum_val,kg[i]-1,-1):
            if dp[k-kg[i]]==1:
                dp[k]=1
for i in range(1,sum_val+1):
    if dp[i]==1:
        ans+=1
print(f"Total={ans}")