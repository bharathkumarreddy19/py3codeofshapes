# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 19:04:25 2020

@author: bhara_5sejtsc
"""

def volumecylinder(r,h): 
	return (3.14 * r * r * h) 

def surfaceareacylinder(r,h): 
	return (2 * 3.14 * r * (r +h)) 


r = int(input("radius = "));
h = int(input("height = "));


print ("Area = ", volumecylinder(r,h)) 
print ("surfacearea = ", surfaceareacylinder(r,h)) 


