import math
import matplotlib.pyplot as mpl
import scipy.linalg as lg


def nrm(a, K, val):
    x = a
    for _ in range(K):
        x = x - lg.inv(jacobi(x)) @ fun(x)
        val.append(x)
    return val


def fun(x):
    f1 = 3 * x[0] - math.cos(x[1] * x[2]) - (3 / 2)
    f2 = 4 * (x[0]**2) - 625 * (x[1]**2) + 2 * x[2] - 1
    f3 = 20 * x[2] + math.exp(-1 * x[0] * x[1]) + 9
    return [f1, f2, f3]


def jacobi(x):
    j1 = [3, x[2] * math.sin(x[1] * x[2]), x[1] * math.sin(x[1] * x[2])]
    j2 = [8 * x[0], -1250 * x[1], 2]
    j3 = [-x[1] * math.exp(-1 * x[0] * x[1]), -x[0] * math.exp(-1 * x[0] * x[1]), 20]
    return [j1, j2, j3]

def plot(x):
    y = []
    for i in nr:
        v = fun(i)
        y.append(lg.norm(v))    

    mpl.title("||f(xₖ)|| vs Iterations")
    mpl.xlabel("Iteration")
    mpl.ylabel("||f(xₖ)||")
    l = len(x)
    mpl.plot(list(range(l)), y, label="Newton-Raphson Method")
    mpl.legend()
    mpl.grid()
    mpl.show()


itr = 20
a = [1, 2, 3]
nr = nrm(a, itr, [a])
print(f"The root of the function is {nr[-1]}")
plot(nr)
