# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 19:32:11 2020

@author: bhara_5sejtsc
"""

def perirhombus(a,b):
	return (2 * (a + b))

def arearhombus(d,D):
	return ((d * D)/2)

a = int(input("Enter side length of two equal lengths :  "))
b = int(input("Enter another side length of two equal lengths: "))
d = int(input("Length of one diagnal:  "))
D = int(input("Length of another diagnal: "))

print("Perimeter of rhombus is ", perirhombus(a,b))
print("Area of rhombus is ", arearhombus(d,D))