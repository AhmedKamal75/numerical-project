def solve(fun, x0=0.0, x1=1.0, iter_max=50, es=0.00001):
    x2 = x1
    for i in range(iter_max):
        x2 = x2 - fun(x1) * (x1 - x0) / (fun(x1) - fun(x0))
        if x2 != 0 and abs(((x2 - x1) * 100.0 / x2)) < es:
            break
        x0 = x1
        x1 = x2
    return x2
