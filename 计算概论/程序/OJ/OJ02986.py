# -*- coding: utf-8 -*-
"""
Created on Fri Oct  6 21:22:33 2023

@author: Lenovo
"""

while True:
    try:
        n,k=map(int,input().split())
        line1=[1]*2+[0]*(k-1)
        line2=[1]+[0]*k
        for i in range(2,n+1):
            for j in range(1,min(i,k)+1):
                line2[j]=line1[j-1]+line1[j]
            line1=line2
            line2=[1]+[0]*k
        print(line1[k]%2)
    except:
        break