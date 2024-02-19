# -*- coding: utf-8 -*-
"""
Created on Sun Dec 24 23:34:41 2023

@author: Lenovo
"""

MAXN=1001
n,m,k=map(int,input().split())
d=[0]+list(map(int,input().split()))
t,a,b=[0]*(MAXN*10),[0]*(MAXN*10),[0]*(MAXN*10)
num,last,arr,sum_arr=[0]*MAXN,[0]*MAXN,[0]*MAXN,[0]*MAXN
for i in range(1,m+1):
    t[i],a[i],b[i]=map(int,input().split())
for i in range(1,m+1):
    num[b[i]]+=1
    last[a[i]]=max(last[a[i]],t[i])
for i in range(2,n+1):
    arr[i]=max(arr[i-1],last[i-1])+d[i-1]
ans=0
for i in range(1,m+1):
    ans+=arr[b[i]]-t[i]
while k>0:
    p,temp=-1,-1
    for i in range(n-1,0,-1):
        if arr[i+1]<=last[i+1]:
            sum_arr[i]=num[i+1]
        else:
            sum_arr[i]=sum_arr[i+1]+num[i+1]
        if sum_arr[i]>temp and d[i]:
            temp=sum_arr[i]
            p=i
    if p==-1:
        break
    ans-=temp
    d[p]-=1
    for i in range(p+1,n+1):
        arr[i]=max(arr[i-1],last[i-1])+d[i-1]
    k-=1
print(ans)