# -*- coding: utf-8 -*-
"""
Created on Sun Oct 15 17:19:51 2023

@author: Lenovo
"""

n=int(input())
word=input().lower()
letters=[]
for i in range(26):
    letters.append(chr(i+97))
for i in range(n):
    if word[i] in letters:
        letters.remove(word[i])
if len(letters)==0:
    print("YES")
else:
    print("NO")