# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 15:15:24 2024

@author: zjjia
"""

import numpy as np
from sklearn.metrics import precision_score, recall_score


# Function to get user input for N points
def get_input_points(N):
    x_values = np.zeros(N, dtype=int)
    y_values = np.zeros(N, dtype=int)

    for i in range(N):
        x_values[i] = int(input(f"Enter x value for point {i+1} (0 or 1): "))
        y_values[i] = int(input(f"Enter y value for point {i+1} (0 or 1): "))

    return x_values, y_values


def main():
    N = int(input("Enter the number of points N (positive integer): "))

    if N <= 0:
        print("N must be a positive integer!")
        return

    x_values, y_values = get_input_points(N)
    print(f"X: {x_values}")
    print(f"Y: {y_values}")
    # Calculating Precision and Recall
    precision = precision_score(x_values, y_values)
    recall = recall_score(x_values, y_values)

    # Output the results
    print(f"Precision: {precision:.2f}")
    print(f"Recall: {recall:.2f}")


if __name__ == "__main__":
    main()
