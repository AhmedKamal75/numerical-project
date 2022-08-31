import numpy as np
import sympy


def solve(A, b):
    M = sympy.matrices.Matrix(np.concatenate((A, b), axis=1)).rref()[0]
    return np.array(M.col(-1))
