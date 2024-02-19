# -*- coding: utf-8 -*-
"""
Created on Fri Dec  8 10:39:03 2023

@author: Lenovo
"""

while True:
    try:
        line=list(map(int,input().split()))
        linenew=sorted(line)
        if line==linenew:
            print("Yes")
        else:
            print("No",*linenew)
    except EOFError:
        break