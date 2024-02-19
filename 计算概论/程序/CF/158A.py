# -*- coding: utf-8 -*-
"""
Created on Tue Aug 29 11:51:16 2023

@author: Lenovo
"""

n,k=map(int,input().split())
score=[int(i)for i in input().split()]
num=0
k_score=score[k-1]
for i in range(n):
    if score[i]>=k_score and score[i]>0:
        num+=1
    else:
        break
print(num)