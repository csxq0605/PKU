# -*- coding: utf-8 -*-
"""
Created on Sat Sep 16 14:58:54 2023

@author: Lenovo
"""

n=int(input())
numDict = {'A' : 2, 'B' : 2, 'C' : 2,'D' : 3, 'E' : 3, 'F' : 3,'G' : 4, 'H' : 4, 'I' : 4,'J' : 5, 'K' : 5, 'L' : 5,'M' : 6, 'N' : 6, 'O' : 6,'P' : 7, 'R' : 7, 'S' : 7,'T' : 8, 'U' : 8, 'V' : 8,'W' : 9, 'X' : 9, 'Y' : 9,"1":1,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9,"0":0}
teles={}
for i in range(n):
    tele=input().replace("-","")
    telenum=""
    for i in tele[0:3]:
            telenum+=str(numDict[i])
    telenum+="-"
    for i in tele[3::]:
            telenum+=str(numDict[i])
    try:        
        teles[telenum]+=1
    except KeyError:
        teles.setdefault(telenum,1)
dictionary=sorted(teles.items())
if set(teles.values()) == {1}:
    print("No duplicates.")
else:
    for key, value in dictionary:
        if value > 1:
            print(key,value)