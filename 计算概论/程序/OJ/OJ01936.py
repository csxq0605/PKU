# -*- coding: utf-8 -*-
"""
Created on Wed Sep 20 19:22:20 2023

@author: Lenovo
"""


def check(a,b):
    for l in b:
       if l==a[0]:
           del a[0]
       if len(a)==0 :
           return "Yes"
    return "No"
while True:
    try:       
        a,b=map(list,input().split())
        print(check(a,b))
    except:
        break
