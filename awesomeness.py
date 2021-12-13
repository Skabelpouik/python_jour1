# -*- coding: utf-8 -*-
"""
Created on Mon Dec 13 17:17:56 2021

@author: Peridot
"""

#Awesomeness
peoples = ["Mylène Farmer", "Hayao Miyazaki", "Darth Vader", "Bibi", "Winnie the Pooh"]
great_peoples = [people + " the great!" for people in peoples]
for people in great_peoples:
    print(people)