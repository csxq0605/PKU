# -*- coding: utf-8 -*-
"""
Created on Sun Oct 15 17:26:09 2023

@author: Lenovo
"""

n=int(input())
l=[60,90,108,120,135,140,144,150,156,160,162,165,168,170,171,172,174,175,176,177,178,179]
for i in range(n):
    num=int(input())
    print(["NO","YES"][num in l])