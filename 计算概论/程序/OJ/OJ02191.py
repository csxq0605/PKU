# -*- coding: utf-8 -*-
"""
Created on Tue Oct 31 10:44:37 2023

@author: Lenovo
"""

import random
prime,p,num,yz=[],[],0,[]

def init():
    global prime,p,cnt
    prime=[True]*65
    cnt=0
    for i in range(2,64):
        if prime[i]:
            p.append(i)
            cnt+=1
            for j in range(i*i,64,i):
                prime[j]=False

def mul(x,y,mod):
    ans=0
    while y:
        if y&1:
            ans=(ans+x)%mod
        x=(x+x)%mod
        y>>=1
    return ans

def poww(x,y,mod):
    ans=1
    while y:
        if y&1:
            ans=mul(ans,x,mod)
        x=mul(x,x,mod)
        y>>=1
    return ans

def miller_rabin(n):
    if n==2:
        return True
    if n==1 or not n&1:
        return False
    t,u=0,n-1
    while not u&1:
        t+=1
        u>>=1
    for i in range(10):
        a=random.randint(1,n-1)
        x=poww(a,u,n)
        for j in range(0,t):
            y=mul(x,x,n)
            if y==1 and x!=1 and x!=n-1:
                return False
            x=y
        if x!=1:
            return False
    return True

def gcd(a,b):
    if a<0:
        return gcd(-a,b)
    if a==0:
        return 1
    while b:
        t=a%b
        a=b
        b=t
    return a

def Pollard_rho(n,c):
    i,k=1,2
    x=random.randint(1,n-1)
    y=x
    while True:
        i+=1
        x=(mul(x,x,n)+c)%n
        p=gcd(y-x,n)
        if p!=1 and p!=n:
            return p
        if y==x:
            return n
        if i==k:
            y=x
            k+=k

def findx(n):
    global num,yz
    if n==1:
        return
    if miller_rabin(n):
        yz.append(n)
        num+=1
        return
    p=n
    while p>=n:
        p=Pollard_rho(p,random.randint(1,n-1))
    findx(p)
    findx(n//p)

init()
k=int(input())
for i in range(cnt):
    if p[i]<k:
        kk=(1<<p[i])-1
        if not miller_rabin(kk):
            num=0
            findx(kk)
            yz.sort()
            print(yz[0],end="")
            for j in range(1,num):
                print(" *",yz[j],end="")
            print(" = {} = ( 2 ^ {} ) - 1".format(kk,p[i]))
            yz=[]