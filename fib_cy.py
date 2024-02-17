# cython: profile=True
import cython


def fib(n: cython.int):
    """Print the Fibonnacci series up to n."""

    i: cython.int
    a: cython.ulonglongint = 0
    b: cython.ulonglongint = 1

    for i in range(n):
        a, b = a + b, a

    return a
