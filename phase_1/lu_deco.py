import numpy as np
import scipy as sp


def solve(A, b):
    return np.array(sp.linalg.lu_solve(sp.linalg.lu_factor(A), b.reshape((b.shape[0]))))


def crout(A):
    pass


def doolittle(A):
    P, L, U = sp.linalg.lu(A)
    return L, U


def cho(A):
    try:
        cho_mat = np.linalg.cholesky(A)
    except np.linalg.LinAlgError:
        print("Matrix is not positive definite")
        cho_mat = np.linalg.cholesky(A @ np.transpose(A))
    return cho_mat
