# -*- coding: utf-8 -*-
"""
Created on Mon Dec 13 17:14:19 2021

@author: Peridot
"""

#Ordered Numbers
numbers = [4, 7, 9, 2, 6]
print("Numbers in original order:")
for number in numbers:
    print(number)
print("Numbers in increasing order:")
for number in sorted(numbers):
    print(number)
print("Numbers in original order:")
for number in numbers:
    print(number)
print("Numbers in decresing order:")
for number in sorted(numbers, reverse=True):
    print(number)
print("Numbers in original order:")
for number in numbers:
    print(number)
print("Numbers in the reverse order from what it started:")
numbers.reverse()
for number in numbers:
    print(number)
print("Numbers in the original order:")
numbers.reverse()
for number in numbers:
    print(number)
print("Number in increasing order:")
numbers.sort()
for number in numbers:
    print(number)
print("Numbers in decreasing order:")
numbers.sort(reverse=True)
for number in numbers:
    print(number)