def fib(n):
    """Print the Fibonnacci series up to n."""
    a = 0
    b = 1
    for i in range(n):
        a, b = a + b, a

    return a
