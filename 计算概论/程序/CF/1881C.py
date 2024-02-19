# -*- coding: utf-8 -*-
"""
Created on Tue Nov 28 11:09:20 2023

@author: Lenovo
"""

for _ in range(int(input())):
    n=int(input())
    martix=[[0]*(n+2)]
    martix.extend([[0]+list(input())+[0] for i in range(n)])
    martix.extend([[0]*(n+2)])
    ans=0
    for i in range(1,n//2+1):
        for j in range(1,n//2+1):
            a,b,c,d=ord(martix[i][j]),ord(martix[j][n+1-i]),ord(martix[n+1-i][n+1-j]),ord(martix[n+1-j][i])
            maxn=max(a,b,c,d)
            ans+=maxn*4-a-b-c-d
    print(ans)