# -*- coding: utf-8 -*-
"""
Created on Mon Dec 13 17:13:47 2021

@author: Peridot
"""

#Ordered Working List
careers = ["actor", "programmer", "pet sitter", "teacher"]
print("List in original order:")
for career in careers:
    print(career)
print("List in alphabetical order:")
for career in sorted(careers):
    print(career)
print("List in original order:")
for career in careers:
    print(career)
print("List in reverse alphabetical order:")
for career in sorted(careers, reverse=True):
    print(career)
print("List in original order:")
for career in careers:
    print(career)
print("List in the reverse order from what it started:")
careers.reverse()
for career in careers:
    print(career)
print("List in original order:")
careers.reverse()
for career in careers:
    print(career)
print("List in alphabetical order:")
careers.sort()
for career in careers:
    print(career)
print("List in reverse alphabetical order:")
careers.sort(reverse=True)
for career in careers:
    print(career)