# -*- coding: utf-8 -*-
"""
Created on Thu Dec 28 12:38:26 2023

@author: Lenovo
"""

for _ in range(1,int(input())+1):
    n,m,k=map(int,input().split())
    dic={i:set() for i in range(1,n+1)}
    for i in range(m):
        a,b=map(int,input().split())
        dic[a].add(b)
        dic[b].add(a)
    print(f"Case {_}:")
    for i in range(k):
        i,j=map(int,input().split())
        ans=0
        for num in dic[i]:
            if num in dic[j]:
                ans+=1
        print(ans)