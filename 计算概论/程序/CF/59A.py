# -*- coding: utf-8 -*-
"""
Created on Tue Aug 29 13:59:54 2023

@author: Lenovo
"""
word=input()
list=[str(i) for i in word]
up,low=0,0
upper=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
lower=["a","b","c","d","e","f","g","h","i""j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
for i in range(len(list)):
    if list[i] in upper:
        up+=1
    if list[i] in lower:
        low+=1
if up>low:
    print(word.upper())
else:
    print(word.lower())
    
    
