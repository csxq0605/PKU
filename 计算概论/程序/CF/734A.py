# -*- coding: utf-8 -*-
"""
Created on Thu Sep  7 19:07:05 2023

@author: Lenovo
"""

n=int(input())
line=input()
A,D=0,0
for i in range(n):
    if line[i]=="A":
        A+=1
    elif  line[i]=="D":
        D+=1
if A>D:
    print("Anton")
elif A<D:
    print("Danik")
elif A==D:
    print("Friendship")