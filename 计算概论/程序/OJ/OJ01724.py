# -*- coding: utf-8 -*-
"""
Created on Sat Oct 21 20:00:45 2023

@author: Lenovo
"""

import sys
sys.setrecursionlimit(10**8)

initvalue=float('inf')
minlen,totallen,totalcost=initvalue,0,0
def dfs(s):
    global totallen,totalcost,minlen
    if s==n:
        minlen=min(minlen,totallen)
        return
    for road in citymap[s]:
        d,l,t=road['d'],road['l'],road['t']
        if visited[d]:
            continue
        cost=t+totalcost
        length=l+totallen
        if cost>k or length>=minlen or length>=minl[d][cost]:
            continue
        totallen=length
        totalcost=cost
        minl[d][cost]=length
        visited[d]=1
        dfs(d)
        totallen-=l
        totalcost-=t
        visited[d]=0

k=int(input())
n=int(input())
r=int(input())
citymap=[[] for _ in range(n+1)]
for _ in range(r):
    s,r_d,r_l,r_t=map(int,input().split())
    if s!=r_d:
        citymap[s].append({'d':r_d,'l':r_l,'t':r_t})
minl=[[initvalue]*(k+1) for _ in range(n+1)]
visited=[0]*(n+1)
visited[1]=1
dfs(1)
if minlen<initvalue:
    print(minlen)
else:
    print(-1)