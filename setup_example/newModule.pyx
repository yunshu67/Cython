cdef extern from "impl_in_C.h":
    int fib(int n)

def pyfib(n=int):
    return fib(n)







