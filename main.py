import math

def real_numbers():
    """
    Function to perform operations on real numbers.
    """
    while True:
        print("\nOperations on Real Numbers:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Solution of a Quadratic Equation")
        print("6. Return to Front Page")
        choice = int(input("Choose an operation: "))

        if choice == 1:
            num1, num2 = map(float, input("Enter two numbers: ").split())
            print(f"Result: {num1 + num2:.2f}")
        elif choice == 2:
            num1, num2 = map(float, input("Enter two numbers: ").split())
            print(f"Result: {num1 - num2:.2f}")
        elif choice == 3:
            num1, num2 = map(float, input("Enter two numbers: ").split())
            print(f"Result: {num1 * num2:.2f}")
        elif choice == 4:
            num1, num2 = map(float, input("Enter two numbers: ").split())
            if num2 == 0:
                print("Division by zero error!")
            else:
                print(f"Result: {num1 / num2:.2f}")
        elif choice == 5:
            num1, num2, c = map(float, input("Enter coefficients a, b, and c: ").split())
            discriminant = num2 ** 2 - 4 * num1 * c
            if discriminant < 0:
                print("This mode only works for real number roots.")
            else:
                root1 = (-num2 + math.sqrt(discriminant)) / (2 * num1)
                root2 = (-num2 - math.sqrt(discriminant)) / (2 * num1)
                print(f"Roots: {root1:.2f}, {root2:.2f}")
        elif choice == 6:
            return
        else:
            print("Invalid choice. Please try again.")

def complex_numbers():
    """
    Function to perform operations on complex numbers.
    """
    while True:
        print("\nOperations on Complex Numbers:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Complex Conjugate")
        print("6. Solution of a Quadratic Equation")
        print("7. Return to Front Page")
        choice = int(input("Choose an operation: "))

        if 1 <= choice <= 4:
            a, b = map(float, input("Enter real and imaginary parts of the first complex number (a, b): ").split())
            c, d = map(float, input("Enter real and imaginary parts of the second complex number (c, d): ").split())
            if choice == 1:
                real_part = a + c
                imag_part = b + d
                print(f"Result: {real_part:.2f} + {imag_part:.2f}i")
            elif choice == 2:
                real_part = a - c
                imag_part = b - d
                print(f"Result: {real_part:.2f} + {imag_part:.2f}i")
            elif choice == 3:
                real_part = a * c - b * d
                imag_part = a * d + b * c
                print(f"Result: {real_part:.2f} + {imag_part:.2f}i")
            elif choice == 4:
                denom = c ** 2 + d ** 2
                if denom == 0:
                    print("Division by zero error!")
                else:
                    real_part = (a * c + b * d) / denom
                    imag_part = (b * c - a * d) / denom
                    print(f"Result: {real_part:.2f} + {imag_part:.2f}i")
        elif choice == 5:
            a, b = map(float, input("Enter real and imaginary parts of the complex number (a, b): ").split())
            print(f"Complex number: {a:.2f} + {b:.2f}i")
            print(f"Conjugate: {a:.2f} - {b:.2f}i")
        elif choice == 6:
            a, b, c = map(float, input("Enter coefficients a, b, and c of the quadratic equation ax^2 + bx + c = 0: ").split())
            discriminant = b ** 2 - 4 * a * c
            if discriminant >= 0:
                print("This mode only works for complex number roots.")
            else:
                real_part = -b / (2 * a)
                imag_part = math.sqrt(-discriminant) / (2 * a)
                print(f"Complex roots: {real_part:.2f} + {imag_part:.2f}i and {real_part:.2f} - {imag_part:.2f}i")
        elif choice == 7:
            return
        else:
            print("Invalid choice. Please try again.")

def allocate_matrix(rows, cols):
    """
    Function to allocate memory for a matrix.
    """
    return [[0] * cols for _ in range(rows)]

def read_matrix(rows, cols):
    """
    Function to read elements of a matrix.
    """
    matrix = []
    for i in range(rows):
        row = list(map(int, input(f"Enter elements of row {i + 1}: ").split()))
        matrix.append(row)
    return matrix

def display_matrix(matrix):
    """
    Function to display a matrix.
    """
    for row in matrix:
        print(' '.join(map(str, row)))

def matrix_addition(matrix1, matrix2):
    """
    Function to perform matrix addition.
    """
    if len(matrix1) == 1 and len(matrix1[0]) == 1:
        print(f"Result: {matrix1[0][0] + matrix2[0][0]}")
    else:
        result = [[matrix1[i][j] + matrix2[i][j] for j in range(len(matrix1[0]))] for i in range(len(matrix1))]
        display_matrix(result)

def matrix_subtraction(matrix1, matrix2):
    """
    Function to perform matrix subtraction.
    """
    if len(matrix1) == 1 and len(matrix1[0]) == 1:
        print(f"Result: {matrix1[0][0] - matrix2[0][0]}")
    else:
        result = [[matrix1[i][j] - matrix2[i][j] for j in range(len(matrix1[0]))] for i in range(len(matrix1))]
        display_matrix(result)

def matrix_multiplication(matrix1, matrix2):
    """
    Function to perform matrix multiplication.
    """
    if len(matrix1) == 1 and len(matrix1[0]) == 1:
        print(f"Result: {matrix1[0][0] * matrix2[0][0]}")
    else:
        rows1, cols1 = len(matrix1), len(matrix1[0])
        rows2, cols2 = len(matrix2), len(matrix2[0])
        if cols1 != rows2:
            print("The dimensions of matrices are not compatible for multiplication.")
            return
        result = [[sum(matrix1[i][k] * matrix2[k][j] for k in range(cols1)) for j in range(cols2)] for i in range(rows1)]
        display_matrix(result)

def element_wise_multiplication(matrix1, matrix2):
    """
    Function to perform element-wise multiplication of matrices.
    """
    if len(matrix1) == 1 and len(matrix1[0]) == 1:
        print(f"Result: {matrix1[0][0] * matrix2[0][0]}")
    else:
        result = [[matrix1[i][j] * matrix2[i][j] for j in range(len(matrix1[0]))] for i in range(len(matrix1))]
        display_matrix(result)

def transpose_matrix(matrix):
    """
    Function to transpose a matrix.
    """
    if len(matrix) == 1 and len(matrix[0]) == 1:
        print("Transpose Matrix:")
        display_matrix(matrix)
    else:
        transposed = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]
        print("Original Matrix:")
        display_matrix(matrix)
        print("Transpose Matrix:")
        display_matrix(transposed)

def matrices():
    """
    Function to perform operations on matrices.
    """
    while True:
        print("\nOperations on Matrices:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Multiplication by corresponding elements")
        print("5. Transpose Matrix")
        print("6. Return to Front Page")
        choice = int(input("Choose an operation: "))

        if 1 <= choice <= 4:
            m, n = map(int, input("Enter the dimensions (rows and columns) of both matrices: ").split())
            matrix1 = read_matrix(m, n)
            matrix2 = read_matrix(m, n)
            print("Matrix 1:")
            display_matrix(matrix1)
            print("Matrix 2:")
            display_matrix(matrix2)
            if choice == 1:
                matrix_addition(matrix1, matrix2)
            elif choice == 2:
                matrix_subtraction(matrix1, matrix2)
            elif choice == 3:
                matrix_multiplication(matrix1, matrix2)
            else:
                element_wise_multiplication(matrix1, matrix2)
        elif choice == 5:
            m, n = map(int, input("Enter the dimensions (rows and columns) of the matrix: ").split())
            matrix = read_matrix(m, n)
            transpose_matrix(matrix)
        elif choice == 6:
            return
        else:
            print("Invalid choice. Please try again.")

def factorial(n):
    """
    Function to calculate the factorial of a number.
    """
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def series_summation():
    """
    Function to perform series summation.
    """
    while True:
        print("\nOperations on Series Summation:")
        print("1. SinX Series")
        print("2. CosX Series")
        print("3. Exponential Series")
        print("4. Return to Front Page")
        choice = int(input("Choose an option: "))

        if 1 <= choice <= 3:
            x = float(input("Enter the value of x: "))
            if choice == 1 or choice == 2:
                N = int(input("Enter the value of N: "))
                result = 0
                for i in range(N):
                    sign = 1 if i % 2 == 0 else -1
                    term = (sign * x**(2 * i + choice - 2)) / factorial(2 * i + choice - 2)
                    result += term
                print(f"sin({x:.2f}) = {result:.4f}" if choice == 1 else f"cos({x:.2f}) = {result:.4f}")
            else:
                accuracy = float(input("Enter the accuracy: "))
                result = 1
                term = 1
                i = 1
                while abs(term) >= accuracy:
                    term *= x / i
                    result += term
                    i += 1
                print(f"exp({x:.2f}) = {result:.4f}")
        elif choice == 4:
            return
        else:
            print("Invalid choice. Please try again.")

def main():
    """
    Main function to control the program flow.
    """
    while True:
        print("\n--- Multipurpose Computation System ---")
        print("1. Operations on real numbers")
        print("2. Operations on complex numbers")
        print("3. Operations on matrices")
        print("4. Operations on series summation")
        print("5. Quit")
        choice = int(input("Select an option: "))

        if choice == 1:
            real_numbers()
        elif choice == 2:
            complex_numbers()
        elif choice == 3:
            matrices()
        elif choice == 4:
            series_summation()
        elif choice == 5:
            print("Exiting the program.")
            return
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
