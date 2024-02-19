# -*- coding: utf-8 -*-
"""
Created on Sun Oct 15 17:23:26 2023

@author: Lenovo
"""

n=int(input())
num=0
for i in range(n):
    polyhedrons=input()
    if polyhedrons=="Tetrahedron":
        num+=4
    if polyhedrons=="Cube":
        num+=6
    if polyhedrons=="Octahedron":
        num+=8
    if polyhedrons=="Dodecahedron":
        num+=12
    if polyhedrons=="Icosahedron":
        num+=20
print(num)