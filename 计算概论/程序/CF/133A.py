# -*- coding: utf-8 -*-
"""
Created on Thu Sep  7 19:31:31 2023

@author: Lenovo
"""

n=input()
def f(n):
    for i in range(len(n)):
        if n[i]=="H"or n[i]=="Q"or n[i]=="9":
            return "YES"
    return "NO"
print(f(n))