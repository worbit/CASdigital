#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Oct  7 14:00:11 2017

@author: Mathias Bernhard <bernhard@arch.ethz.ch>
"""

import csv
import matplotlib.pyplot as plt

# csv datei öffnen und als liste von dictionaries speichern
sales = []
input_datei = open("../resources/realestate.csv","rU")
datenbank = csv.DictReader(input_datei)
for zeile in datenbank:
    sales.append(zeile)
input_datei.close()

# finde alle häuser mit mindestens 4 schlafzimmern für weniger als 100'000 $
for e in sales:
    if int(e["beds"])>3 and float(e["price"])<100000:
        print e

# speichere alle längen- und breitengrade in listen (x für längen und y für breitengrade)
xs = []
ys = []
prices = []
for e in sales:
    x = float(e["longitude"])
    y = float(e["latitude"])
    xs.append(x)
    ys.append(y)
    prices.append(float(e["price"]))

# plotte die koordinatenpunkte mit dem preis als farbe
plt.scatter(xs,ys,c=prices)
plt.show()
