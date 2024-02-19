# -*- coding: utf-8 -*-
"""
Created on Tue Dec 12 14:53:41 2023

@author: Lenovo
"""

for _ in range(int(input())):
    cases=[list(input().split())for i in range(3)]
    for coin in "ABCDEFGHIJKL":
        if all((coin in c[0] and c[2]=="up")or(coin in c[1] and c[2]=="down")or(coin not in c[1] and coin not in c[0] and c[2]=="even")for c in cases):
            print(f"{coin} is the counterfeit coin and it is heavy.")
            break
        elif all((coin in c[0] and c[2]=="down")or(coin in c[1] and c[2]=="up")or(coin not in c[0] and coin not in c[1] and c[2]=="even")for c in cases):
            print(f"{coin} is the counterfeit coin and it is light.")
            break