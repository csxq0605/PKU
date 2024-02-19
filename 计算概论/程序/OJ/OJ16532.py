# -*- coding: utf-8 -*-
"""
Created on Tue Nov 28 15:52:38 2023

@author: Lenovo
"""

wx,wy=map(int,input().split())
bx,by=map(int,input().split())
dirx,diry=map(int,input().split())
energy=int(input())
bags=[[0,0],[8,0],[16,0],[0,5],[8,5],[16,5]]
flag1=flag2=False
for i in range(energy):
    wx+=dirx
    wy+=diry
    if [wx,wy] in bags:
        flag2=True
        print(1 if flag1 else -1)
        break
    if wx==bx and wy==by:
        flag1=True
    if (wx==0 and dirx==-1)or(wx==16 and dirx==1):
        dirx=-dirx
    if (wy==0 and diry==-1)or(wy==5 and diry==1):
        diry=-diry
if not flag2:
    print(0)