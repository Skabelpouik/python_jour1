# -*- coding: utf-8 -*-
"""
Created on Mon Dec 13 17:13:00 2021

@author: Peridot
"""

#Working List
careers = ["actor", "programmer", "pet sitter", "teacher"]
print(careers.index("pet sitter"))
print("teacher" in careers)
careers.append("nurse")
careers.insert(0, "cooking chef")
for career in careers:
    print(career)