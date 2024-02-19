# -*- coding: utf-8 -*-
"""
Created on Tue Oct 24 16:25:54 2023

@author: Lenovo
"""

def game():
    input()
    l=[int(i) for i in input().split()]
    s=filter(lambda x:x<=2048,l)
    if sum(s)>=2048:    
        return "YES"
    else:
        return "NO"

q=int(input())
for _ in range(q):
    print(game())