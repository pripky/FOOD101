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
def slope_of_cubic(coefficients, x):
    #Let the four coefficients of the cubic polynomial be a, b, c and d.
    #d won't contribute to slope calculation.
    a, b, c, d = coefficients
    #differentiating the polynomial wrt x gives us the slope at a given value of x
    slope = 3 * a * x**2 + 2 * b * x + c
    return slope


coefficients = (2, -1, 1, 3)
x = 3
answer = slope_of_cubic(coefficients, x)
print(f"The slope of the cubic polynomial at x = {x} is {answer}")
