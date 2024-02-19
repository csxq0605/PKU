# -*- coding: utf-8 -*-
"""
Created on Tue Nov  7 21:35:24 2023

@author: Lenovo
"""

while True:
    s=input()
    n=len(s)
    if s==".":
        break
    Next=[0]*(n+1)
    Next[0]=-1
    Next[1]=0
    for i in range(2,n+1):
        t=Next[i-1]
        while(t>=0 and s[i-1]!=s[t]):
            t=Next[t]
        Next[i]=t+1
    print(n//(n-Next[n]) if n%(n-Next[n])==0 else 1)