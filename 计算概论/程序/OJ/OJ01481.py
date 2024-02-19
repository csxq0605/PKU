# -*- coding: utf-8 -*-
"""
Created on Tue Nov  7 23:21:56 2023

@author: Lenovo
"""

import sys
sys.setrecursionlimit(10**8)

dx=[0,0,1,-1]
dy=[1,-1,0,0]

def ddfs(s,e):
    mmap[s][e]='*'
    for i in range(4):
        xx=s+dx[i]
        yy=e+dy[i]
        if 0<=xx<h and 0<=yy<w and mmap[xx][yy]=='X':
            ddfs(xx,yy)

def dfs(s,e):
    mmap[s][e]='.'
    for i in range(4):
        xx=s+dx[i]
        yy=e+dy[i]
        if not (0<=xx<h and 0<=yy<w) or mmap[xx][yy]=='.':
            continue
        if mmap[xx][yy]=='X':
            ddfs(xx,yy)
            num[l]+=1
        if mmap[xx][yy]=='*':
            dfs(xx,yy)

k=1
while True:
    w,h=map(int,input().split())
    if w==0 and h==0:
        break
    mmap=[]
    for _ in range(h):
        row=list(input())
        mmap.append(row)
    num=[0]*1000
    l=0
    for i in range(h):
        for j in range(w):
            if mmap[i][j]=='*':
                dfs(i,j)
                l+=1
    print(f'Throw {k}')
    k+=1
    sorted_nums=sorted(num[:l])
    print(' '.join(map(str,sorted_nums)))
    print()