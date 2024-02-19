# -*- coding: utf-8 -*-
"""
Created on Tue Aug 29 21:51:32 2023

@author: Lenovo
"""

n=int(input())
def j(n):
    l_n=[4,7,44,47,74,77,444,447,474,477,744,747,774,777]
    for i in range(len(l_n)):
        if n%(l_n[i])==0:
            return("YES")
    return("NO")
print(j(n))