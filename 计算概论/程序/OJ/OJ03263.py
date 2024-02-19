# -*- coding: utf-8 -*-
"""
Created on Thu Nov 16 13:51:25 2023

@author: Lenovo
"""

while True:
    n=int(input())
    if n==0:
        break
    maxsum=[[0]*120 for _ in range(120)]
    a=[[0]*120 for _ in range(120)]
    for i in range(1,n+1):
        a[i][1:i+1]=map(int,input().split())
    x,y=map(int,input().split())
    for i in range(n,0,-1):
        for j in range(1,i+1):
            max_low=max(maxsum[i+1][j],maxsum[i+1][j+1])
            maxsum[i][j]=max(max_low,a[i][j])
    print(maxsum[x][y])