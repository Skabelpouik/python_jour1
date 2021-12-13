# -*- coding: utf-8 -*-
"""
Created on Mon Dec 13 17:19:55 2021

@author: Peridot
"""

#Gymnast Scores
scores = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print("The lowest possible score is %d, and the highest possible score is %d." % (scores[0], scores[-1]))
for score in scores:
    print("A judge can give a gymnast %d points" % score)