# -*- coding: utf-8 -*-
"""
Created on Sun Oct 15 17:24:06 2023

@author: Lenovo
"""

guest=input()
host=input()
letters=[i for i in input()]

def judge(guest,host,letters):
    for i in guest:
        if i in letters:
            letters.remove(i)
        else:
            return("NO")
    for i in host:
        if i in letters:
            letters.remove(i)
        else:
            return("NO")
    if len(letters)==0:
        return("YES")
    else:
        return("NO")

print(judge(guest,host,letters))