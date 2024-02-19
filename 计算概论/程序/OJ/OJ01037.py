# -*- coding: utf-8 -*-
"""
Created on Tue Oct 24 15:29:57 2023

@author: Lenovo
"""

t=int(input())
for _ in range(t):
    n,c=map(int,input().split())
    dp=[[[0,0] for _ in range(n+1)] for _ in range(n+1)]
    dp[1][1][0]=dp[1][1][1]=1 
    for i in range(2,n+1):
        for j in range(1,i+1):
            for k in range(j,i):
                dp[i][j][0]+=dp[i-1][k][1]
            for k in range(1,j):
                dp[i][j][1]+=dp[i-1][k][0]
    res,visited=[0]*(n+1),[0]*(n+1)
    s=0
    for cur in range(1,n+1):
        no=0
        for i in range(1,n+1):
            if not visited[i]:
                no+=1
                num=0
                if cur==1:
                    num=dp[n][no][0]+dp[n][no][1]
                else:
                    if (i>res[cur-1]) and (cur<=2 or res[cur-2]>res[cur-1]):
                        num+=dp[n-cur+1][no][1]
                    elif (i<res[cur-1]) and (cur<=2 or res[cur-2]<res[cur-1]):
                        num+=dp[n-cur+1][no][0]
                s+=num
                if s>=c:
                    s-=num
                    res[cur]=i
                    visited[i]=1
                    break
        else:
            break
    print(*res[1:n+1])