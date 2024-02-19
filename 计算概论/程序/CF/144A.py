# -*- coding: utf-8 -*-
"""
Created on Sun Oct 15 17:19:34 2023

@author: Lenovo
"""

n=int(input())
line=[int(i) for i in input().split()]
mi=[x for x ,y in list(enumerate(line)) if y==min(line)]
mini=mi[len(mi)-1]
ma=line.index(max(line))
if mini>ma:
    print(ma+len(line)-1-mini)
else:
    print(ma-1+len(line)-1-mini)