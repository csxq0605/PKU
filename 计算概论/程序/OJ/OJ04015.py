# -*- coding: utf-8 -*-
"""
Created on Tue Sep 19 23:29:13 2023

@author: Lenovo
"""

def check(email):
    if len(email)!=2:
        return "NO"
    elif email[0]=="" or email[1]=="":
        return "NO"
    elif email[0][0]=="." or email[0][-1]==".":
        return "NO"
    else:
        last=sorted(email[1].split("."))
        if last[0]=="" or len(last)==1:
            return "NO"
        else:
            return "YES"
l=[]
while True:
    try:
        email=input().split("@")
        l.append(check(email))
    except:
        break
for i in l:    
    print(i)