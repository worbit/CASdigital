#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 29 17:26:50 2018

@author: Mathias Bernhard <bernhard@arch.ethz.ch>
"""

# import regular expressions library
import re

# file to read
path = '../resources/'
filename = 'L-slab.ifc'

# output for http://www.webgraphviz.com
graphvizfile = open('../output/L-slab_webgraphviz.txt','w')
graphvizfile.write('digraph ifc {\n')
graphvizfile.write('graph [rankdir=LR];\n')
graphvizfile.write('node [shape=plaintext,height=0.1,style=filled];\n')
graphvizfile.write('edge [arrowhead=none];\n\n')

with open(path + filename,'r') as f:
    lns = f.readlines()
    for l in lns:
        if l.startswith('#'):
            prts = l.split(' ')
            objid = prts[0][:-1]
            objtype = prts[1].split('(')[0]
            graphvizfile.write('"'+objid+'" [label="'+objtype[3:]+'"];\n')
            searchstring = prts[1]
            res = re.findall("#[0-9]+", searchstring)
            if res:
                for r in res:
                    graphvizfile.write('"'+r+'" -> "'+objid+'";\n')

graphvizfile.write('}')
graphvizfile.close()
