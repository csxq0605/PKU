# -*- coding: utf-8 -*-
"""
Created on Wed Dec 27 15:23:27 2023

@author: Lenovo
"""

dic=dict(zip(list("ABCDEFGHIJKLMNOPQRSTUVWXYZ"),[0]*26))
for i in range(4):
    s=input()
    for j in s:
        if "A"<=j<="Z":
            dic[j]+=1
maxn=max(dic.values())
l=sorted(dic.items())
ans=[["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]]+[[]for i in range(maxn)]
for i in range(1,maxn+1):
    for j,k in l:
        if j<"A" or j>"Z":
            continue
        if k>=i:
            ans[i].append("*")
        else:
            ans[i].append(" ")
for i in ans[::-1]:
    print(" ".join(i))