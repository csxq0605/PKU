# -*- coding: utf-8 -*-
"""
Created on Sun Nov 12 13:50:36 2023

@author: Lenovo
"""

while True:
    n=int(input())
    if n==0:
        break
    b=[0]+list(map(int,input().split()))
    a=[0]*(n+1)
    for i in range(1,n+1):
        a[b[i]]=i
    x=[0]*(n+1)
    for i in range(1,n+1):
        j,k=i,0
        while True:
            k=a[j]
            if a[i]==a[k]:
                x[i]+=1
                break
            else:
                j=k
                k=a[j]
                x[i]+=1
    while True:
        input_=input()
        index=input_.find(" ")
        if index==-1:
            break
        num,string=int(input_[:index]),input_[index+1:]
        if len(string)<n:
            for i in range(n-len(string)):    
                string+=" "
        ss=[""]*(n+1)
        for i in range(1,n+1):
            cnt=i
            for j in range(1,num%x[i]+1):
                cnt=b[cnt]
            ss[cnt-1]=string[i-1]
        print("".join(ss[:n]))
    print()