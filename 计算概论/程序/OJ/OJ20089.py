# -*- coding: utf-8 -*-
"""
Created on Sun Nov 26 00:03:11 2023

@author: Lenovo
"""

n=int(input())
ticket=list(map(int,input().split()))
cost=[50,100,250,500,1000,2500,5000]
choice,dic={0:0},{0:[0,0,0,0,0,0,0]}
for i in range(n):
    if i in choice:
        for k in range(7):
            if dic[i][k]<ticket[k]:
                if i+cost[k] in choice:
                    if choice[i]+1<choice[i+cost[k]]:
                        choice[i+cost[k]]=choice[i]+1
                        dic[i+cost[k]]=dic[i][0::]
                        dic[i+cost[k]][k]+=1
                else:
                    choice[i+cost[k]]=choice[i]+1
                    dic[i+cost[k]]=dic[i][0::]
                    dic[i+cost[k]][k]+=1
print(choice[n] if n in choice else "Fail")