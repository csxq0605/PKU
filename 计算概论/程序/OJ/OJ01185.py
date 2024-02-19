# -*- coding: utf-8 -*-
"""
Created on Tue Dec 26 00:00:11 2023

@author: Lenovo
"""

n,m=map(int,input().split())
maxsta=1<<m
num,sta,pic=[0]*110,[0]*110,[0]*110
dp=[[[0]*(110)for _ in range(110)]for _ in range(110)]
def cal(x):
    num=0
    while x:
        if x&1:
            num+=1
        x>>=1
    return num

cnt=ans=0
for i in range(1,n+1):
    str_input=list(input())
    for j in range(1,m+1):
        if str_input[j-1]=='H':
            pic[i]+=1<<(j-1)
for i in range(maxsta):
    if not (i&(i<<1)) and not (i&(i<<2)):
        cnt+=1
        sta[cnt]=i
        num[cnt]=cal(i)
for i in range(1,cnt+1):
    if not (sta[i]&pic[1]):
        dp[1][i][1]=num[i]
for i in range(2,n+1):
    for j in range(1,cnt+1):
        if sta[j]&pic[i]:
            continue
        for k in range(1,cnt+1):
            if sta[j]&sta[k] or sta[k]&pic[i-1]:
                continue
            for l in range(1,cnt+1):
                if sta[l]&pic[i-2] or sta[l]&sta[j] or sta[l]&sta[k]:
                    continue
                dp[i][j][k]=max(dp[i][j][k],dp[i-1][k][l]+num[j])
for i in range(1,cnt+1):
    for j in range(1,cnt+1):
        ans=max(ans,dp[n][i][j])
print(ans)