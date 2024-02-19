# -*- coding: utf-8 -*-
"""
Created on Tue Aug 29 13:33:28 2023

@author: Lenovo
"""

num=0
letters=[]
name=input()
for i in range(len(name)):
    if name[i] not in letters:
        num+=1
        letters.append(name[i])
if num%2==0:
    print("CHAT WITH HER!")
else:
    print("IGNORE HIM!")