# -*- coding: utf-8 -*-
"""
Created on Sat Dec  9 10:42:19 2023

@author: Lenovo
"""

n,l=map(int,input().split())
line=[int(i) for i in input().split()]
line.sort()
num=max(line[0]-0,l-line[-1])
for i in range(n-1):
    num=max(num,(line[i+1]-line[i])/2)
print(num)