# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 19:17:46 2020

@author: bhara_5sejtsc
"""

def peritrapezoid(a,b,c,d):
	return (a + b + c + d)

def areatrapezoid(h,b,d): #h is height between two parallel and opposite sides
	return (((b + d) * h)/2)

a = int(input("First side: "))
b = int(input("Second side: "))
c = int(input("Third side: "))
d = int(input("Fourth sode: "))
h = int(input("Heigth: "))

print("Perimeter of Trapezoid is ", peritrapezoid(a,b,c,d))
print("Area of Trapezoid is ", areatrapezoid(h,b,d))