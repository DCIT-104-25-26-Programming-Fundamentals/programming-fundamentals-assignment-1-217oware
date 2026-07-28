# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 4
# Topic: Multi-dimensional Arrays (2D Lists), Nested Loops, and Functions
# =============================================================================
#
# TASK: Matrix Operations
#
# Write a Python program that performs three operations on matrices (2D lists),
# each implemented in its own function.
#
# -----------------------------------------------------------------------------
# PART A — Transpose a Matrix
# -----------------------------------------------------------------------------
# - Read an M x N matrix from the user.
# - Compute and display its transpose (rows become columns, columns become rows).
#
# Example (2 x 3 input):
#
#   Original Matrix:      Transposed Matrix:
#   1  2  3               1  4
#   4  5  6               2  5
#                         3  6
#
# -----------------------------------------------------------------------------
# PART B — Add Two Matrices
# -----------------------------------------------------------------------------
# - Read two matrices of exactly the same size (M x N).
# - Compute their element-wise sum and display the result.
#   (Each position in the result = the sum of the values at that position
#    in both matrices.)
#
# -----------------------------------------------------------------------------
# PART C — Multiply Two Matrices
# -----------------------------------------------------------------------------
# - Read matrix A of size M x N and matrix B of size N x P.
#   (The number of COLUMNS in A must equal the number of ROWS in B.)
# - Compute and display the matrix product A × B (result is M x P).
#
# -----------------------------------------------------------------------------
# EXPECTED INPUT FORMAT
# -----------------------------------------------------------------------------
# When entering a row, the user types all values on one line separated by spaces:
#
#   Enter number of rows: 2
#   Enter number of columns: 3
#   Enter row 1: 1 2 3
#   Enter row 2: 4 5 6
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - Use nested loops for all operations (no NumPy or other libraries).
# - Each operation must be in its own function (see scaffold below).
# - Display each matrix in a neat, aligned grid format.
# - Tip: Complete Part A first, then Parts B and C.
#

#
# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 4
# Topic: Multi-dimensional Arrays (2D Lists), Nested Loops, and Functions
# =============================================================================
#
# TASK: Matrix Operations
# =============================================================================


def read_matrix(rows, cols, label="matrix"):
    matrix = []
    for i in range(rows):
        while True:
            entry = input(f"Enter row {i + 1} of {label}: ").split()
            if len(entry) != cols:
                print(f"Error: please enter exactly {cols} numbers.")
                continue
            row = [float(value) for value in entry]
            matrix.append(row)
            break
    return matrix


def display_matrix(matrix):
    for row in matrix:
        formatted_row = "  ".join(f"{value:g}" for value in row)
        print(formatted_row)


def transpose_matrix(matrix):
    rows = len(matrix)
    cols = len(matrix[0])

    result = []
    for j in range(cols):
        new_row = []
        for i in range(rows):
            new_row.append(matrix[i][j])
        result.append(new_row)
    return result


def add_matrices(matrix_a, matrix_b):
    rows = len(matrix_a)
    cols = len(matrix_a[0])

    result = []
    for i in range(rows):
        new_row = []
        for j in range(cols):
            new_row.append(matrix_a[i][j] + matrix_b[i][j])
        result.append(new_row)
    return result


def multiply_matrices(matrix_a, matrix_b):
    m = len(matrix_a)
    n = len(matrix_a[0])
    p = len(matrix_b[0])

    result = []
    for i in range(m):
        new_row = []
        for j in range(p):
            total = 0
            for k in range(n):
                total += matrix_a[i][k] * matrix_b[k][j]
            new_row.append(total)
        result.append(new_row)
    return result


def part_a_transpose():
    print("\n--- Part A: Transpose a Matrix ---")
    rows = int(input("Enter number of rows: "))
    cols = int(input("Enter number of columns: "))

    matrix = read_matrix(rows, cols)

    print("\nOriginal Matrix:")
    display_matrix(matrix)

    result = transpose_matrix(matrix)

    print("\nTransposed Matrix:")
    display_matrix(result)


def part_b_add():
    print("\n--- Part B: Add Two Matrices ---")
    rows = int(input("Enter number of rows: "))
    cols = int(input("Enter number of columns: "))

    print("\nMatrix A:")
    matrix_a = read_matrix(rows, cols, "matrix A")

    print("\nMatrix B:")
    matrix_b = read_matrix(rows, cols, "matrix B")

    result = add_matrices(matrix_a, matrix_b)

    print("\nSum (A + B):")
    display_matrix(result)


def part_c_multiply():
    print("\n--- Part C: Multiply Two Matrices ---")
    m = int(input("Enter rows of matrix A: "))
    n = int(input("Enter columns of matrix A (= rows of matrix B): "))
    p = int(input("Enter columns of matrix B: "))

    print("\nMatrix A:")
    matrix_a = read_matrix(m, n, "matrix A")

    print("\nMatrix B:")
    matrix_b = read_matrix(n, p, "matrix B")

    result = multiply_matrices(matrix_a, matrix_b)

    print("\nProduct (A x B):")
    display_matrix(result)


def main():
    print("Matrix Operations")
    print("1. Transpose a Matrix (Part A)")
    print("2. Add Two Matrices (Part B)")
    print("3. Multiply Two Matrices (Part C)")
    choice = input("Choose an operation (1-3): ")

    if choice == "1":
        part_a_transpose()
    elif choice == "2":
        part_b_add()
    elif choice == "3":
        part_c_multiply()
    else:
        print("Error: invalid choice.")


if __name__ == "__main__":
    main()
# =============================================================================

