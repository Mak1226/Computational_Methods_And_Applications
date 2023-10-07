import numpy as np
import matplotlib.pyplot as mpl

# method to return the value of function for a given x
def fun(x):
    return 2 * x * np.exp(np.power(x, 2))

# method to return the value of integral for a given x
def integral(x):
    return np.exp(np.power(x, 2))

# method to plot the graph
def graph(area, x, y, s):
    mpl.title(f"Approximate area under the graph: {s}")
    mpl.axhline(y=area, color="r", label="Exact Area")
    mpl.xlabel("Total intervals  →")
    mpl.plot(x, y, label="Approx Area")
    mpl.ylabel("Area  →")
    mpl.grid()
    mpl.legend()
    mpl.show()

# method to calculate the area under the curve using trapezoid formula
def calculate(p):

    s = "2*x*e^(x^2)"
    a, b = 1, 3
    x, y = [], []
    # Exact area
    real = integral(b) - integral(a)

    for i in range(1, p + 1):
        # Width of each interval
        h = (b - a) / i
        # Area of first trapezoid
        area = (fun(a) + fun(b)) * h / 2
        for j in range(1, i):
            # x-coordinate of right endpoint of kth interval
            k = a + (j * h)
            # Area of kth trapezoid
            area += h * fun(k)

        # initializing (x,y)
        x.append(i)
        y.append(area)

    graph(real, x, y, s)

calculate(100)
