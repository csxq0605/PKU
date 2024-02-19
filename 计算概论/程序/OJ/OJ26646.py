# -*- coding: utf-8 -*-
"""
Created on Wed Oct 18 17:22:04 2023

@author: Lenovo
"""

def calculate(x,y,m):
    tem=[]
    for start in range(max(0,x-y+1),min(m,x+1)):
        end=start+y
        if end<=m:
            tem.append((start,end))
    return tem

n,m=map(int,input().split())
line=[]
l=[tuple(map(int,input().split())) for _ in range(n)]
for x,y in l:
    line.extend(calculate(x,y,m))
line.sort(key=lambda x:(x[1],x[0]))
ans,now_end=0,0
for start,end in line:
    if start>=now_end:
        now_end=end
        ans+=1
print(ans)