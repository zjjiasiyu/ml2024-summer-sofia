# -*- coding: utf-8 -*-
"""
Created on Thu Aug  8 13:04:13 2024

@author: zjjia
"""

import numpy as np


# Read input values
N = int(input("Please enter the number of points (N): "))
k = int(input("Enter the value of k: "))

if k > N:
    print("Error: k should be less than or equal to N.")
else:
    print(f"Great! we are analyzing {N} points with {k} neighbors. ")
    points = []
    for i in range(N):
        x = float(input(f"Enter x value for Point {i+1}: "))
        y = float(input(f"Enter y value for Point {i+1}: "))
        points.append((x, y))

    X = float(input("Enter the X value for prediction: "))

    # Extract x and y values
    x_values = np.array([point[0] for point in points])
    y_values = np.array([point[1] for point in points])
    
    # Calculate the distances from X to all points
    distances = np.abs(x_values - X)
    
    # Get the indices of the k nearest neighbors
    nearest_indices = np.argsort(distances)[:k]
    
    # Average the y-values of the k nearest neighbors
    y_result = np.mean(y_values[nearest_indices])
    
    print(f"The predicted Y value is: {y_result}")
