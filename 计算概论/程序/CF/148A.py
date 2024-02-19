# -*- coding: utf-8 -*-
"""
Created on Sun Oct 15 17:20:11 2023

@author: Lenovo
"""

list=[]
for i in range(4):
    list.append(int(input()))
n=int(input())
num=set()
for i in range(4):
    shu=list[i]
    former=list[i]
    while shu<=n :
        num.add(shu)
        shu+=former
print(len(num))