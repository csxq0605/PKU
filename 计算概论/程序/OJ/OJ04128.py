# -*- coding: utf-8 -*-
"""
Created on Sun Oct 29 09:51:01 2023

@author: Lenovo
"""

def bfs(string,n):
    global min1,flag
    total=0
    for i in range(length):
        if total>1:
            break
        if string[i]!=str2[i]:
            total+=1
    if total==1:
        flag=True
        min1=min(min1,n+2)
        return
    else:
        for i in range(m):
            total=0
            if vis[i]:
                for j in range(length):
                    if total>1:
                        break
                    if string[j]!=f[i][j]:
                        total+=1
            if total==1:
                vis[i]=False
                bfs(f[i],n+1)
                vis[i]=True

str1,str2=input().split()
flag,min1=False,float("inf")
f=[_ for _ in input().split()]
lenf=len(f)
vis=[True]*lenf
m=lenf
length=len(str1)
bfs(str1,0)
if flag:
    print(min1)
else:
    print(0)