# -*- coding: utf-8 -*-
"""
Created on Tue Aug 29 13:39:31 2023

@author: Lenovo
"""

word=input().lower()
list=[]
vowels=["a","e","i","o","u","y"]
word1=""
for i in range(len(word)):
    list.append(word[i])
for i in range(len(list)):
    if list[i] not in vowels:
        word1+="."+list[i]
print(word1)