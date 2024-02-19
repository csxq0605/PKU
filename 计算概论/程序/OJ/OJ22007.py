# -*- coding: utf-8 -*-
"""
Created on Wed Dec 13 09:37:28 2023

@author: Lenovo
"""

def isvalid(former,row,col):
    for i in range(row):
        if former[i]==col or abs(i-row)==abs(former[i]-col):
            return False
    return True

def queen(former=[],row=0):
    if row==n:
        result.append(former[:])
        return
    for col in range(n):
        if isvalid(former,row,col):
            former.append(col)
            queen(former,row+1)
            former.pop()

n=int(input())
result=[]
queen()
if result:
    for i in result:
        print(*i)
else:
    print("NO ANSWER")