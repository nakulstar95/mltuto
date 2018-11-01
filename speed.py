import numba
import numpy as np
from timeit import timeit

def pyMult(A,B): # very simple/crude matrix multiplication
    m,n = A.shape
    p,q = B.shape
    if n != p: print("ERROR: invalid dimensions: %d != %d",n,p)
    C=np.empty((m,q))
    for i in range(m):
        for j in range(q):
            c=0
            for k in range(n): c += A[i][k]*B[k][j]
            C[i][j]=c
    return C

## Here we mark a function as being "just-in-time compiled" (jit)
## In addition we tell the compiler that this is a function that
## - has two arguments that are 64bit floating point matrices
## - returns a 64 bit floating point matrix
## - no interpreted python should be used (nopython=True)
## The arguments in brackets are optional (@numba.jit is sufficient)
@numba.jit(numba.float64[:,:](numba.float64[:,:],numba.float64[:,:]),nopython=True)
def jitMult(A,B):
    m,n = A.shape
    p,q = B.shape
    if n != p: print("ERROR: invalid dimensions: %d != %d",n,p)
    C=np.empty((m,q))
    for i in range(m):
        for j in range(q):
            c=0
            for k in range(n): c += A[i][k]*B[k][j]
            C[i][j]=c
    return C
mat=lambda m,n: np.random.rand(m,n)
print("Normal python %.4f sec" % timeit(lambda: pyMult(mat(100,200),mat(200,50)),number=9))
print("JIT    python %.4f sec" % timeit(lambda:jitMult(mat(100,200),mat(200,50)),number=9))
print("Numpy C code  %.4f sec" % timeit(lambda: np.asmatrix(mat(100,200))*np.asmatrix(mat(200,50)), number=9))