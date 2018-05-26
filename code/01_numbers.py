#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Oct  7 08:39:49 2017

@author: Mathias Bernhard <bernhard@arch.ethz.ch>
"""

# schreibe das resultat von 2/3 in die konsole
print(2/3)

# definiere varaiblen a und b
a = 7
b = 3
e = a/b
print(e)

# definiere c und d als float
c = 2.0
d = 3.0
print(c/d)

# definiere s als string
s = "a/b"
name = "mathias o'donnell"
print(s)

# type conversion
print(float(a)/float(b))

# kombiniere string und zahl
print("heute ist der " + str(7) + ". Oktober")

w = str(a)
print("der wert von a ist "+w)

pi = 3.14159
print(pi)

# zahlen vergleichen
a = 9
b = 5
vergleich = a > b

#if vergleich == True:
#    print("a ist grösser")

if a > b:
    print("a ist grösser")
elif a < b:
    print("a ist kleiner")
else:
    print("a und b sind gleich")

print("vergleiche")
print(a > b)
print(a < b)
print(a == b)
print(a <= b)
print(a >= b)
print(a != b)
