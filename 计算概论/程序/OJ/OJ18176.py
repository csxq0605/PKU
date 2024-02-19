# -*- coding: utf-8 -*-
"""
Created on Thu Dec  7 15:07:58 2023

@author: Lenovo
"""

from math import sqrt
n=10000
ls,x,y=[True]*(n+1),2,int(sqrt(n))+1
while x<y:
    if ls[x]==True:
        for i in range(x*2,n+1,x):
            ls[i]=False
    x+=1
ls=set([i**2 for i in range(2,n+1) if ls[i]==True])

m,n=map(int,input().split())
for _ in range(m):
    scores=list(map(int,input().split()))
    score=0
    for i in scores:
        if i in ls:
            score+=i
    print("%.2f"%(score/len(scores)) if score else 0)