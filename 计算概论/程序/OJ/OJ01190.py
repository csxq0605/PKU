# -*- coding: utf-8 -*-
"""
Created on Mon Oct 23 09:14:02 2023

@author: Lenovo
"""

import math

V=int(input())
N=int(input())
sumMinS=[0]*27
sumMinV=[0]*27
minsurArea=float('inf')

def dfs(ifloor,preR,preH,leftV,surArea):
    global minsurArea,N,sumMinS,sumMinV
    if ifloor==0:
        if leftV==0 and surArea<minsurArea:
            minsurArea=surArea
        return
    if preR>1 and 2*leftV/(preR-1)+surArea>=minsurArea: 
        return
    if leftV<sumMinV[ifloor]:  
        return
    if surArea+sumMinS[ifloor]>=minsurArea: 
        return
    for r in range(preR-1,ifloor-1,-1):
        if ifloor==N: 
            surArea=r*r
        H_max=int(leftV/(r*r)+1)
        if H_max>preH-1: 
            H_max=preH-1   
        for h in range(H_max,ifloor-1,-1):
            dfs(ifloor-1,r,h,leftV-r*r*h,surArea+2*r*h)
    return


for i in range(1,N+1):
    sumMinS[i]=sumMinS[i-1]+2*i*i
    sumMinV[i]=sumMinV[i-1]+i*i*i
maxH=int((V-sumMinV[N-1])/(N*N)+1)
maxR=int(math.sqrt((V-sumMinV[N-1])+1))
dfs(N,maxR,maxH,V,0)
if minsurArea==float('inf'):
    print(0)
else:
    print(minsurArea)