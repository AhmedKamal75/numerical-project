import numpy as np


def solve(A, b, X_init=None, iterations=100, goal_relative_error=0.05):
    if X_init is None:
        X_init = [0 for _ in range(A.shape[0])]
    X = np.array(X_init, dtype=float)
    Xs = [X.tolist()]
    for i in range(iterations):
        for i in range(len(X)):
            s = 0
            for j in range(len(X)):
                if i != j:
                    s = s + A[i][j] * X[j]
            X[i] = (b[i][0] - s) / A[i][i]
            Xs.append(X.tolist())
        # Xs.append(X.tolist())
        if absolute_relative_approximate_error(Xs[-1], Xs[-2], goal_relative_error):
            break
    return Xs


def absolute_relative_approximate_error(x_new, x_old, goal_relative_error):
    if len(x_new) != len(x_old):
        return False
    ok = True
    for i in range(len(x_new)):
        temp_error = (x_new[i] - x_old[i]) * 100.0 / x_new[i]
        if temp_error >= goal_relative_error:
            ok = False

    return ok
