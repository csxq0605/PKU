# -*- coding: utf-8 -*-
"""
Created on Tue Sep 26 11:25:46 2023

@author: Lenovo
"""

while True:
    n,m=map(int,input().split())
    if n==0 and m==0:
        break
    l=[int(i) for i in input().split()]
    price=l[:n]
    number=l[n:]
    dp_set=set()
    dp_set.add(0)
    for i in range(n):
        dp_list=list(dp_set)
        for j in range(1,number[i]+1):    
            for p in dp_list:
                price1=p+price[i]*j
                if price1>m:
                    break
                dp_set.add(price1)
    print(len(dp_set)-1)