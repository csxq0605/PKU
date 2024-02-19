# -*- coding: utf-8 -*-
"""
Created on Sun Oct  8 12:08:22 2023

@author: Lenovo
"""

def check(j):
    k=1
    while k<=length[j]:
        ans=a[j][:k]
        l,flag=0,True
        while l<len(a) and flag:
            if l!=j:
                if a[l].startswith(ans):
                    flag=False
            l+=1
        if flag:
            return a[j],ans
        k+=1
    return a[j],a[j]

a=[]
length=[]
while True:
    try:
        s=input()
        a.append(s)
        length.append(len(s))
    except EOFError:
        break
for j in range(len(a)):
    c,b=map(str,check(j))
    print(c,b)