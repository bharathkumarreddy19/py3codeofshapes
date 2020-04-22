# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 20:36:51 2020

@author: bhara_5sejtsc
"""

def volumecuboid(l,b,h):
	return (l * b * h)

def areacuboid(l,b,h):
	return (2 * ((l * b) + (b * h) + (h * l)))

l = int(input("length = "))
b = int(input("bradth = "))
h = int(input("heigth = "))

print ("Volume of cuboid is = ", volumecuboid(l,b,h))
print ("Area of cuboid is = ", areacuboid(l,b,h))
