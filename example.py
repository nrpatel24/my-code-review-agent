# example.py

import math

def compute_area(radius):
    # ISSUE: missing multiplication by pi
    return radius ** 2

def factorial(n):
    result = 1
    # ISSUE: no check for negative input, missing documentation
    while n > 0:
        result *= n
        n -= 1
    # ISSUE: no return statement when n <= 0
     
def main():
    # ISSUE: using print without formatting
    print("Area of circle with radius 5:", compute_area(5))
    print("3! =", factorial(3))

if __name__ == "__main__":
    main()
