# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 20:26:30 2020

@author: bhara_5sejtsc
"""

def volumecube(s):
	return (s * s * s)

def areacube(s):
	return (6 * s * s)

s = int(input("Side length = "));

print ("Volume of cube = " , volumecube(s))
print ("Area of Cube = " , areacube(s))
	