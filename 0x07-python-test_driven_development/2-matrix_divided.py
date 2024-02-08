#!/usr/bin/python3

def matrix_divided(matrix, div):
    if type(matrix) not in [int, float]:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    elif 