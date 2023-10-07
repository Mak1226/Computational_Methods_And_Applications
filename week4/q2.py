import numpy as np
import matplotlib.pyplot as mpl

# method to find the value of sin
def fun(x):
    return np.sin(np.power(x, 2))

# method to find the derivative value of sin
def derv(x):
    return 2 * x * np.cos(np.power(x, 2))

# method to compute the finite difference approx of each point
def diff(func, x, h, val):

    match val:
        case 1:
            return (func(x + h) - func(x)) / h
        case -1:
            return (func(x) - func(x - h)) / h
        case 0:
            return (func(x + h) - func(x - h)) / (2 * h)

# method to plot the graph
def graph(x, f, b, c, s):
    mpl.plot(x, f, label="Forward", c="r")
    mpl.plot(x, b, label="Backward", c="b")
    mpl.plot(x, c, label="Centered", c="g")
    mpl.title(f"Absolute errors of finite diff approx for {s}")
    mpl.xlabel("x  →")
    mpl.ylabel("Absolute error  →")
    mpl.grid()
    mpl.legend()
    mpl.show()


# method to calculate the absolute errors of finite diff approx
def calculate(min, max, h, p):
    s = "sin(x^2)"
    # generating the values to plot
    x = np.linspace(min, max, p)

    # Compute the absolute errors of approx
    yf, yb, yc = [], [], []
    for i in x:
        d = derv(i)
        f = diff(fun, i, h, 1)
        b = diff(fun, i, h, -1)
        c = diff(fun, i, h, 0)
        f = np.abs(f-d)
        b = np.abs(b-d)
        c = np.abs(c-d)
        yf.append(f)
        yb.append(b)
        yc.append(c)

    # Plot the curves for forward, backward, centred
    graph(x, yb, yf, yc, s)
    
calculate(0, 1, 0.01, 1000)
