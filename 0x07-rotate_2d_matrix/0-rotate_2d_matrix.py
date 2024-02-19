#!/usr/bin/python3
""" Rotates A 2D Matrix """


def rotate_2d_matrix(matrix):
    """ This function rotates a 2D Matrix in-place """
    matrix.reverse()
    copy_matrix = matrix.copy()

    for i in range(len(matrix)):
        matrix[i] = [row[i] for row in copy_matrix]
