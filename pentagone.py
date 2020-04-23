# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 18:43:46 2020

@author: bhara_5sejtsc
"""

def perimeterpentagone(s):
	return (5 * s)

def areapentagone(s,a): #a is distance from center of pentagon to each side
	return ((p * a)/2)

p = perimeterpentagone(s)

s = int(input("Enter the side: "))
a = int(input("Enter the apothem: "))

print("Perimeter of pentagone is ", perimeterpentagone(s))
print("Area of pentagone is ", areapentagone(s,a))
	