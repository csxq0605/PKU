# -*- coding: utf-8 -*-
"""
Created on Fri Oct  6 15:00:03 2023

@author: Lenovo
"""

while True:
    n,m=map(int,input().split())
    if n==0 and m==0:
        break
    line=[True]*n
    num,i,j=0,0,0
    while num<n-1:
        if line[j%n]==True:
            i+=1
        if i==m:
            line[j%n]=False
            i=0
            num+=1
        j+=1
    print(line.index(True)+1)