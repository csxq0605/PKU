# -*- coding: utf-8 -*-
"""
Created on Mon Sep 25 21:39:28 2023

@author: Lenovo
"""

check=True
def count():
    global check
    a,b,c,d,e,f=map(int,input().split())
    if a==0 and b==0 and c==0 and d==0 and e==0 and f==0:
        check=False
    else:    
        x,y,num=0,0,0
        num+=f+e+d+(c+3)//4
        y=d*5+l[c%4]
        if y<b:
            num+=(b-y+8)//9
        x=36*num-36*f-25*e-16*d-9*c-4*b
        if x<a:
            num+=(a-x+35)//36
        return num
l,number=[0,5,3,1],[]
while check:    
    number.append(count())
del number[-1]
for i in number:
    print(i)