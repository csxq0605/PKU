# -*- coding: utf-8 -*-
"""
Created on Thu Oct 19 13:02:43 2023

@author: Lenovo
"""

def split(n,m):
    if n==1 or m==1:
        return 1
    elif n<m:
        return split(n,n)
    elif n==m:
        return split(n,n-1)+1
    elif n>m:
        return split(n,m-1)+split(n-m,m)

while True:
    try:
        n=int(input())
        print(split(n,n))
    except:
        break

l=[1,1,2,3,5,7,11,15,22,30,42,56,77,101,135,176,231,
 297,385,490,627,792,1002,1255,1575,1958,2436,3010,
 3718,4565,5604,6842,8349,10143,12310,14883,17977,
 21637,26015,31185,37338,44583,53174,63261,75175,
 89134,105558,124754,147273,173525,204226]