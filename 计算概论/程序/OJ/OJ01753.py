# -*- coding: utf-8 -*-
"""
Created on Sun Oct 29 13:57:05 2023

@author: Lenovo
"""

def isgoal():
    for i in range(1,5):
        for j in range(1,5):
            if map[i][j]!=map[1][1]:
                return False
    return True

def flip(row,col):
    for i in range(5):
        r,c=row+dr[i],col+dc[i]
        map[r][c]=not map[r][c]

def dfs(row,col,dep):
    global flag
    if dep==step:
        flag=isgoal()
        return
    if flag or row==5:
        return
    flip(row,col)
    if col<4:
        dfs(row,col+1,dep+1)
    else:
        dfs(row+1,1,dep+1)
    flip(row,col)
    if col<4:
        dfs(row,col+1,dep)
    else:
        dfs(row+1,1,dep)

map=[[False]*6 for _ in range(6)]
dr=[-1,0,0,0,1]
dc=[0,-1,0,1,0]
for i in range(1,5):
    row=input().strip()
    for j in range(1,5):
        if row[j-1]=='b':
            map[i][j]=True
for step in range(17):
    flag=False
    dfs(1,1,0)
    if flag:
        break
if flag:
    print(step)
else:
    print("Impossible")