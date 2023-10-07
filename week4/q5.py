import numpy as np
import matplotlib.pyplot as mpl
import scipy as sp

# method to calculate the the value
def fun(x):
    return 2 * x * np.exp(np.power(x, 2))

# method to calculate the integral of the value
def integral(x):
    return np.exp(np.power(x, 2))

def graph(i, a, t, q, s, r, st):
    mpl.title("Integral of: " + st)
    mpl.xlabel("x  →")
    mpl.ylabel("Area  →")
    mpl.plot(i, q, label="General Purpose Integration Rule")
    mpl.plot(i, r, label="Romberg Integration")
    mpl.plot(i, t, label="Trapezoidal Rule")
    mpl.plot(i, s, label="Simpson's Rule")
    mpl.plot(i, a, label="Actual Area")
    mpl.legend()
    mpl.grid()
    mpl.show()

# method to plot the approx area under the graph using different integral methods
def calculate(max):
    min = 0
    st = "2*x*e^(x^2)"
    p = 1000
    # excluding the 1st point or min
    h = np.linspace(min, max, p)
    u = []
    for i in range(0, len(h)):
        if i:
            u.append(h[i])
    
    a, t, q, s, r = [], [], [], [],[]

    # calculating the area under the graph using different integral methods
    for i in u:
        # initializing the coordinates
        x = np.linspace(min, i, p)
        y = [fun(k) for k in x]

        # Using different methods to calculate the area under the graph
        a.append(integral(i)-integral(min))
        t.append(sp.integrate.trapezoid(y, x))
        q.append(sp.integrate.quad(fun, min, i)[0])
        s.append(sp.integrate.simpson(y, x))
        r.append(sp.integrate.romberg(fun, min, i))

    graph(u, a, t, q, s, r, st)

calculate(0.2)
