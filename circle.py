# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 19:04:25 2020

@author: bhara_5sejtsc
"""

def areacircle(r): 
	return (3.14 * r * r) 

def perimetercircle(r): 
	return (2 * 3.14 * r) 


r = int(input("radius = "));

print ("Area = ", areacircle(r)) 
print ("perimeter = ", perimetercircle(r)) 


