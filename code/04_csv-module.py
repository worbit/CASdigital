#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Oct  7 11:12:53 2017

@author: Mathias Bernhard <bernhard@arch.ethz.ch>
"""

import csv

adressen = []
meine_datei = open("../resources/us-500_m.csv","rU")
db = csv.DictReader(meine_datei)
for meine_zeilen in db:
    adressen.append(meine_zeilen)
meine_datei.close()

# adress-liste durchsuchen
# und alle vom state NY in neue liste
new_yorkers = []
for e in adressen:
    if e["state"]=="NY":
        new_yorkers.append(e["first_name"])
        print(e["first_name"],e["state"])

texaner = []
for e in adressen:
    if e["state"]=="TX":
        texaner.append(e["last_name"])
        print(e["first_name"],e["state"])

Ma_namen = []
for e in adressen:
    if e["first_name"].startswith("Ma"):
        Ma_namen.append([e["first_name"],e["last_name"]])


triple_as = []
for e in adressen:
    if e["first_name"].count("a")==3:
        triple_as.append(e["first_name"])

namen10 = []
for e in adressen:
    if len(e["first_name"])==10:
        namen10.append(e["first_name"])

for e in adressen:
    if e["state"]=="ZH":
        print e["phone1"]

for e in adressen:
    if e["first_name"].endswith("la"):
        print(e["first_name"])
