# -*- coding: utf-8 -*-
"""
Created on Sat Sep 16 12:07:24 2023

@author: Lenovo
"""

def calc(ropes,mid):
    number = 0
    for i in ropes:
        number += i//mid
    if number < k:
        x = 0
    else:
        x = 1
    return x

def find(ropes,minl,maxl):
    mid = (minl+maxl)//2
    x = calc(ropes, mid)
    if x:
        minl = mid
    else:
        maxl = mid
    if maxl-minl>1:
        maxl = find(ropes, minl, maxl)
    return maxl

n,k= map(int,input().split())
ropes = []
total = 0
for i in range(n):
    rope = int(float(input())*100)
    ropes.append(rope)
    total += rope
minl = 1
maxl = (total//(k*100)+1)*100
if total < k:
    print("0.00")
else:
    out = find(ropes, minl, maxl)
    if calc(ropes, out) == 0:
        out -= 1
    answer = out/100
    print('%.2f'%answer)