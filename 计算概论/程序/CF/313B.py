# -*- coding: utf-8 -*-
"""
Created on Tue Nov  7 11:22:18 2023

@author: Lenovo
"""

string="."+input()
ans=[0]*len(string)
for i in range(1,len(string)-1):
        if string[i]==string[i+1]:
            ans[i]=ans[i-1]+1
        else:
            ans[i]=ans[i-1]
m=int(input())
for _ in range(m):
    l,r=map(int,input().split())
    print(ans[r-1]-ans[l-1])