# -*- coding: utf-8 -*-
"""
Created on Thu Nov 30 22:09:51 2023

@author: Lenovo
"""

m,n=map(int,input().split())
seats=[[-1]*(n+2)]+[[-1]+list(map(int,input().split()))+[-1] for i in range(m)]+[[-1]*(n+2)]
scores=[list(map(int,input().split())) for i in range(m*n)]
num=0
for i in range(1,m+1):
    for j in range(1,n+1):
        seat=seats[i][j]
        for around in [seats[i-1][j],seats[i+1][j],seats[i][j+1],seats[i][j-1]]:
            if around!=-1 and scores[around]==scores[seat]:
                num+=1
                break
l=[sum(x) for x in scores]
l.sort(reverse=True)
ans=[x>l[int(m*n*0.4)] for x in l]
print(num,ans.count(True))