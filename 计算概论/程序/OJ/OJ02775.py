# -*- coding: utf-8 -*-
"""
Created on Mon Oct 16 08:54:35 2023

@author: Lenovo
"""

n=1
flag=True
s=""
def printkg(level):
    for _ in range(level):
        print("|     ",end="")

def pf(level):
    global flag
    global s
    file_set=set()
    while True:
        if s!="":
            str_input=s
            s=""
        else:    
            str_input=input().strip()
        if str_input.startswith('f'):
            file_set.add(str_input)
        elif str_input.startswith('d'):
            printkg(level)
            print(str_input)
            pf(level+1)
        elif str_input==']':
            for file in sorted(file_set):
                printkg(level-1)
                print(file)
            return
        elif str_input=='*':
            for file in sorted(file_set):
                print(file)
            s=input()
            if s=="#":
                flag=False
            return

while flag:
    print(f"DATA SET {n}:")
    print("ROOT")
    pf(1)
    n+=1
    print()