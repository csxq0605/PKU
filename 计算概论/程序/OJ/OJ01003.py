# -*- coding: utf-8 -*-
"""
Created on Sun Sep 17 14:09:23 2023

@author: Lenovo
"""

a=True
list=[]
while a:
    goal=float(input())
    if goal==0.0:
        a=False
    else:
        n,length=0,0
        while length<goal:
            n+=1
            length+=1/(n+1)
        list.append(n)
for n in list:    
    print(f"{n} card(s)")