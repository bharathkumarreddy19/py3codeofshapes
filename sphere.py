# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 19:04:25 2020

@author: bhara_5sejtsc
"""

def volumesphere(r): 
	return ((4/3) * 3.14 * r * r * r) 

def surfaceareasphere(r): 
	return (4 * 3.14 * r * r) 


r = int(input("radius = "));

print ("Area = ", volumesphere(r)) 
print ("surface area = ", surfaceareasphere(r)) 


