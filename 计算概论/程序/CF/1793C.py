# -*- coding: utf-8 -*-
"""
Created on Tue Oct 24 10:50:31 2023

@author: Lenovo
"""
  
def check():
    n=int(input())
    l=[int(i) for i in input().split()]
    i,j,k,m=0,n-1,1,n
    while j-i>1:
        if l[i]==k:
            i+=1
            k+=1
        elif l[i]==m:
            i+=1
            m-=1
        elif l[j]==k:
            j-=1
            k+=1
        elif l[j]==m:
            j-=1
            m-=1
        else:
            return i+1,j+1
    return -1,-1

t=int(input())
for i in range(t):
    a1,a2=check()
    if a1==-1:
        print(-1)
    else:
        print(a1,a2)