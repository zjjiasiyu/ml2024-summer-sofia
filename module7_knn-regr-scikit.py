# -*- coding: utf-8 -*-
"""
Created on Mon Aug 12 17:32:56 2024

@author: zjjia
"""
pip install scikit-learn
import numpy as np
from sklearn.neighbors import KNeighborsRegressor
from sklearn.metrics import mean_squared_error

def main():
    # Read input values
    N = int(input("Enter the number of data points (N): "))
    k = int(input("Enter the number of neighbors (k): "))

    if k > N:
        print("Error: k cannot be greater than N.")
        return

    # Initialize lists to store the points
    X = []
    Y = []
    print(f"Enter {N} data points (x y) one by one:")

    for i in range(N):
        x = float(input(f"Enter x value for Point {i+1}: "))
        y = float(input(f"Enter y value: for Point {i+1}: "))
        X.append([x])  # Use list of lists for X to match expected input shape
        Y.append(y)

    # Convert lists to numpy arrays
    X = np.array(X)
    Y = np.array(Y)

    # Calculate variance of labels
    variance = np.var(Y)
    print(f"Variance of labels in the training dataset: {variance:.2f}")

    # Create and train the k-NN regressor
    regressor = KNeighborsRegressor(n_neighbors=k)
    regressor.fit(X, Y)

    # Get input X for prediction
    X_pred = float(input("Enter the X value to predict: "))
    X_pred = np.array([[X_pred]])

    # Perform prediction
    Y_pred = regressor.predict(X_pred)
    print(f"The predicted Y value for X={X_pred[0][0]} is: {Y_pred[0]:.2f}")

if __name__ == "__main__":
    main()
