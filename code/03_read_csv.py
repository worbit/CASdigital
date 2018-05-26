#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Oct  7 10:37:10 2017

@author: Mathias Bernhard <bernhard@arch.ethz.ch>
"""

# csv datei öffnen und zeilen in liste speichern
f = open("../resources/us-500_m.csv","rU")
zeilen = f.readlines()
f.close()

print(zeilen[2])

# spalten trennen
adressen = []
for z in zeilen:
    spalten = z.split(",")
    adressen.append(spalten)

# andere schreibweise
#adressen = []
#for i in range(len(zeilen)):
#    spalten = zeilen[i].split(",")
#    adressen.append(spalten)
