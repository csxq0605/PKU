# -*- coding: utf-8 -*-
"""
Created on Sun Oct 15 17:35:16 2023

@author: Lenovo
"""

def generateParenthesis(n):
    s = set(['()'])
    for i in range(2, n+1):
        nextSet = set()
        for p in s:
            for j in range(len(p)):
                nextSet.add(p[:j] + '()' + p[j:])
        s = nextSet
    return list(s)

n=int(input())
line=sorted(generateParenthesis(n))
for i in line:
    print(i)