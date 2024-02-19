# -*- coding: utf-8 -*-
"""
Created on Tue Aug 29 21:21:51 2023

@author: Lenovo
"""


word=[c for c in input().lower()]
letters=["h","e","l","l","o"]
s=""
j=0
for i in range(len(word)):
    if word[i]==letters[0]:
        s+=word[i]
        letters.remove(letters[0])
        j+=1
    if j==5:
        break
if s=="hello":
    print("YES")
else:
    print("NO")