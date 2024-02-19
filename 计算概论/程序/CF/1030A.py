# -*- coding: utf-8 -*-
"""
Created on Thu Sep  7 19:09:06 2023

@author: Lenovo
"""

n=int(input())
list=input().split()
def j(n):
    for i in range(n):
        if list[i]=="1":
            return "HARD"
    return "EASY"
print(j(n))