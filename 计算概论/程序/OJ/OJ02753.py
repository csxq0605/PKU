# -*- coding: utf-8 -*-
"""
Created on Fri Oct  6 13:53:01 2023

@author: Lenovo
"""

n=int(input())
list=[1,1,2,3,5,8,13,21,34,55,89,144,233,377,610,987,1597,2584,4181,6765]
for i in range(n):
    num=int(input())
    print(list[num-1])