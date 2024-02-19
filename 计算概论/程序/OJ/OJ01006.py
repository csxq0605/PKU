# -*- coding: utf-8 -*-
"""
Created on Sun Oct 15 17:32:43 2023

@author: Lenovo
"""

l=[]
A=True
while A:
    days=input()
    if days!="-1 -1 -1 -1":
        l.append(list(map(int,days.split())))
    else:
        A=False
n=0
for queue in l:
    n+=1;B=True
    q,e,i,d=map(int,queue)
    q=q%23;e=e%28;i=i%33
    add=23-q
    while B:
        if (e+add)%28==0 and (i+add)%33==0:
            B=False
        else:
            add+=23
    d+=add
    if d>=21252:
        num=42504-d
    else:
        num=21252-d
    print(f'Case {n}: the next triple peak occurs in {num} days.')