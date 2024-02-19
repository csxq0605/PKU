# -*- coding: utf-8 -*-
"""
Created on Tue Nov 14 11:14:39 2023

@author: Lenovo
"""

dir=[(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1)]
pos=[[0]*3 for _ in range(1001)]

class Tree:
    def __init__(self):
        self.next=[None]*26
        self.end=False
        self.order=0

def create_trie(p,string,j):
    i=0
    while i<len(string):
        value=ord(string[i])-ord('A')
        if p.next[value] is None:
            p.next[value]=Tree()
        p=p.next[value]
        i+=1
    p.end=True
    p.order=j

def search(p,i,j,k):
    di=i
    dj=j
    while p and 0<=di<l and 0<=dj<c:
        value=ord(puzzle[di][dj])-ord('A')
        if p.next[value]:
            if p.next[value].end:
                pos[p.next[value].order][0]=i
                pos[p.next[value].order][1]=j
                pos[p.next[value].order][2]=k
            di+=dir[k][0]
            dj+=dir[k][1]
            p=p.next[value]
        else:
            break

l,c,w=map(int,input().split())
puzzle=[]
for _ in range(l):
    puzzle.append(list(input()))
root=Tree()
for i in range(w):
    word=input()
    create_trie(root,word,i)
for i in range(l):
    for j in range(c):
        for k in range(8):
            search(root,i,j,k)
for i in range(w):
    print(f'{pos[i][0]} {pos[i][1]} {chr(pos[i][2]+ord("A"))}')