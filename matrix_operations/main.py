import numpy as np

def trasform_to_matching_shape(matrix1, matrix2):
    shape_y = max(m.shape[0] for m in (matrix1, matrix2))
    shape_x = max(m.shape[1] for m in (matrix1, matrix2))
    matrix1 = np.pad(matrix1, ((0, shape_y - matrix1.shape[0]), (0, shape_x - matrix1.shape[1])), 'constant', constant_values=1)
    matrix2 = np.pad(matrix2, ((0, shape_y - matrix2.shape[0]), (0, shape_x - matrix2.shape[1])), 'constant', constant_values=1)
    return matrix1, matrix2

def find_index(ls, item):

    for n, i in enumerate(ls):
        if type(i) == str and i == item:
            return n

def matrix_operator(matrixes, operations):
    while len(operations)>1:
        if any('*' in i for i in operations):
            i = find_index(operations, '*')
            if type(operations[i-1]) == str:
                array1 = np.array(matrixes[operations[i-1]])
            else:
                array1 = np.array(operations[i-1])

            if type(operations[i+1]) == str:
                array2 = np.array(matrixes[operations[i+1]])
            else:
                array2 = np.array(operations[i+1])

            for j in range(2): operations.pop(i)
            array1, array2 = trasform_to_matching_shape(array1,array2)
            operations[i-1] = np.dot(array1, array2)

        else:
            i = find_index(operations, '+')
            if type(operations[i-1]) == str:
                array1 = np.array(matrixes[operations[i-1]])
            else:
                array1 = np.array(operations[i-1])

            if type(operations[i+1]) == str:
                array2 = np.array(matrixes[operations[i+1]])
            else:
                array2 = np.array(operations[i+1])

            for j in range(2): operations.pop(i)
            array1, array2 = trasform_to_matching_shape(array1,array2)
            operations[i-1] = np.add(array1, array2)
    return operations[0]

matrixes = {}
operations = []

with open('./input.txt', 'r') as f:
    lines = f.readlines()
    current_key = ""
    current_matrix = []
    for i in lines:
        i = i.rstrip()
        if i == 'matrices':
            read_more_matrix = True
        elif i == "operations":
            read_more_matrix = False
        elif i.isalpha() and read_more_matrix:
            if current_key:
                matrixes[current_key] = current_matrix
            current_key = i
            current_matrix = []
        elif read_more_matrix is False:
            operations.append(i.split())
        elif i:
            current_matrix.append([int(n) for n in i.split()])
    matrixes[current_key] = current_matrix


for i in operations:
    if len(i) > 0:
        print(' '.join(i))
        solution = matrix_operator(matrixes, i)
        for row in solution:
            print(*row, sep=' ')
        print()
