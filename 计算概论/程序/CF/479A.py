# -*- coding: utf-8 -*-
"""
Created on Sun Oct 15 17:19:01 2023

@author: Lenovo
"""

a=int(input())
b=int(input())
c=int(input())
list=[]
list.append(a+b+c)
list.append(a*b+c)
list.append(a+b*c)
list.append(a*b*c)
list.append((a+b)*c)
list.append(a*(b+c))
list.sort()
print(list[len(list)-1])