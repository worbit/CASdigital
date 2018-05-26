#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat May 26 07:14:02 2018

@author: Mathias Bernhard <bernhard@arch.ethz.ch>
"""

import ifcopenshell
path = '/Users/bernham/Desktop/180526_kurs/'
fn = 'MFH Birmensdorf Arch_optimized.ifc'

ifcfile = ifcopenshell.open(path+fn)

doors = ifcfile.by_type('IfcDoor')

#d1 = doors[0]

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
spids = []
for d in doors:
    print('----')
    di = ifcfile.get_inverse(d)
    for e in di:
        if e.is_a('IfcRelSpaceBoundary'):
            s = e.RelatingSpace
            print(s.LongName)
'''

f = open('fuer_graphviz.txt','w')
spids = []
for d in doors:
    #print('----')
    di = ifcfile.get_inverse(d)
    rsb = [e for e in di if e.is_a('IfcRelSpaceBoundary')]
    if len(rsb)>1:
        for e in rsb:
            sid = e.RelatingSpace.GlobalId
            sn = e.RelatingSpace.LongName
            if sid not in spids:
                spids.append(sid)
                f.write('"'+sid+'" [label="'+sn+'"]\n')
        f.write('"'+rsb[0].RelatingSpace.GlobalId +'" -> "'+ rsb[1].RelatingSpace.GlobalId+'"\n')
f.close()
