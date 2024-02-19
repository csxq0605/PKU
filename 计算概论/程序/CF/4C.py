# -*- coding: utf-8 -*-
"""
Created on Sun Oct 15 17:24:43 2023

@author: Lenovo
"""

n=int(input())
database={}
for i in range(n):
    name=input()
    print(name+str(database[name]) if database.setdefault(name,0) else "OK")
    database[name]+=1