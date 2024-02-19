# -*- coding: utf-8 -*-
"""
Created on Mon Oct 30 20:48:19 2023

@author: Lenovo
"""

hang=[0]*8
ans=[[0]*8 for _ in range(92)]
num=0
def queen(n):
    global num
    if n==8:
        for i in range(8):
            ans[num][i]=hang[i]+1
        num+=1
        return
    for i in range(8):
        for j in range(n):
            if i==hang[j] or (j-n)==hang[j]-i or (n-j)==hang[j]-i:
                break
        else:
            hang[n]=i
            queen(n+1)
queen(0)
n=int(input())
for _ in range(n):
    b=int(input())
    for i in range(8):
        print(ans[b-1][i],end="")
    print()