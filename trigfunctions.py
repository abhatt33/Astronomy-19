#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 12 15:12:50 2026

@author: atish
"""
import math


def main():
 
    n = 1000

    step = 2 / (n - 1)


    print(f"{'x':>10} {'sin(x)':>15}")

    for i in range(n):
        x = i * step
        y = math.sin(x)
        print(f"{x:10.6f} {y:15.6f}")


if __name__ == "__main__":
    main()
