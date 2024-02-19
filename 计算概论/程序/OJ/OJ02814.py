# -*- coding: utf-8 -*-
"""
Created on Tue Nov  7 16:46:42 2023

@author: Lenovo
"""

mp=["","ABDE","ABC","BCEF","ADG","BDEFH","CFI","DEGH","GHI","EFHI"]
arr=[0]*10
vis=[0]*10
sum_val=[0]*10
ans=[0]*10
minn=float('inf')
def dfs(depth):
    global minn
    if depth==10:
        for i in range(1,10):
            if arr[i]%4!=0:
                return
        asum=sum(sum_val[1:])
        if asum<minn:
            for i in range(1,10):
                if vis[i]==1:
                    ans[i]=sum_val[i]
                else:
                    ans[i]=0
            minn=asum
        return
    for i in range(4):
        for j in range(len(mp[depth])):
            arr[ord(mp[depth][j])-64]=(arr[ord(mp[depth][j])-64]+i)
        vis[depth]=0 if i==0 else 1
        sum_val[depth]=i
        dfs(depth+1)
        for j in range(len(mp[depth])):
            arr[ord(mp[depth][j])-64]=(arr[ord(mp[depth][j])-64]-i)%12
        vis[depth]=0
        sum_val[depth]=0

arr[1:4]=map(int,input().split())
arr[4:7]=map(int,input().split())
arr[7:10]=map(int,input().split())
dfs(1)
for i in range(1,10):
    if ans[i]!=0:
        for j in range(ans[i]):
            print(i,end=" ")
print()