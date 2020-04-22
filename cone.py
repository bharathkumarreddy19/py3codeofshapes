# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 19:04:25 2020

@author: bhara_5sejtsc
"""


def volumecone(r,h): 
	return ((1/3) * 3.14 * r * r * h) 

def surfaceareacone(r,s): 
	return (3.14 * r * (r + s)) 


r = int(input("radius = "));
h = int(input("heught = "));
s = int(input("slant height = ")); 

print ("Area = ", volumecone(r,h)) 
print ("Perimeter = ", surfaceareacone(r,s)) 
