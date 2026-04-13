#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 11 20:38:38 2026

@author: atish
"""

def f(x):
    return x**3 + 8
def main():
    value = f(9)
    print(value)
    
    if value > 27:
        print("YAY!")
if __name__ == "__main__":
    main()    