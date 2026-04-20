#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 13 16:04:07 2026

@author: atish
"""

class Cat(): 
    def __init__(self, arms, legs, eyes, tail, furry):
        self.arms = arms
        self.legs = legs
        self.eyes = eyes
        self.tail = tail
        self.furry = furry
        
    def member(self):
        print(f"The length of the arm is {self.arms} inches")
        print(f"The length of the legs is {self.legs} inches")
        print(f"The cat has {self.eyes} eyes")
        print(f"It is {self.tail} that the cat has a tail")
        print(f"It is {self.furry} that the cat is furry")
    

Cat(8,7,2,True,False).member()
