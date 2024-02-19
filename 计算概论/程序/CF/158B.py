# -*- coding: utf-8 -*-
"""
Created on Sun Oct 15 17:21:31 2023

@author: Lenovo
"""

n=int(input())
l=[int(i) for i in input().split()]
print(l.count(4)+l.count(3)+(l.count(2)*2+max(0,l.count(1)-l.count(3))+3)//4)