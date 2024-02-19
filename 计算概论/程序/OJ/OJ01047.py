# -*- coding: utf-8 -*-
"""
Created on Sun Oct 15 17:33:41 2023

@author: Lenovo
"""

number=[]
while True:
    try:
        number.append(str(input()))
    except:
        break
for num in number:
    if str(int(num)*(len(num)+1))=="9"*len(num):
        print(f'{num} is cyclic')
    else:
        print(f'{num} is not cyclic')