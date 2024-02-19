# -*- coding: utf-8 -*-
"""
Created on Tue Dec 19 16:28:11 2023

@author: Lenovo
"""


def dfs(n):
    for num in s:
        if num>n or n%num!=0 or num in vis:
            continue
        elif num==n:
            return True
        else:
            vis.add(num)
            if dfs(n//num):
                return True
            vis.discard(num)
    return False

t=int(input())
s=set(map(int,input().split()))
vis=set()
flag=dfs(t)
print("YES" if flag else "NO")