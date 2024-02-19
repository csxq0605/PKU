# -*- coding: utf-8 -*-
"""
Created on Sun Oct 15 17:21:55 2023

@author: Lenovo
"""

l=set(input())
l.discard("{")
l.discard("}")
l.discard(",")
l.discard(" ")
print(len(l))