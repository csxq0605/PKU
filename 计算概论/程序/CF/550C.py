# -*- coding: utf-8 -*-
"""
Created on Wed Nov 22 09:00:14 2023

@author: Lenovo
"""

def check(n):
    l=len(n)   
    for i in range(l-1,-1,-1):
        if int(n[i])%8==0:
            print("YES")
            return n[i]
        elif int(n[i])%2==0:
            for j in range(i-1,-1,-1):
                if int(n[j]+n[i])%8==0:
                    print("YES")
                    return n[j]+n[i]
                elif int(n[j]+n[i])%4==0:
                    for k in range(j-1,-1,-1):
                        if int(n[k]+n[j]+n[i])%8==0:
                            print("YES")
                            return n[k]+n[j]+n[i]
    return "NO"

n=input()
print(check(n))