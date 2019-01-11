# -*- coding: utf-8 -*-
"""
Created on Thu Jan  10 16:19:20 2019

@author: meenaprasad
"""
def fib2(n): # return Fibonacci series up to n
    result = []
    a, b = 0, 1
    while b < n:
        result.append(b)
        a, b = b, a+b
    return result
