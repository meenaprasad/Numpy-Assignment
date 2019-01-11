# -*- coding: utf-8 -*-
"""
Created on Thu Jan  10 16:27:49 2019

@author: meenaprasad
"""
def reverse(s): 
    return s[::-1]

def isPalindrome(s): 
    # Calling reverse function 
    rev = reverse(s) 
  
    # Checking if both string are equal or not 
    if (s == rev): 
        return True
    return False