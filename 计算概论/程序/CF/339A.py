# -*- coding: utf-8 -*-
"""
Created on Tue Aug 29 12:49:33 2023

@author: Lenovo
"""

list=input().split("+")
list1=[str(i) for i in list]
list1.sort(reverse=False)
list2=""
for i in range(len(list1)-1):
    list2+=list1[i]+"+"
list2+=list1[len(list1)-1]
print(list2)
