# -*- coding: utf-8 -*-
"""
Created on Thu Dec  7 15:28:30 2023

@author: Lenovo
"""

n=int(input())
pairs=[i[1:-1] for i in input().split()]
distances=[sum(map(int,i.split(','))) for i in pairs]
prices=list(map(int,input().split()))
values=[distances[i]/prices[i] for i in range(n)]
pnew=sorted(prices)
vnew=sorted(values)
if n%2==0:
    pmid=(pnew[n//2]+pnew[n//2-1])/2
    vmid=(vnew[n//2]+vnew[n//2-1])/2
else:
    pmid=pnew[n//2]
    vmid=vnew[n//2]
ans=0
for i in range(n):
    if values[i]>vmid and prices[i]<pmid:
        ans+=1
print(ans)