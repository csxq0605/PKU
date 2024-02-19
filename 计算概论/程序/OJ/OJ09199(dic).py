# -*- coding: utf-8 -*-
"""
Created on Thu Dec 14 08:55:51 2023

@author: Lenovo
"""

from collections import defaultdict,deque
m,n=map(int,input().split())
l=list(map(int,input().split()))
dic=defaultdict(int)
queue=deque()
length=ans=0
for num in l:
    if not dic[num] and length<m:
        ans+=1
        length+=1
        dic[num]=1
        queue.append(num)
    elif not dic[num] and length==m:
        dic[num]=1
        queue.append(num)
        ans+=1
        p=queue.popleft()
        dic[p]=0
print(ans)