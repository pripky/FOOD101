#-------------------------------------------------------------------------------
# Name:        module3
# Purpose:
#
# Author:      ASUS
#
# Created:     17/12/2024
# Copyright:   (c) ASUS 2024
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()
import numpy as np

def matrix_operation(array1, array2, operation):
    try:
        if operation == "dot":
            # dot product
            return np.dot(array1, array2)

        elif operation == "matrix":
            # matrix multiplication
            return np.matmul(array1, array2)

        elif operation == "determinant":
            # determinants
            det1 = np.linalg.det(array1) if array1.shape[0] == array1.shape[1] else "Not a square matrix"
            det2 = np.linalg.det(array2) if array2.shape[0] == array2.shape[1] else "Not a square matrix"
            return det1, det2

        else:
            raise ValueError("Invalid operation.Choose between 'dot', 'matrix', and 'determinant'.")
    except ValueError as ve:
        return str(ve)
    except Exception as e:
        return f"An error occurred: {str(e)}"

# Example
array1 = np.array([[1, 2], [3, 4]])
array2 = np.array([[4, 3], [2, 1]])


print("Dot product:", matrix_operation(array1, array2, "dot"))
print("Matrix multiplication:", matrix_operation(array1, array2, "matrix"))
print("Determinants:", matrix_operation(array1, array2, "determinant"))