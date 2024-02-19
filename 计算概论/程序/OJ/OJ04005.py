# -*- coding: utf-8 -*-
"""
Created on Tue Oct 10 11:43:17 2023

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
            ans+=3
        elif b[l2]>a[l1]:
            l1+=1
            l2+=1
            ans+=3
        elif b[l2]==a[r1]:
            l2+=1
            r1-=1
            ans+=2
        else:
            r1-=1
            l2+=1
            ans+=1
    return ans

while True:
    n=int(input())
    if n==0:
        break
    c=list(map(int,input().split()))
    s=list(map(int,input().split()))
    c.sort()
    s.sort()
    maxi=check(c,s)
    mini=n*4-check(s,c)
    print(maxi,mini)