# -*- coding: utf-8 -*-
"""
Created on Fri Aug  2 20:39:08 2024

@author: zjjia
"""


from module5_mod import NumberList

def main():
    # Create an instance of NumberList
    num_list = NumberList()
    
    # Read N from the user
    while True:
        try:
            N = int(input("Enter the number of elements (N): "))
            if N > 0:
                break
            else:
                print("Please enter a positive integer.")
        except ValueError:
            print("Invalid input. Please enter an integer.")

    # Read N numbers
    num_list.read_numbers(N)
    
    # Read X from the user
    while True:
        try:
            X = int(input("Enter the number to find: "))
            break
        except ValueError:
            print("Invalid input. Please enter an integer.")

    # Find and display the index of X
    index = num_list.find_index(X)
    if index == -1:
        print("-1")
    else:
        print(f"The index of {X} is: {index}")

if __name__ == "__main__":
    main()

