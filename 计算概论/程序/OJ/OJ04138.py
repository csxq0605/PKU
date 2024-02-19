# -*- coding: utf-8 -*-
"""
Created on Fri Oct  6 14:26:12 2023

@author: Lenovo
"""

n=int(input())
if n%2==1:
    print(2*(n-2))
else:
    from math import sqrt
    ls,x,y=[True]*(n+1),2,int(sqrt(n))+1
    while x<y:
        if ls[x]==True:
            for i in range(x*2,n+1,x):
                ls[i]=False
        x+=1
    ls=[i for i in range(2,n+1) if ls[i]==True]
    i=0
    while True:
       if n//2-i in ls and n//2+i in ls:
           print((n//2-i)*(n//2+i))
           break
       i+=1