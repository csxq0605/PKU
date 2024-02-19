# -*- coding: utf-8 -*-
"""
Created on Sun Oct 15 17:22:22 2023

@author: Lenovo
"""

def judge(n):
    if n.upper()==n:
        return n.lower()
    elif n[0].lower()==n[0] and n[1:len(n)].upper()==n[1:len(n)]:
        return n.capitalize()
    else:
        return n

word=input()
print(judge(word))