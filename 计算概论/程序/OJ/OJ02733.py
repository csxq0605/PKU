# -*- coding: utf-8 -*-
"""
Created on Sun Oct 15 17:28:12 2023

@author: Lenovo
"""

year=int(input())
if year%4==0:
    if year%100==0:
        if year%400==0:
            print("Y")
        else:
            print("N")
    else:
        print("Y")
else:
    print("N")