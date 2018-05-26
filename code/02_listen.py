#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Oct  7 09:41:34 2017

@author: Mathias Bernhard <bernhard@arch.ethz.ch>
"""

# definiere eine liste von zahlen
meine_liste = [3,5,8,1.5,2,0,567,34,123.34,87]

# definiere eine zweite liste von zahlen
otherlist = [1,2,34,5]

# füge die eine liste der anderen hinzu
combined_lists = meine_liste + otherlist

# einzelnes element auslesen
print(meine_liste[2])
print(meine_liste[-1])

# mehrere elemente auslesen (slicing)
print(meine_liste[2:8])

print(meine_liste[2],meine_liste[8])

# len: gibt die länge der liste zurück
print(len(meine_liste))
meine_liste.append(55)
print(len(meine_liste))

print(meine_liste)
meine_liste.sort()
print(meine_liste)

for z in meine_liste:
    print("z = "+str(z))
