# -*- coding: utf-8 -*-
"""
Created on Mon Jul 22 23:02:16 2024

@author: zjjia
"""

# Ask the user for input N (positive integer)
N = int(input("Enter a positive integer N to represent number of elements: "))

numbers = []

# Ask the user to provide N numbers one by one
for i in range(N):
    num = int(input("Enter a number in the list of numbers: "))
    numbers.append(num)

# Ask the user for input X (integer)
X = int(input("Enter an integer X to search for in the list: "))

# Search for X in the list of numbers
if X in numbers:
    print(f"The output is {numbers.index(X) + 1}")
else:
    print("The output is -1") #X is not in the list