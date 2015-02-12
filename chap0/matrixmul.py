# python-3

def inputmatrix_values(row, col):
    print ("Enter matrix values row by row - space separated")
    r = 1
    matrix = []
    while r <= row:
        row_in = input("row %d: " % r)
        rowvals = row_in.split(" ")
        try:
            rowvals = [int(val) for val in rowvals]
        except ValueError:
            print ("Bad integer value. plz try again..")
            print ("Enter matrix values row by row - space separated")
            r = 1
            continue
        if len(rowvals) != col:
            print ("Wrong number of cols. Expected: %d, Got: %d"
                   % (col, len(rowvals)))
            print ("Enter matrix values row by row - space separated")
            r = 1
            continue
        matrix.append(rowvals)
        r += 1
    print (matrix)
    return matrix


def matrixmultiply(A, B):
    if (A is None) or (B is None):
        print ("One of matrix is None")
        return None
    rowA = len(A)
    colA = len(A[0])
    rowB = len(B)
    colB = len(B[0])
    if colA != rowB:
        print ("matrix multiplication not possible.")
        return None
    C = []
    for i in range(rowA):
        c_row = []
        for j in range(colB):
            total = 0
            for k in range(rowA):
                total += A[i][k] * B[k][j]
            c_row.append(total)
        C.append(c_row)
    return C


def matrix_input():
    print ("Enter values space separated")
    while True:
        matrix = input("rows and cols for matrix: ")
        matrix = matrix.strip()
        matrix = matrix.split(" ")
        try:
            if len(matrix) != 2:
                print ("Too few or too many values for row/col")
                continue
            matrix = [int(f) for f in matrix]
            A = inputmatrix_values(matrix[0], matrix[1])
            return A
        except ValueError:
            print ("Bad row/col input. Try again..")


def printmatrix(M):
    if M is None:
        return
    row = len(M)
    col = len(M[0])
    for i in range(row):
        for j in range(col):
            print (M[i][j], sep=" ", end=" ")
        print ()


def test_matrix_mul():
    print ("Input for Matrix A")
    A = matrix_input()
    print ("\n")
    print ("Input for Matrix B")
    B = matrix_input()
    C = matrixmultiply(A, B)
    print ("\n")
    print ("Matrix A: ")
    printmatrix(A)
    print ("Matrix B: ")
    printmatrix(B)
    print ("Matrix C = A * B")
    printmatrix(C)


def main():
    test_matrix_mul()


if __name__ == '__main__':
    main()
