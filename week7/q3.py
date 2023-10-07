def fun(x, n, a):
    return x**n - a

# Bisection method to find root
def root(n, a, e):
    l, u = 0, a
    v = abs(l - u)
    while v > e:
        mid = (l + u) / 2

        # midpoint is root
        if fun(mid, n, a) == 0:
            return mid

        # midpoint in lower bound
        elif fun(mid, n, a) * fun(l, n, a) >= 0:
            l = mid

        # midpoint in upper bound
        else:
            u = mid

        v = abs(l - u)

    return (l + u) / 2


a = 5
n = 15
e = 1e-3
val = a ** n
k = root(n, val, e)
print(f"The {n}th root of {a} ^ {n} is: {k}")
