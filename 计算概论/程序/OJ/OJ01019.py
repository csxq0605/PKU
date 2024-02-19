# -*- coding: utf-8 -*-
"""
Created on Sun Oct 15 17:29:34 2023

@author: Lenovo
"""

import math
n=int(input())
l=[]
for i in range(n):
    p=int(input())
    total,add=1,1
    i=1
    while total<p:
        i+=1
        add=add+int(math.log10(i))+1
        total+=add
    total-=add
    pos=p-total
    i=1
    while pos>=(int(math.log10(i))+1):
        pos-=int(math.log10(i))+1
        i+=1
    if pos==0:
        digit=int(str(i-1)[-1])
    else:
        digit=int(str(i)[pos-1])
    l.append(digit)
for i in l:
    print(i)