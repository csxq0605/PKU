# -*- coding: utf-8 -*-
"""
Created on Sun Oct 15 17:22:38 2023

@author: Lenovo
"""

team=[]
n=int(input())
num=0
for i in range(n):
    team.append([int(i) for i in input().split()])
for i in range(n):
    for j in range(n):
        if team[i][0]==team[j][1]:
            num+=1
print(num)