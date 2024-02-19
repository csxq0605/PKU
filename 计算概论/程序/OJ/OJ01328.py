# -*- coding: utf-8 -*-
"""
Created on Sun Oct 15 17:41:30 2023

@author: Lenovo
"""

class island:
    def __init__(self,left,right):
        self.left=left
        self.right=right
from math import sqrt
NO,p=1,[]
while True:
    n,d=map(int,input().split())
    if n==0 and d==0:
        break
    l,num,flag,i=[],1,True,0
    while i<n and flag:
        x,y=map(float,input().split())
        if y>d:
            flag=False
        else:    
            left=x-sqrt(d**2-y**2)
            right=x+sqrt(d**2-y**2)
            l.append(island(left,right))
        i+=1
    for j in range(n-i+1):
        input()
    if not flag:
        p.append(f"Case {NO}: -1")
    else:
        l.sort(key=lambda x:x.left)
        left=l[0].left
        right=l[0].right
        for i in range(1,n):
            if l[i].left<=right:
                right=min(right,l[i].right)
            else:
                num+=1
                right=l[i].right
        p.append(f"Case {NO}: {num}")
    NO+=1
for i in p:
    print(i)