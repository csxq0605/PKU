# -*- coding: utf-8 -*-
"""
Created on Sun Oct 15 17:36:19 2023

@author: Lenovo
"""

def solve():
    while True:
        r, n = map(int, input().split())
        if r == -1 and n == -1:
            return
        res = 0
        troop = list(map(int, input().split()))
        troop.sort()
        i = 0
        while i < n:
            far = troop[i]
            while i < n and troop[i] - far <= r:
                i += 1
            res += 1
            far = troop[i - 1]
            while i < n and troop[i] - far <= r:
                i += 1
        print(res)

solve()