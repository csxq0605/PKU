# -*- coding: utf-8 -*-
"""
Created on Sat Oct  7 11:06:37 2023

@author: Lenovo
"""

s="`1234567890-=QWERTYUIOP[]\ASDFGHJKL;'ZXCVBNM,./"
while True:
    try:
        line=input()
        for i in line:
            if i in s:
                print(s[s.index(i)-1],end="")
            else:
                print(i,end="")
        print()
    except:
        break