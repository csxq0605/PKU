# -*- coding: utf-8 -*-
"""
Created on Sat Nov 11 12:25:49 2023

@author: Lenovo
"""

from collections import deque
inf=float('inf')
maxn=205
maxe=4*maxn*maxn

class Solution:
    class Edge:
        def __init__(self,v,w,nxt):
            self.v=v
            self.w=w
            self.nxt=nxt
    
    def __init__(self):
        self.edge=[self.Edge(0,0,0)for _ in range(maxe)]
        self.head=[-1]*maxn
        self.tot=0
        self.level=[-1]*maxn
    
    def init(self):
        self.head=[-1]*maxn
        self.tot=0
    
    def add(self,u,v,w):
        self.edge[self.tot]=self.Edge(v,w,self.head[u])
        self.head[u]=self.tot
        self.edge[self.tot+1]=self.Edge(u,0,self.head[v])
        self.head[v]=self.tot+1
        self.tot+=2
    
    def bfs(self,s,t):
        self.level=[-1]*maxn
        q=deque([s])
        self.level[s]=0
        while q:
            u=q.popleft()
            i=self.head[u]
            while i!=-1:
                if self.edge[i].w>0 and self.level[self.edge[i].v]<0:
                    self.level[self.edge[i].v]=self.level[u]+1
                    q.append(self.edge[i].v)
                i=self.edge[i].nxt
        return self.level[t]>0
    
    def dfs(self,u,t,f):
        if u==t:
            return f
        i=self.head[u]
        while i!=-1:
            v=self.edge[i].v
            if self.edge[i].w>0 and self.level[v]>self.level[u]:
                d=self.dfs(v,t,min(f,self.edge[i].w))
                if d>0:
                    self.edge[i].w-=d
                    self.edge[i ^ 1].w+=d
                    return d
            i=self.edge[i].nxt
        self.level[u]=-1
        return 0
    
    def solve(self,s,t):
        flow=0
        while self.bfs(s,t):
            while f:=self.dfs(s,t,inf):
                flow+=f
        return flow

S=Solution()
while True:
    try:
        m,n=map(int,input().split())
        S.init()
        for _ in range(m):
            u,v,c=map(int,input().split())
            S.add(u,v,c)
        print(S.solve(1,n))
    except EOFError:
        break