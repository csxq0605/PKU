# -*- coding: utf-8 -*-
"""
Created on Sun Oct 15 17:42:28 2023

@author: Lenovo
"""

def check(a,b):
    ans=0
    l1,r1=0,len(a)-1
    l2,r2=0,len(b)-1
    while l1<=r1 and l2<=r2:
        if b[r2]>a[r1]:
            r2-=1
            r1-=1
            ans+=200
        elif b[l2]>a[l1]:
            l1+=1
            l2+=1
            ans+=200
        elif b[l2]==a[r1]:
            l2+=1
            r1-=1
            ans+=0
        else:
            r1-=1
            l2+=1
            ans-=200
    return ans

while True:
    n=int(input())
    if n==0:
        break
    tian=list(map(int,input().split()))
    king=list(map(int,input().split()))
    tian.sort()
    king.sort()
    maxi=check(king,tian)
    print(maxi)