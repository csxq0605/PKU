# -*- coding: utf-8 -*-
"""
Created on Sun Oct 15 17:31:57 2023

@author: Lenovo
"""

try:
    while True:
        r, n = map(float, input().split())
        n = int(n)
        r_without_point = r

        if r % 1 != 0:
            last_location = len(str(r).split('.')[-1])
        else:
            last_location = 0

        r_without_point *= 10**last_location

        r_without_point = int(r_without_point)
        output = str(r_without_point**n)
        if r < 1:
            print(f'.{str(0)*(last_location*n - len(output))}{output}')
        elif last_location == 0:
            print(int(r ** n))
        elif r > 1:
            print(f'{output[:len(output) - last_location*n]}.{output[len(output) - last_location*n:]}')

except EOFError:
    pass