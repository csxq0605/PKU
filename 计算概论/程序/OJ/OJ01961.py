# -*- coding: utf-8 -*-
"""
Created on Fri Sep 22 20:50:17 2023

@author: Lenovo
"""
num=1
while True:
    n=int(input().strip())
    if n==0:
        break
    s=input().strip()
    Next=[0]*(n+1)
    Next[0]=-1
    Next[1]=0
    for i in range(2,n+1):
        t=Next[i-1]
        while(t>=0 and s[i-1]!=s[t]):
            t=Next[t]
        Next[i]=t+1
    print('Test case #%d' % num)
    num+=1
    for i in range(2,n+1):
        if i%(i-Next[i])==0 and Next[i]!=0:
            print('%d %d' % (i,i//(i-Next[i])))
    print()
