# -*- coding: utf-8 -*-
"""
Created on Sun Dec 10 00:47:17 2023

@author: Lenovo
"""

from itertools import permutations
l=input()
li=list(permutations(l,r=len(l)))
li.sort()
for i in li:
    print("".join(list(i)))