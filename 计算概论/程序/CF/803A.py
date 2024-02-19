# -*- coding: utf-8 -*-
"""
Created on Tue Oct 24 10:23:52 2023

@author: Lenovo
"""

def check(k):
    if k>1:
        return True
    return False

n,k=map(int,input().split())
martix=[["0"]*n for _ in range(n)]
if n*n<k:
    print(-1)
else:   
    m=0
    while check(k):
       martix[m][m]="1"
       k-=1
       i=m+1
       while check(k) and i<n:
           martix[i][m]="1"
           martix[m][i]="1"
           k-=2
           i+=1
       m+=1
    if k==1:
        martix[m][m]="1"
    for l in martix:
        print(" ".join(l))