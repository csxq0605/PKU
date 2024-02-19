# -*- coding: utf-8 -*-
"""
Created on Thu Nov 23 16:25:37 2023

@author: Lenovo
"""

from itertools import permutations
import re
num=input()
length=len(num)
flag=0
if length>=7:
    print("YES")
else:
    num="0"*(length-1)+num
    a=permutations(num,r=length)
    for i in list(a):
        j=int("".join(i))
        k=re.search(".*".join(i),num)
        if j%7==0 and k!=None:
            print("YES")
            flag=1
            break
    if not flag:
        print("NO")