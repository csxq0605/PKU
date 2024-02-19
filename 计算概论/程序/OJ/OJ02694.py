# -*- coding: utf-8 -*-
"""
Created on Mon Oct 16 08:18:20 2023

@author: Lenovo
"""

m=0
def solve():
    global m
    a=l[m]
    m+=1
    if a=='+':
        return solve()+solve()
    elif a=='-':
        return solve()-solve()
    elif a=='*':
        return solve()*solve()
    elif a=='/':
        return solve()/solve()
    else:
        return float(a)

l=[i for i in input().split()]
n=solve()
print("%6f" % n)