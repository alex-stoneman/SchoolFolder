import numpy as np

def matrix_of_known_connections(n, c):
    # Create a nxn matrix which for which each node
    # has exactly c connections
    # If this isn't possible then get close
    # Connections are undirected
    errorMessage = False
    matrix = np.zeros((n ,n), dtype=int)
    for y in range(n):
        index = y
        while sum(matrix[y]) < c:
            if index != y:
                matrix[y][index] = 1
                matrix[index][y] = 1
            index += 1
            if index == n and sum(matrix[y]) != c:
                errorMessage = True
                break
    if errorMessage:
        print("A matrix of this form is not possible")
    print(matrix)
    # only works if n % (c+1) == 0



matrix_of_known_connections(7, 3)
