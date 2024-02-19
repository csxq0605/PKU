# -*- coding: utf-8 -*-
"""
Created on Sun Dec  3 00:12:07 2023

@author: Lenovo
"""

def dfs(x,d):
    if d<=l-1:
        for i in tree[x]:
            if check[i]:
                check[i]=False
                ans.append(i)
                dfs(i,d+1)

n,m,l=map(int,input().split())
tree=[[] for _ in range(n)]
for i in range(m):
    a,b=map(int,input().split())
    tree[a].append(b)
    tree[b].append(a)
for i in tree:
    i.sort()
start=int(input())
check,ans=[True]*n,[start]
check[start]=False
dfs(start,0)
print(*ans)