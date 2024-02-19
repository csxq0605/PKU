# -*- coding: utf-8 -*-
"""
Created on Sun Nov 12 14:27:47 2023

@author: Lenovo
"""

def search(n,m):
    i,j=0,ac[n]-m
    if j==1:
        while i<m and a[n][i]==b[i]:
            i+=1
        while i<m and a[n][i+1]==b[i]:
            i+=1
        if i==m:
            return True
    elif j==0:
        while i<m and a[n][i]==b[i]:
            i+=1
        i+=1
        while i<m and a[n][i]==b[i]:
            i+=1
        if i==m:
            return True
    elif j==-1:
        while i<ac[n] and a[n][i]==b[i]:
            i+=1
        while i<ac[n] and a[n][i]==b[i+1]:
            i+=1
        if i==ac[n]:
            return True
    return False

ac,a=[0]*10000,[""]*10000
k=0
while True:
    word=input()
    if word=="#":
        break
    ac[k]=len(word)
    a[k]=word
    k+=1
while True:
    b=input()
    flag=True
    if b=="#":
        break
    for i in range(k):
        if ac[i]==len(b) and a[i]==b:
            print(f"{b} is correct")
            flag=False
            break
    if flag:
        ans=[b+":"]
        for i in range(k):
            if search(i,len(b)):
                ans.append(a[i])
        print(" ".join(ans))