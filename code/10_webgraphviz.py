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

# output for http://www.webgraphviz.com
graphvizfile = open('../output/door-space-connections_webgraphviz.txt','w')
graphvizfile.write('digraph ifc {\n')
graphvizfile.write('graph [rankdir=LR];\n')
graphvizfile.write('node [shape=plaintext,height=0.1,style=filled];\n')
graphvizfile.write('edge [arrowhead=none];\n\n')

uniquespaceids = []
for d in doors:
    di = ifcfile.get_inverse(d)
    rsb = [e for e in di if e.is_a('IfcRelSpaceBoundary')]
    if len(rsb)>1:
        sids = []
        for e in rsb:
            sid = e.RelatingSpace.GlobalId
            sn = e.RelatingSpace.LongName
            sids.append(sid)
            if sid not in uniquespaceids:
                uniquespaceids.append(sid)
                graphvizfile.write('"'+sid+'" [label="'+sn+'"];\n')
        graphvizfile.write('"'+sids[0] +'" -> "'+ sids[1]+'" [label="'+str(d.OverallWidth)+'"];\n')

graphvizfile.write('}')
graphvizfile.close()
