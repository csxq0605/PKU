# -*- coding: utf-8 -*-
"""
Created on Thu Nov 30 22:34:34 2023

@author: Lenovo
"""

for _ in range(int(input())):
    n=int(input())
    tree=[[] for i in range(n+1)]
    for i in range(n-1):
        u,v=map(int,input().split())
        tree[u].append(v)
        tree[v].append(u)
    stack,dic=[(1,0,0)],{}
    while stack:
        x,y,t=stack.pop()
        if t==0:
            stack.append((x,y,1))
            for spot in tree[x]:
                if spot!=y:
                    stack.append((spot,x,0))
        else:
            if tree[x]==[y]:
                dic[x]=1
            else:
                dic[x]=sum(dic[spot] for spot in tree[x] if spot!=y)
    for i in range(int(input())):
        a,b=map(int,input().split())
        print(dic[a]*dic[b])