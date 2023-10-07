import numpy as np
import matplotlib.pyplot as mpl

# method of evaluate the sin of the value
def fun(x):
    return np.sin(np.power(x,2))

# method to evaluate derivative of the sin at that value
def derv(x):
    return 2 * x * np.cos(np.power(x,2))

# method to calculate forward difference approx.
def frwd_diff(x,h):
        return (fun(x + h) - fun(x)) / h

# method to plot graph
def graph(x,act,app):
    mpl.title("Actual derivative f'(x) vs Forward difference approx δ+")
    mpl.xlabel("x  →")
    mpl.ylabel("f'(x) and δ+  →")
    mpl.plot(x, act, c="r", label="f'(x)")
    mpl.plot(x, app, c="b", label="δ+")
    mpl.grid()
    mpl.legend()
    mpl.show()

# method to calculate the actual and approx derivatives
def calculate(h, min, max):

    # linspaceis used to generate the values to plot
    x = np.linspace(min, max, 1000)

    # Calculate the actual and approx derivative values
    act,app= [],[]

    for i in x:
        t = derv(i)
        act.append(t)
        p = frwd_diff(i,h)
        app.append(p)

    graph(x,act,app)

calculate(0.01, 0, 1)

