# -*- coding: utf-8 -*-
"""
Created on Sun Oct 15 17:26:39 2023

@author: Lenovo
"""

word=input()
word_new=""
for i in word:
    if 97<=ord(i)<=122:
        word_new+=chr(ord(i)-32)
    elif 65<=ord(i)<=90:
        word_new+=chr(ord(i)+32)
    else:
        word_new+=i
print(word_new)