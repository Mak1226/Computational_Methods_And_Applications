import math
import matplotlib.pyplot as mpl


def fun(x):
    return x * math.exp(x)


def derv(x):
    return math.exp(x) * (1 + x)


def nrm(a, K, val):
    x = a
    for _ in range(K):
        v = fun(x) / derv(x)
        x -= v
        val.append(x)
    return val


def sm(b, K, val):
    x = b
    for _ in range(K):
        v = fun(x) * ((x - val[-2]) / (fun(x) - fun(val[-2])))
        x -= v
        val.append(x)
    return val


def converge(val):
    A = []
    l = len(val) - 1
    for i in range(2, l):
        num = abs((val[i + 1] - val[i]) / (val[i] - val[i - 1]))
        den = abs((val[i] - val[i - 1]) / (val[i - 1] - val[i - 2]))
        A.append(math.log(num) / math.log(den))

    return A


def plot(a_nr, a_s):
    mpl.title("Rate of Convergence")
    mpl.ylabel("Alpha")
    mpl.xlabel("Iteration")
    nr = len(a_nr) + 2
    s = len(a_s) + 2
    mpl.plot(list(range(2, nr)), a_nr, label="Newton-Raphson Method")
    mpl.plot(list(range(2, s)), a_s, label="Secant Method")
    mpl.legend()
    mpl.grid()
    mpl.show()


itr = 212
a = 200
b = 201
nr_m = nrm(a, itr, [a])
s_m = sm(b, itr - 1, [a, b])

a_nr = converge(nr_m)
a_s = converge(s_m)

plot(a_nr, a_s)
