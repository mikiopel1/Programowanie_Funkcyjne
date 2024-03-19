def transpose_matrix(matrix):
    return [[row[i] for row in matrix] for i in range(len(matrix[0]))]

# Przykład użycia:
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
transposed_matrix = transpose_matrix(matrix)
print("Transposed matrix:", transposed_matrix)
