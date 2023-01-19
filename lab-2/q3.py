# WAP to perform multiplication of two matrices using UDF

def matrix_multiplication(A, B):
    result = [[0 for i in range(len(B[0]))] for j in range(len(A))]

    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(B)):
                result[i][j] += A[i][k] * B[k][j]
    return result

matrix1 = [[1, 2], [3, 4]]
matrix2 = [[5, 6], [7, 8]]

result = matrix_multiplication(matrix1, matrix2)

for row in result:
    print(row)