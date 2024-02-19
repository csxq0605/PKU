# -*- coding: utf-8 -*-
"""
Created on Fri Dec 15 15:07:59 2023

@author: Lenovo
"""

from collections import deque
n,m=map(int,input().split())
dic={i:[]for i in range(n)}
ceil=[0]*n
for i in range(m):
    a,b=map(int,input().split())
    dic[b].append(a)
    ceil[a]+=1
queue=deque()
for i in range(n):
    if not ceil[i]:
        queue.append(i)
awards=[100]*n
while queue:
    team=queue.popleft()
    for teams in dic[team]:
        ceil[teams]-=1
        if awards[teams]<=awards[team]:
            awards[teams]=awards[team]+1
        if ceil[teams]==0:
            queue.append(teams)
ans=sum(awards)
print(ans)