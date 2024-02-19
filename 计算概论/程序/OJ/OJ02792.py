# -*- coding: utf-8 -*-
"""
Created on Sun Nov 19 11:58:49 2023

@author: Lenovo
"""

for _ in range(int(input())):
    A=[0]*10001
    B=[0]*10001
    C=[0]*10001
    s=int(input())
    a=int(input())
    k=ans=0
    la=list(map(int,input().split()))
    for tmp in la:
        if A[tmp]==0:
            C[k]=tmp
            k+=1
            A[tmp]+=1
        else:
            A[tmp]+=1
    b=int(input())
    lb=list(map(int,input().split()))
    for tmp in lb:
        B[tmp]+=1
    for i in range(k):
        if s-C[i]>0:
            ans+=A[C[i]]*B[s-C[i]]
    print(ans)