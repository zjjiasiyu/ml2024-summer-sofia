# -*- coding: utf-8 -*-
"""
Created on Fri Aug  2 20:26:52 2024

@author: zjjia
"""

class NumberProcessor:
    def __init__(self):
        self.numbers = []

    def read_numbers(self, N):
        print(f"Please enter {N} numbers:")
        for _ in range(N):
            number = int(input())
            self.numbers.append(number)

    def find_number(self, X):
        try:
            index = self.numbers.index(X)
            return index + 1
        except ValueError:
            return -1

def main():
    processor = NumberProcessor()
    N = int(input("Enter a positive integer N: "))
    processor.read_numbers(N)
    X = int(input("Enter the number to search for X: "))
    result = processor.find_number(X)
    print(result)

if __name__ == "__main__":
    main()
