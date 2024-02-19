# -*- coding: utf-8 -*-
"""
Created on Tue Nov 21 15:31:39 2023

@author: Lenovo
"""

while True:
    n,m=map(int,input().split())
    if n==0 and m==0:
        break
    f=[False]*(m+1)
    l=list(map(int,input().split()))
    c=[0]+l[0:n]
    num=[0]+l[n:]
    used=[0]*(n+1)
    f[0]=True
    for i in range(1,n+1):
        used[0:m+1]=[0]*(m+1)
        for j in range(c[i],m+1):
            if not f[j] and f[j-c[i]] and used[j-c[i]]<num[i]:
                f[j]=True
                used[j]=used[j-c[i]]+1
    ans=sum(f[1:m+1])
    print(ans)

while True:
    n,m=map(int,input().split())
    if n==0 and m==0:
        break
    f=[False]*(m+1)
    l=list(map(int,input().split()))
    c=[0]+l[0:n]
    num=[0]+l[n:]
    used=[0]*(n+1)
    f[0]=True    
    for i in range(1,n+1):
        j=1
        while j<num[i]:
            num[i]-=j
            k=m
            while k>=0:
                if k>=j*c[i]:
                    f[k]|=f[k-j*c[i]]
                k-=1
            j<<=1
        if num[i]:
            k=m
            while k>=0:
                if k>=c[i]*num[i]:
                    f[k]|=f[k-num[i]*c[i]]
                k-=1
    ans=sum(f[1:m+1])
    print(ans)