# -*- coding: utf-8 -*-
"""
Created on Tue Dec 19 15:58:06 2023

@author: Lenovo
"""

import sys
import heapq
from collections import defaultdict
input=sys.stdin.readline
hl,hr=[],[]
ldict,rdict=defaultdict(int),defaultdict(int)
n=int(input())
for _ in range(n):
    op,l,r=map(str,input().split())
    l,r=int(l),int(r)
    if op=="+":
        ldict[l]+=1
        rdict[r]+=1
        heapq.heappush(hl,-l)
        heapq.heappush(hr,r)
    else:
        ldict[l]-=1
        rdict[r]-=1
    while hl and ldict[-hl[0]]<=0:
        heapq.heappop(hl)
    while hr and rdict[hr[0]]<=0:
        heapq.heappop(hr)
    if hl and -hl[0]>hr[0]:
        print("Yes")
    else:
        print("No")