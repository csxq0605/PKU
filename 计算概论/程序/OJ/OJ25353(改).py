# -*- coding: utf-8 -*-
"""
Created on Wed Sep 13 23:43:52 2023

@author: Lenovo
"""

N,D=map(int,input().split())
height=[]
check=[]
for i in range(N):
    height.append(int(input()))
    check.append(0)
height_new=[]
while True:
    if not(0 in check):
        break
    try:
        i,l=0,len(height)
        tem=[]
        while i<l:
            if check[i]:
                i+=1
                continue
            if not tem:
                tem=[height[i]]
                maximun=height[i]
                minimun=height[i]
                check[i]+=1
                continue
            maximun=max(maximun,i)
            minimun=min(minimun,i)
            if maximun-height[i]<=D and height[i]-minimun<=D:
                tem.append(height[i])
                check[i]+=1
            i+=1
        tem.sort()
        height_new.extend(tem)
    except IndexError:
        break
for i in height_new:
    print(i)