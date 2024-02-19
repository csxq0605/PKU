# -*- coding: utf-8 -*-
"""
Created on Sat Oct 28 10:50:44 2023

@author: Lenovo
"""

mod=998244353
n=int(input())
summ=[0]*(n+1)
a=[0]*(n+1)
def add(p,x):
    i=p
    while i<n+1:
        summ[i]+=x
        i+=i&-i

def query(p):
    ans=0
    i=p
    while i:
        ans+=summ[i]
        i-=i&-i
    return ans

ans=0
fac=1
a_input=list(map(int,input().split()))
a[1:n+1]=a_input[::-1]
for i in range(1,n+1):
    tmp=query(a[i])
    ans=(ans+tmp*fac)%mod
    fac=(fac*i)%mod
    add(a[i],1)
print(ans+1)