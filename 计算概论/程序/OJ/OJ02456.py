# -*- coding: utf-8 -*-
"""
Created on Fri Oct 13 11:29:13 2023

@author: Lenovo
"""

def check(x):
    num,tem=1,l[0]
    for i in range(1,n):
        if l[i]-tem>=x:
            num+=1
            tem=l[i]
        if num>=c:
            return True
    return False

n,c=map(int,input().split())
l=[]
for i in range(n):
    l.append(int(input()))
l.sort()
left,right=0,l[-1]-l[0]
while left<=right:
    mid=(left+right)//2
    if check(mid):
        left=mid+1
    else:
        right=mid-1
print(left-1)