# -*- coding: utf-8 -*-
"""
Created on Tue Dec  5 17:24:26 2023

@author: Lenovo
"""

flag,dic=True,{}
while True:
    if flag:
        line=input()
        if line=="":
            flag=False
            continue
        w,t=map(str,line.split())
        dic.setdefault(t,w)
    else:
        try:
            word=input()
            try:    
                trans=dic[word]
            except KeyError:
                trans="eh"
            print(trans)
        except EOFError:
            break