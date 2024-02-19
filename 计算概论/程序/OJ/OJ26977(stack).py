# -*- coding: utf-8 -*-
"""
Created on Tue Oct 17 11:24:47 2023

@author: Lenovo
"""

class Stack:
	def __init__(self):
		self.items=[]
	def push(self, item):
		self.items.append(item)
	def pop(self):
		return self.items.pop()
	def peek(self):
		return self.items[-1]
	def size(self):
		return len(self.items)
	def isEmpty(self):
		return self.items==[]

n=int(input())
l=[int(i) for i in input().split()]
s=Stack()
num=0
for i in range(n):
    while not s.isEmpty() and l[i]>l[s.peek()]:
        top=s.peek()
        s.pop()
        if s.isEmpty():
            break
        h=min(l[i],l[s.peek()])-l[top]
        d=i-s.peek()-1
        num+=d*h
    s.push(i)
print(num)