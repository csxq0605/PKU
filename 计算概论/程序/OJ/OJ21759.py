# -*- coding: utf-8 -*-
"""
Created on Sun Nov 26 11:28:14 2023

@author: Lenovo
"""

n,x,y=map(int,input().split())
dic,count={},{}
for _ in range(n):
    classes,name,score=map(str,input().split())
    try:
        dic[name]+=int(score)
        count[name]+=1
    except KeyError:
        dic.setdefault(name,int(score))
        count.setdefault(name,1)
for _ in range(int(input())):
    name=input()
    if count[name]>=x and (dic[name]/count[name])>y:
        print("yes")
    else:
        print("no")