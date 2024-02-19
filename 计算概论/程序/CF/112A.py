# -*- coding: utf-8 -*-
"""
Created on Tue Aug 29 12:32:27 2023

@author: Lenovo
"""

s1=input().lower()
s2=input().lower()
for i in range(len(s1)):
    if s1[i]<s2[i]:
        print("-1")
        break
    if s1[i]>s2[i]:
        print("1")
        break
    if i==len(s1)-1:
        print("0")
        