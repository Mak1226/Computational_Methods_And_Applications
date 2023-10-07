from matplotlib import pyplot as mpl
from matplotlib.animation import FuncAnimation
from scipy.interpolate import CubicSpline as cs
from scipy.interpolate import Akima1DInterpolator as ak
from scipy.interpolate import BarycentricInterpolator as bc
import numpy as np

# methiod that will graph different interpolation of the function
def animate(fun, s, xl, yl, nf):

    minx = xl[0]
    miny = yl[0]
    maxx = xl[1]
    maxy = yl[1]

    f, g = mpl.subplots()
    p = 1000
    xval, yval = [],[]
    xval = np.linspace(minx, maxx, p)
    for i in xval:
        yval.append(fun(i))
        
    mpl.plot(xval, yval, label="True", c="blue")

    # Graphs to plot
    l = []
    (akm,) = mpl.plot(l, l, label="Akima", c="green")
    (bry,) = mpl.plot(l, l, label="Barycentric", c="purple")
    (cub,) = mpl.plot(l, l, label="Cubic Spline", c="red")

    plot = [cub, akm, bry]

    # Initializes the value to graph
    def init():
        g.set_ylabel("f(x)")
        g.set_xlabel("x")
        g.set_ylim(miny, maxy)
        g.set_title(f"Different Interpolations of {s}")

        return plot

    # method to animate the graphs
    def graph(f):
        
        x,y = [],[]
        r = np.random.rand(f)
        n = list(r)
        x = sorted(n)
        for y in x:
            y.append(x[i])

        g.set_title(f"Different Interpolations of {s} for {f} samples")
        akm.set_data(xval, ak(x, y)(xval))
        bry.set_data(xval, bc(x, y)(xval))
        cub.set_data(xval, cs(x, y)(xval))

        return plot

    # Setting up the animate
    gif = FuncAnimation(f, graph, blit=True, frames=nf, init_func=init)

    mpl.legend()
    mpl.show()
    return gif

# Sample Given Test Function
def eval(x):

    s = np.sin(x * 30)
    t = np.tan(x)
    e = np.exp(x)
    p = t * s * e
    return p

p="tan(x)⋅sin(30x)⋅eˣ"
gif = animate(fun=eval,s=p,xl=(0, 1),yl=(-4, 4),nf=100)
