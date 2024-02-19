# -*- coding: utf-8 -*-
"""
Created on Sun Oct 15 17:28:30 2023

@author: Lenovo
"""

num=int(input())
if num%2==0:
    maxi=num//2
    mini=num//4+num%4//2
else:
    maxi=0
    mini=0
print(str(mini)+" "+str(maxi))