# -*- coding: utf-8 -*-
"""
Created on Fri Dec 22 11:02:05 2023

@author: Lenovo
"""

def work(x,y):
    i,j,ans=1,n,0
    while i<min(x,y) and j>max(x,y):    #确定所在层
        ans+=(j-i)*4
        i+=1
        j-=1
    a=b=i
    ans+=1
    if i==j:
        return ans
    while a<j and b<=j:                #开始对层扫描，先右移后下移
        if a==x and b==y:
            return ans
        if b<j:
            b+=1
            ans+=1
        else:
            a+=1
            ans+=1
    while a>i and b>=i:               #在左移后上移，把层扫描完直到找到
        if a==x and b==y:
            return ans
        if b>i:
            b-=1
            ans+=1
        else:
            a-=1
            ans+=1
    return ans

k,n=map(int,input().split())
for _ in range(k):
    x,y=map(int,input().split())
    print(work(x,y))