# -*- coding: utf-8 -*-
"""
Created on Fri Nov 17 11:15:37 2023

@author: Lenovo
"""

for _ in range(int(input())):
    n=int(input())
    s=list(map(int,input().split()))
    l,check=[],[True]*n
    for i in range(n):
        l.append([s[2*i+1],s[2*i]])
    l.sort(key=lambda x:(x[0],x[1]))
    ans,num=0,n
    while num:
        ans+=1
        for i in range(n):
            if check[i]:
                now=l[i]
                check[i]=False
                num-=1
                break
        for i in range(n):
            if now[0]<=l[i][0] and now[1]<=l[i][1] and check[i]:
                now=l[i]
                check[i]=False
                num-=1
    print(ans)