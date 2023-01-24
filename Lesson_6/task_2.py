def factorial(n: int) -> int:
    """This is recursion function
     to find the factorial(n)"""
    if n > 0:  # Base condition
        return factorial(n-1) * n
    return 1


print(factorial(5))
