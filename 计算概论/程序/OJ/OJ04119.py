# -*- coding: utf-8 -*-
"""
Created on Thu Oct 19 13:12:08 2023

@author: Lenovo
"""

def test1(n,k):
    dp1=[[0]*51 for _ in range(51)]
    dp1[0][0]=1
    for i in range(1,n+1):
        for j in range(1,i+1):
            if i==j:
                dp1[i][j]=1  
            else:
                dp1[i][j]=dp1[i-1][j-1]+dp1[i-j][j]
    print(dp1[n][k])

def test2(n):
    dp2=[[0]*51 for _ in range(51)]
    dp2[0][0]=1
    for i in range(1,n+1):
        for j in range(1,n+1):
            if i==j:
                dp2[i][j]=dp2[i][j-1]+1
            elif j>i:
                dp2[i][j]=dp2[i][i]
            else:
                dp2[i][j]=dp2[i-j][j-1]+dp2[i][j-1]
    print(dp2[n][n])

def test3(n):
    dp3=[[0]*51 for _ in range(51)]
    dp3[0][0]=1
    for i in range(1,n+1):
        for j in range(1,n+1):
            if j % 2==0:
                dp3[i][j]=dp3[i][j-1]
            else:
                if i<j:
                    dp3[i][j]=dp3[i][i]
                elif i==j:
                    dp3[i][j]=dp3[i][j-1]+1
                else:
                    dp3[i][j]=dp3[i-j][j]+dp3[i][j-1]
    print(dp3[n][n])

while True:
    try:
        n,k=map(int,input().split())
        test1(n,k)
        test2(n)
        test3(n)
    except:
        break