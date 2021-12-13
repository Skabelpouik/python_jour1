# -*- coding: utf-8 -*-
"""
Created on Mon Dec 13 19:38:29 2021

@author: Peridot
"""

def original(careers):
    print("List in original order:")
    for career in careers:
        print(career)

def increase(careers):
    print("List in alphabetical order:")
    for career in sorted(careers):
        print(career)
        
def decrease(careers):
    print("List in reverse alphabetical order:")
    for career in sorted(careers, reverse=True):
        print(career)
        
def reverse_list(careers):
    careers.reverse()
    for career in careers:
        print(career)
        
def increasePermanently(careers):
    careers.sort()
    print("List in alphabetical order:")
    for career in careers:
        print(career)
        
def decreasePermanently(careers):
    careers.sort(reverse=True)
    print("List in reverse alphabetical order:")
    for career in careers:
        print(career)
        
careers = ["actor", "programmer", "pet sitter", "teacher"]
original(careers)
increase(careers)
original(careers)
decrease(careers)
original(careers)
print("List in reverse alphabetical order from what it started:")
reverse_list(careers)
print("List in original order:")
reverse_list(careers)
increasePermanently(careers)
decreasePermanently(careers)