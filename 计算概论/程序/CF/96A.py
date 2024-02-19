# -*- coding: utf-8 -*-
"""
Created on Thu Sep  7 19:06:10 2023

@author: Lenovo
"""

q=input()
def j(quene):
    if len(quene)<7:
        return "NO"
    else:    
        for i in range(len(quene)-6):
            if quene[i]==quene[i+1]==quene[i+2]==quene[i+3]==quene[i+4]==quene[i+5]==quene[i+6]:
                return "YES"
                break
        return "NO"
print(j(q))