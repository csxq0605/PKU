# -*- coding: utf-8 -*-
"""
Created on Wed Oct 25 19:32:22 2023

@author: Lenovo
"""

N=16
def min_cost(n, g):
    f=[[float('inf')]*N for _ in range(1 << N)]
    for i in range(n):
        g[i][:n]=map(int,input().split())
    f[1][0]=0 
    for i in range(1,1 << n):
        for j in range(n):
            if (i >> j)&1:
                for k in range(n):
                    if (i >> k)&1:
                        f[i][j]=min(f[i][j],f[i-(1 << j)][k]+g[k][j])
    return f[(1 << n)-1][n-1]

while True:
    try:
        n=int(input())
        g=[[0]*N for _ in range(N)]
        result=min_cost(n,g)
        print(result)
    except EOFError:
        break