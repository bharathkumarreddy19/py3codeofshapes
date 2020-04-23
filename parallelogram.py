# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 19:10:38 2020

@author: bhara_5sejtsc
"""

def periparallelogram(a,b):
	return (2 * (a + b))

def areaparallelogram(h,b):
	return (h * b)

a = int(input("Enter one side length: "))
b = int(input("Enter another side length: "))
h = int(input("Enter length of the height: "))

print("Perimeter of parallelogram is ",periparallelogram(a,b))
print("Area of parallelogram is ",areaparallelogram(h,b))