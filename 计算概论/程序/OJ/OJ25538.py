# -*- coding: utf-8 -*-
"""
Created on Wed Nov 22 22:26:32 2023

@author: Lenovo
"""

num=bin(int(input()))[2:]
print("Yes" if num==num[::-1] else "No")