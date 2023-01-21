import numpy as np

matrix = [[1 if i == j else 0 for j in range(3)] for i in range(3)]
for row in matrix:
    print(row)
for i in range(3):
    for j in range(3):
        if i != j:
            matrix[i][j] += 3
for row in matrix:
    print(row)
matrix = [row[:2] for row in matrix]
for row in matrix:
    print(row)
