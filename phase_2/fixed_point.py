from sympy import *


def solve(g, x0=1.0, x_from=1.0, x_to=1.0, iter_max=50, es=0.00001):
    if not validate(g, x_from=x_from, x_to=x_to):
        return "not applicable"
    x = x0
    for i in range(iter_max):
        temp_x = x
        x = g(x)
        if x != 0 and abs(((x - temp_x) * 100.0 / x)) < es:
            break
    return x


def validate(g, x_from=1.0, x_to=2.0):
    x = Symbol("x")
    f = lambdify(x, g(x).diff(x))
    x_delta = (x_to - x_from) / 100
    for i in range(100):
        if abs(f(x_from + x_delta * i)) > 1.0:
            return False
    return True
