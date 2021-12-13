# -*- coding: utf-8 -*-
"""
Created on Mon Dec 13 17:15:59 2021

@author: Peridot
"""

#Protected List
peoples = ["Mylène Farmer", "Hayao Miyazaki", "Darth Vader"]
peoples_copy = peoples[:]
peoples_copy.append("Bibi")
peoples_copy.append("Winnie the Pooh")
print("It's the original list:")
for people in peoples:
    print(people)
print("It's the copied list:")
for people in peoples_copy:
    print(people)