import numpy as np

#returns the assigned arrays before and after the specified index in the operation list
def get_arrays(i, operation, matrixes):
    match operation[i - 1]:
        case str(): 
            array1 = matrixes[operation[i - 1]]
        case _: 
            array1 = operation[i - 1]

    match operation[i + 1]:
        case str(): 
            array2 = matrixes[operation[i + 1]]
        case _: 
            array2 = operation[i + 1]
    return array1, array2

#performs the given operation on the given matrixes, and returns the solution
def matrix_operator(matrixes, operation):
    while len(operation) > 1:
        operators = operation[1::2]
        if '*' in operators:
            i = operators.index('*') * 2 + 1
            array1, array2 = get_arrays(i, operation, matrixes)
            for j in range(2): operation.pop(i)
            operation[i - 1] = np.dot(array1, array2)

        else:
            i = operators.index('+') * 2 + 1
            array1, array2 = get_arrays(i, operation, matrixes)
            for j in range(2): operation.pop(i)
            operation[i - 1] = np.add(array1, array2)
    return operation[0]

#reads input file and returns matrixes in a dictionary, and operations in a list
def read_input_file(file):
    matrixes = {}
    operations = []
    with open(file, 'r') as f:
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
                    matrixes[current_key] = np.array(current_matrix)
                current_key = i
                current_matrix = []
            elif read_more_matrix is False:
                operations.append(i.split())
            elif i:
                current_matrix.append([int(n) for n in i.split()])
        matrixes[current_key] = np.array(current_matrix)
    return matrixes, operations

#iterating through the operations, and printing the solutions
matrixes, operations = read_input_file('./input.txt')
for i in operations:
    if len(i) > 0:
        print(' '.join(i))
        solution = matrix_operator(matrixes, i)
        for row in solution:
            print(*row, sep=' ')
        print()