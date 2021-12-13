# -*- coding: utf-8 -*-
"""
Created on Mon Dec 13 17:20:20 2021

@author: Peridot
"""

#Greeter
def greetingPeople(name):
        print("Hi %s!" % name)
        print("Your name is %s and I am very happy to welcome you on board" % name)
        print("See what can you do on this website %s" % name)
        

names = ["Fanny", "Emilie", "Cookie", "Ramina"]
for name in names:
    greetingPeople(name)