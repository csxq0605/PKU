# -*- coding: utf-8 -*-
"""
Created on Sat Dec 16 12:17:17 2023

@author: Lenovo
"""

l=list((" "+input()).split("."))
flag=False
if l[-1]!="":l.append("");flag=True
for i in range(len(l)-1):
    l[i]+=" "
    l[i]=l[i].lower()
    l[i]=list(l[i].split(","))
    for j in range(len(l[i])-1):
        l[i][j]+=" "
a,b=map(str.lower,input().split())
a,b=" "+a+" "," "+b+" "
for i in range(len(l)-1):
    for j in range(len(l[i])):
        l[i][j]=l[i][j].replace(a,b)
for i in range(len(l)-1):
    for j in range(len(l[i])):
        l[i][j]=l[i][j][1:-1]
for i in range(len(l)-1):
    l[i]=(", ".join(l[i])+".").capitalize()
print(" ".join(l[:-1]) if not flag else (" ".join(l[:-1])[:-1]))