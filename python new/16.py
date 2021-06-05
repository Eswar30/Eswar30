#  Recursions

# factorial using iterative
def factorial_iterative(n):
    """
    Logic:
        :param n: Integer
        :return: n * n-1 * n-2 * n-3.......1
    """
    fac = 1
    for i in range(n):
        fac = fac * (i+1)
    return fac
num = int(input("Enter the number:  "))
print(factorial_iterative(num))

# factorial using Recurasive
def factorial_recurasve(n):
    """
    Logic:
    if n = 5 
    5 * factoral_recurasve(4)
    5 * 4 * factoral_recurasve(3)
    5 * 4 * 3 * factoral_recurasve(2)
    5 * 4 * 3 * 2 * factoral_recurasve(1)
    5 * 4 * 3 * 2 * 1 = 120 # as factorial_recurasve becomes 1 it returns the value
    """
    if n == 1:
        return 1
    else:
        return n * factorial_recurasve(n-1)
print(factorial_recurasve(num))