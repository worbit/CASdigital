#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Oct  7 13:41:28 2017

@author: Mathias Bernhard <bernhard@arch.ethz.ch>
"""

import csv

# csv datei öffnen und als liste von dictionaries speichern
adressen = []
input_datei = open("../resources/us-500_m.csv","rU")
datenbank = csv.DictReader(input_datei)
for zeile in datenbank:
    adressen.append(zeile)
input_datei.close()

# alle einträge mit einer yahoo-email adresse
yahoo_mail = []
for e in adressen:
    if "yahoo" in e["email"]:
        yahoo_mail.append(e)

# listen einträge in neue csv-datei speichern
output_datei = open("../output/yahoo-export.csv","w")
for e in yahoo_mail:
    output_datei.write(e["first_name"]+","+e["last_name"]+","+e["email"]+"\n")
output_datei.close()
