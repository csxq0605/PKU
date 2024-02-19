# -*- coding: utf-8 -*-
"""
Created on Thu Sep 28 20:41:25 2023

@author: Lenovo
"""

n1="- -- -----"
n2="|   ||| ||"
n3="|||||  |||"
n4="  ----- --"
n5="| |   | | "
n6="|| |||||||"
n7="- -- -- --"
while True:    
    s,num=map(int,input().split())
    if s==0 and num==0:
        break
    num=[int(i) for i in str(num)]
    for i in num:
        print(" ",end="")
        for j in range(s):
            print(n1[i],end="")
        print("  ",end="")
    print()
    for i in range(s):
        for i in num:
            print(n2[i],end="")
            for k in range(s):
                print(" ",end="")
            print(n3[i],end="")
            print(" ",end="")
        print()
    for i in num:
        print(" ",end="")
        for j in range(s):
            print(n4[i],end="")
        print("  ",end="")
    print()
    for i in range(s):
        for i in num:
            print(n5[i],end="")
            for k in range(s):
                print(" ",end="")
            print(n6[i],end="")
            print(" ",end="")
        print()
    for i in num:
        print(" ",end="")
        for j in range(s):
            print(n7[i],end="")
        print("  ",end="")
    print()
    print()