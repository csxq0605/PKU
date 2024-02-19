# -*- coding: utf-8 -*-
"""
Created on Sat Nov 11 12:31:25 2023

@author: Lenovo
"""

from collections import deque
maxn=500
class Edge:
    def __init__(self,v,w,nxt):
        self.v=v
        self.w=w
        self.next=nxt

p=[Edge(0,0,0) for _ in range(maxn)]
cnt=0
q=deque()
def add(u,v,w):
    global cnt
    p[cnt].v=v
    p[cnt].w=w
    p[cnt].next=head[u]
    head[u]=cnt
    cnt+=1
    p[cnt].v=u
    p[cnt].w=0
    p[cnt].next=head[v]
    head[v]=cnt
    cnt+=1

def bfs(s,t):
    vis=[0]*maxn
    vis[s]=1
    min1=float("inf")
    while q:
        q.pop()
    q.append(s)
    while q:
        u=q.popleft()
        i=head[u]
        while i!=-1:
            v=p[i].v
            if not vis[v] and p[i].w:
                vis[v]=1
                min1=min(min1,p[i].w)
                pre[v]=i
                q.append(v)
            i=p[i].next
    if vis[t]:
        return min1
    return -1

while True:
    try:
        m,n=map(int,input().split())
        cnt=0
        max_flow=0
        head=[-1]*maxn
        pre=[-1]*maxn
        p=[Edge(0,0,0) for _ in range(maxn)]
        q=deque()
        for _ in range(m):
            u,v,w=map(int,input().split())
            add(u,v,w)
        while True:
            k=bfs(1,n)
            if k==-1:
                break
            max_flow+=k
            i=pre[n]
            while i!=-1:
                p[i].w-=k
                p[i^1].w+=k
                i=pre[p[i^1].v]
        print(max_flow)
    except EOFError:
        break