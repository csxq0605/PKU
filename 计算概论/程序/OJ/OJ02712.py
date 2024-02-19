# -*- coding: utf-8 -*-
"""
Created on Fri Oct  6 13:45:57 2023

@author: Lenovo
"""

n=int(input())
month={1:0,2:31,3:59,4:90,5:120,6:151,7:181,8:212,9:243,10:273,11:304,12:334}
for i in range(n):
    line=[int(x) for x in input().split()]
    num=line[2]
    day=month[line[3]]+line[4]-month[line[0]]-line[1]
    for j in range(day):
        num*=2
    print(num)