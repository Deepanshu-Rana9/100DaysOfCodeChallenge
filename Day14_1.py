# Matrix Rotation (90° Clockwise)
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

def rotate_matrix(matrix):
    n = len(matrix)
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    for row in matrix:
        row.reverse()
    return matrix

rotated_matrix = rotate_matrix(matrix)
for row in rotated_matrix:
    print(row)
