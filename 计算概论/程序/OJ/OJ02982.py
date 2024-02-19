# -*- coding: utf-8 -*-
"""
Created on Fri Dec 15 16:10:43 2023

@author: Lenovo
"""

def ok(n,cur,num):    #是否合法
    r=n//9
    c=n%9
    for j in range(9):     #列合法
        if num[r][j]==cur:
            return False
    for i in range(9):     #行合法
        if num[i][c]==cur:
            return False
    x=r//3*3
    y=c//3*3
    for i in range(x,x+3):     #三角块合法
        for j in range(y,y+3):
            if num[i][j]==cur:
                return False
    return True

def DFS(n,num,flag):
    if n>80 or flag[0]:
        flag[0]=True
        return
    if num[n//9][n%9]:    #当前有数字，直接下一位
        DFS(n+1,num,flag)
        if flag[0]:
            return
    else:
        for cur in range(1,10):     #枚举合法数字
            if ok(n,cur,num):
                num[n//9][n%9]=cur      #合法插入
                DFS(n+1,num,flag)
                if flag[0]:
                    return
                num[n//9][n%9]=0        #还原

for _ in range(int(input())):
    flag=[False]
    num=[[0]*9 for _ in range(9)]
    for i in range(9):
        s=input()
        for j in range(9):
            num[i][j]=int(s[j])
    DFS(0,num,flag)
    for i in range(9):
        for j in range(9):
            print(num[i][j], end="")
        print()