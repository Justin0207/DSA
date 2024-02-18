# -*- coding: utf-8 -*-
"""
Created on Sat Dec 23 05:26:54 2023

@author: HP
"""


num = int(input("Enter a number"))
i = 1
fib = []
if num == 0:
    fib = []
elif num == 1:
    fib = [1]
elif num == 2:
    fib = [1 , 1]
elif num > 2:
    fib = [1, 1]
    while i < (num - 1):
        fib.append(fib[i] + fib[i-1])
        i += 1
print(fib)