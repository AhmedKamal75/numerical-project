def solve(xl, xu, func, steps=50, goal_relative_error=0.00001):
    result = xl
    for i in range(steps):
        xr = (xl + xu) / 2
        if func(xl) * func(xr) < 0:
            xl, xu = xl, xr
        elif func(xr) * func(xu) < 0:
            xl, xu = xr, xu
        # print(f"step #{i}::: root = {xr}")
        if xr != 0.0 and abs((xr - result) * 100 / xr) < goal_relative_error:
            result = xr
            break
        result = xr
    return result
