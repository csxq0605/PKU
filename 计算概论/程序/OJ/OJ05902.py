# -*- coding: utf-8 -*-
"""
Created on Thu Dec 14 08:51:35 2023

@author: Lenovo
"""

for _ in range(int(input())):
    n=int(input())
    queue=[]
    cnt=0
    for i in range(n):
        t,num=map(int,input().split())
        if t==1:
            queue.append(num)
        elif t==2 and num==0:
            cnt+=1
        else:
            queue.pop()
    if queue[cnt::]:
        print(*queue[cnt::])
    else:
        print("NULL")