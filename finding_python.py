# -*- coding: utf-8 -*-
"""
Created on Mon Dec 13 17:19:39 2021

@author: Peridot
"""

#Finding Python
sentence = "You can read this file into your Python program. Python is a great language."
print("Python" in sentence)
print(sentence.find("Python"))
print(sentence.rfind("Python"))
print(sentence.count("Python"))
words_list = sentence.split(" ")
for word in words_list:
    print(word)
print(sentence.replace("Python", "Ruby"))