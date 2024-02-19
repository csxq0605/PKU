# -*- coding: utf-8 -*-
"""
Created on Fri Dec 22 10:47:08 2023

@author: Lenovo
"""

n=int(input())
dic,l={},[]
for i in range(n):
    station=input()
    dic[station]=i
    l.append(station)
m=int(input())
for i in range(m):
    s,e=map(str,input().split())
    s1,s2=dic[s],dic[e]
    if s1<s2:
        print(*l[s1:s2+1])
    else:
        print(*(l[s2:s1+1][::-1]))