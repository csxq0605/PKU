# -*- coding: utf-8 -*-
"""
Created on Sun Sep 24 16:56:18 2023

@author: Lenovo
"""

a,b,k=map(int,input().split())
martix=[[1]*a]*b
for i in range(k):
    r,s,p,t=map(int,input().split())
    for i in range(1,a+1):
        for j in range(1,b+1):
            if t==0 and r-p//2<=i<=r+p//2 and s-p//2<=j<=s+p//2:
                martix[i-1][j-1]=0
            if t==1 and (i<r-p//2 or i>r+p//2) and (j<s-p//2 or j>s+p//2):
                martix[i-1][j-1]=0
total=0
for i in martix:
    total+=sum(i)
print(total)