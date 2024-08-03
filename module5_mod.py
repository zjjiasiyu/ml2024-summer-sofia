# -*- coding: utf-8 -*-
"""
Created on Fri Aug  2 20:36:17 2024

@author: zjjia
"""


class NumberList:
    def __init__(self):
        self.numbers = []

    def read_numbers(self, count):
        self.numbers = []
        for i in range(count):
            while True:
                try:
                    num = int(input(f"Enter number {i + 1}: "))
                    self.numbers.append(num)
                    break
                except ValueError:
                    print("Please enter an positive integer.")

    def find_index(self, x):
        if x in self.numbers:
            return self.numbers.index(x) + 1  # +1 to convert from 0-based to 1-based index
        return -1

