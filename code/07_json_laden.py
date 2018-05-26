#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 20 15:11:09 2017

@author: Mathias Bernhard <bernhard@arch.ethz.ch>
"""

import json
import networkx as nx
import matplotlib.pyplot as plt

with open('../resources/gugelmann.json','r') as meinedatei:
    datensatz = json.load(meinedatei)

# kreiere ein neues Graph-Objekt
nG = nx.Graph()

# für jeden eintrag im dict
# ein eintrag ist ein gemälde / zeichnung
for k in datensatz:
    eintrag = datensatz[k]
    # für diese visualisierung interessieren uns nur die
    # namen der maler / zeichner...
    malerliste = eintrag['MalerInZeichnerIn']
    # ...noch spezifischer nur die gemälde, die
    # eine zusammenarbeit sind, dh. mehr als einen autoren haben
    if len(malerliste)>1:
        # innerhalb dieser liste jeder mit jedem mit einer kante verbinden
        for a in malerliste:
            for b in malerliste:
                # ...aber nur wenn die zwei namen unterschiedlich sind
                if a!=b:
                    nG.add_edge(a,b)

# grafische darstellung
plt.figure(figsize=(9,9))
nx.draw_spring(nG, with_labels=True, node_size=20)
