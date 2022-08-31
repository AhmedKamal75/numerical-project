from sympy import *


def solve(fun, x0=0, iter_max=50, es=0.00001):
    x_1 = x0
    x = Symbol("x")
    f_fprime = lambdify(x, fun(x) / fun(x).diff(x))
    for i in range(iter_max):
        temp_x = x_1
        x_1 = x_1 - f_fprime(x_1)
        if x_1 != 0 and abs(((x_1 - temp_x) * 100.0 / x_1)) < es:
            break
    return x_1
