# -*- coding: utf-8 -*-
"""
Created on Thu Nov  2 09:06:48 2023

@author: Lenovo
"""

while True:
    try:
        a=input()
        ans=[" "]*len(a)
        stack,ps=[""]*len(a),0
        for i in range(len(a)):
            if a[i]=="(":
                stack[ps]=i
                ps+=1
            elif a[i]==")":
                if (ps):
                    ps-=1
                else:
                    ans[i]="?"
        for _ in range(ps):
            ans[stack[_]]="$"
        print(a)
        print("".join(ans))
    except EOFError:
        break