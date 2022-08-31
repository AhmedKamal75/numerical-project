import numpy as np
import sympy


# ag :: augmented_matrix
def forward_elimination(am=None):
    (rows, columns) = am.shape
    for k in range(0, rows - 1, 1):
        am = partial_pivoting(am, k)
        for i in range(k + 1, rows, 1):
            factor = am[i][k] / am[k][k]
            for j in range(0, rows, 1):
                am[i][j] = am[i][j] - factor * am[k][j]
            am[i][columns - 1] = am[i][columns - 1] - factor * am[k][columns - 1]
    return am


def back_substitution(am):
    (rows, columns) = am.shape
    # result = np.array((rows, 1))
    # result.astype(float)
    result = [[0] for _ in range(rows)]

    for i in range(rows - 1, -1, -1):
        s = 0.0
        for j in range(i + 1, rows, 1):
            s = s + am[i][j] * result[j][0]
        result[i][0] = (am[i][columns - 1] - s) / am[i][i]
    return np.array(result)


def partial_pivoting(am, k):
    best_raw = k
    for i in range(k, am.shape[0], 1):
        if abs(am[i][k]) > abs(am[k][k]):
            best_raw = i
    # exchange raw's k <==> i
    if best_raw != k:
        for j in range(0, am.shape[1], 1):
            temp = am[k][j]
            am[k][j] = am[best_raw][j]
            am[best_raw][j] = temp
    return am


def solve(A, b):
    A_b = np.concatenate((A, b), axis=1)
    # return back_substitution(forward_elimination(A_b))
    return back_substitution(
        np.array(sympy.matrices.Matrix(np.concatenate((A, b), axis=1)).echelon_form(with_pivots=True)[0]).astype(float))
