# -*- coding: utf-8 -*-
"""
Created on Wed Oct 25 18:31:55 2023

@author: Lenovo
"""

import sys
sys.setrecursionlimit(10**8)

INF=int(1e9)
n,ans,step,record,weight,pos=0,INF,0,[],[0 for _ in range(20)],0
a,book=[[0]*20 for _ in range(20)],[0 for _ in range(20)]

def dfs(cur,now):
    global ans,step,pos,a,book,weight,n
    if cur+2==n:
        step+=a[now][n]
        if(step<ans):
            ans=step
        step-=a[now][n]
        return
    if step>ans:
        return
    for i in range(2,n):
        if book[i]==0:
            if record[i][pos+weight[i]]<=step+a[now][i]:
                continue
            step+=a[now][i]
            pos+=weight[i]
            book[i]=1
            record[i][pos]=step
            dfs(cur+1,i)
            step-=a[now][i]
            pos-=weight[i]
            book[i]=0
    return

for i in range(1,17):
    weight[i]=(1<<i)
while True:
    try:
        n=int(input())
        ans,step,pos=INF,0,0
        book=[0 for _ in range(20)]
        record=[[INF for _ in range((1<<15))] for _ in range(20)]
        for i in range(1,n+1):
            a[i][1:n+1]=map(int,input().split())
        dfs(0,1)
        print(ans)
    except EOFError:
        break