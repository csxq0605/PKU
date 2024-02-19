# -*- coding: utf-8 -*-
"""
Created on Sat Dec  9 00:15:39 2023

@author: Lenovo
"""

while True:
    try:
        check=[0]*10
        l=input()
        for i in l:
            if ord("0")<=ord(i)<=ord("9"):
                check[int(i)]+=1
        for i in range(10):
            if check[i]:
                print(f"{i}:{check[i]}")
    except EOFError:
        break