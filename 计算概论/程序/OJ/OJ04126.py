# -*- coding: utf-8 -*-
"""
Created on Wed Nov  1 21:55:50 2023

@author: Lenovo
"""

maxn=10
f=[[0]*maxn for _ in range(1<<(maxn+1))]
genes=[''for _ in range(maxn+1)]
invalid=[False]*(maxn+1)
l=[0]*(maxn+1)
chong=[[0]*(maxn+1) for _ in range(maxn+1)]
minlen,base=0,0

def dp(state,last):
    global f
    if f[state][last]:
        return f[state][last]
    f[state][last]=(1<<10)
    for i in range(1,n+1):
        flag=state&(1<<i)
        if invalid[i] and flag!=0:
            f[state][last]=min(dp(state-(1<<i),i)+l[last]-chong[last][i],f[state][last])
    return f[state][last]

t=int(input())
for _ in range(t):
    n=int(input())
    for i in range(1,n+1):
        genes[i]=input()
    f=[[0]*maxn for _ in range(1<<(maxn+1))]
    minlen=2<<10
    base=1<<(n+1)
    for i in range(1,n+1):
        invalid[i]=True
        f[0][i]=l[i]=len(genes[i])
    for i in range(1,n+1):
        for j in range(1,n+1):
            if i!=j and invalid[i] and invalid[j] and genes[i].find(genes[j])!=-1:
                invalid[j]=False
                base-=1<<j
            if i!=j and invalid[i] and invalid[j]:
                l0=min(l[i],l[j])
                while l0:
                    if genes[j]==genes[j][genes[j].find(genes[i][l[i]-l0:]):]:
                        break
                    l0-=1
                chong[i][j]=l0
    for i in range(1,n+1):
        if invalid[i]:
            minlen=min(dp(base-(1<<i)-2,i),minlen)
    print(minlen)