# -*- coding: utf-8 -*-
"""
Created on Sat Oct  7 11:03:21 2023

@author: Lenovo
"""

while True:
    n,p,m=map(int,input().split())
    if n==0 and p==0 and m==0:
        break
    line=[True]*n
    num,i,j=0,0,p-1
    while num<n-1:
        if line[j%n]==True:
            i+=1
        if i==m:
            line[j%n]=False
            i=0
            num+=1
            print(j%n+1,end=",")
        j+=1
    print(line.index(True)+1)