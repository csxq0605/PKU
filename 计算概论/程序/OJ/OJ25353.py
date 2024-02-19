# -*- coding: utf-8 -*-
"""
Created on Wed Sep 13 23:43:52 2023

@author: Lenovo
"""

N,D=map(int,input().split())
height=[]
for i in range(N):
    height.append(int(input()))
height_new=[]
while True:
    try:
        tem=[]
        cap=height[0]
        maximun=height[0]
        minimun=height[0]
        for i in height[0::]:
            maximun=max(maximun,i)
            minimun=min(minimun,i)
            if abs(i-maximun)<=D and abs(i-minimun)<=D and 0<=cap-i<=D:
                tem.append(i)
        tem.sort()
        for i in range(len(tem)):
            height.remove(tem[i])
        height_new.extend(tem)
    except IndexError:
        break
for i in height_new:
    print(i)


