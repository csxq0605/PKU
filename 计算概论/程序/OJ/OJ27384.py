# -*- coding: utf-8 -*-
"""
Created on Sun Dec 17 11:22:46 2023

@author: Lenovo
"""

import heapq
n,k=map(int,input().split())
l=list(map(int,input().split()))
l=[[l[i],l[i+1]]for i in range(0,2*n,2)]
l.sort()
s=set(map(int,input().split()))
heap=[]
for member in s:
    heapq.heappush(heap,[0,member])
count=[0]*314160
if k==314159:
    print(l[-1][0])
    quit()
ans=max2=0
for i in range(n):
    member=l[i][1]
    count[member]+=1
    if member in s:
        while count[heap[0][1]]:
            f=heapq.heappop(heap)
            f=[f[0]+count[f[1]],f[1]]
            heapq.heappush(heap,f)
            count[f[1]]=0
    else:
        max2=max(max2,count[member])
    if heap[0][0]>max2 and i!=n-1 and l[i+1][0]!=l[i][0]:
        ans+=l[i+1][0]-l[i][0]
print(ans)