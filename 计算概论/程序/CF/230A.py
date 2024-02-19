# -*- coding: utf-8 -*-
"""
Created on Sun Oct 15 17:25:26 2023

@author: Lenovo
"""

s,n=map(int,input().split())
line=[]
for i in range(n):
    line.append([int(x) for x in input().split()])
line.sort()

def j(s,n,line):
    for i in range(n):
        if s>line[i][0]:
            s+=line[i][1]
        else:
            return "NO"
    return "YES"

print(j(s,n,line))