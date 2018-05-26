#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat May 26 07:14:02 2018

@author: Mathias Bernhard <bernhard@arch.ethz.ch>
"""

import ifcopenshell

# file to read
path = '../resources/'
filename = 'MFH Birmensdorf Arch_optimized.ifc'

# open ifc file
ifcfile = ifcopenshell.open(path+filename)

# get a list of all the doors
doors = ifcfile.by_type('IfcDoor')

# short version with list comprehension and set
doorwidths = [d.OverallWidth for d in doors]
for w in set(doorwidths):
    print w, '\t', doorwidths.count(w)

# long version with dictionary
'''
widths = {}
for d in doors:
    ws = str(d.OverallWidth)
    if ws in widths:
        widths[ws] += 1
    else:
        widths[ws] = 1

for k in widths:
    print(str(k)+'\t'+str(widths[k]))
'''
