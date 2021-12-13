# -*- coding: utf-8 -*-
"""
Created on Mon Dec 13 19:14:45 2021

@author: Peridot
"""

def original(numbers_list):
    print("Numbers in original order:")
    for number in numbers_list:
        print(number)

def increase(numbers_list):
    print("Numbers in increasing order:")
    for number in sorted(numbers_list):
        print(number)
        
def decrease(numbers_list):
    print("Numbers in decreasing order:")
    for number in sorted(numbers_list, reverse=True):
        print(number)
        
def reverse_list(numbers_list):
    numbers_list.reverse()
    for number in numbers_list:
        print(number)
        
def increasePermanently(numbers_list):
    numbers_list.sort()
    print("Numbers in increasing order:")
    for number in numbers_list:
        print(number)
        
def decreasePermanently(numbers_list):
    numbers_list.sort(reverse=True)
    print("Numbers in decreasing order:")
    for number in numbers_list:
        print(number)
        
numbers_list = [4, 7, 9, 2, 6]
original(numbers_list)
increase(numbers_list)
original(numbers_list)
decrease(numbers_list)
original(numbers_list)
print("Numbers in the reverse order from what it started:")
reverse_list(numbers_list)
print("Numbers in original order:")
reverse_list(numbers_list)
increasePermanently(numbers_list)
decreasePermanently(numbers_list)