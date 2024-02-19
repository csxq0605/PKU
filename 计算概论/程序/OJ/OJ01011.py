# -*- coding: utf-8 -*-
"""
Created on Sat Nov  4 11:01:50 2023

@author: Lenovo
"""

visit=[False]*64
def dfs(cnt,curlen,left,begin):
    global visit
    if cnt==total//curlen:
        return True
    fail=-1
    for i in range(begin,n):
        if visit[i] or fail==l[i]:
            continue
        visit[i]=True
        if left==l[i]:
            if dfs(cnt+1,curlen,curlen,0):
                return True
            fail=l[i]
        elif left>l[i]:
            if dfs(cnt,curlen,left-l[i],i+1):
                return True
            fail=l[i]
        visit[i]=False
        if left==curlen:
            break
    return False

while True:
    n=int(input())
    if n==0:
        break
    l=[int(i) for i in input().split()]
    total=sum(l)
    l.sort(reverse=True)
    maxlen=l[0]
    flag=False
    for length in range(maxlen,total-maxlen+1):
        if total%length==0:
            visit=[False]*n
            if dfs(0,length,length,0):
                print(length)
                flag=True
                break
    if not flag:
        print(total)