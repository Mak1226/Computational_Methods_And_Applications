from matplotlib import projections
from matplotlib.animation import FuncAnimation as an
from mpl_toolkits import mplot3d
import matplotlib.pyplot as mpl
import numpy as np


def tridiagonal(n, a, b, c):
    x = np.eye(n, k=-1) * a
    y = np.eye(n, k=0) * b
    z = np.eye(n, k=1) * c
    t = x + y + z
    return t

# 2D heat eqn


def twodim():

    def f(x, y, t, xc, yc): return np.exp(-np.sqrt(((x - xc) ** 2) + ((y - yc) ** 2)))
    def uT0(x, y): return 0
    def uB(t): return 0
    xc, yc = 0.5, 0.5
    mu = 5 * (10 ** (-5))
    T = 200
    h = 0.01
    ht = 0.5
    xn, xm = 0, 1
    yn, ym = 0, 1

    n = int((xm - xn) // h) + 2
    xs = np.linspace(xn, xm, n)
    ys = np.linspace(yn, ym, n)

    nt = int(T//ht) + 2
    ts = np.linspace(0, T, nt)

    us = np.array([[uT0(i, j) for j in ys] for i in xs])

    A = tridiagonal(n, 1, -2, 1)
    result = [us]
    itr = ts[1:]

    for t in itr:
        fMat = np.array([[f(x, y, t, xc, yc) for y in ys] for x in xs])

        v1 = mu / np.power(h, 2)
        v2 = (A @ us) + (us @ A)
        du = v1 * v2 + fMat
        us = us + ht * du

        for i in range(n):
            us[i][0] = uB(t)
            us[i][-1] = uB(t)

        for i in range(n):
            us[0][i] = uB(t)
            us[-1][i] = uB(t)

        result.append(us)

    anime(result, xs, ys, 0, 1, 0, 1, mu, False)
    anime(result, xs, ys, 0, 1, 0, 1, mu, True)

# method to plot animation
def anime(u, xs, ys, xn, xm, yn, ym, mu, show_graph):
    fig = mpl.figure()
    ax = mpl.axes()
    pt = []

    if show_graph:
        ax = mpl.axes(projection="3d")
    else:
        ax = mpl.axes()

    if show_graph:
        a, b = np.meshgrid(xs, ys)
        ax.plot_surface(
            a,
            b,
            u[0],
            cmap="hot",
            linewidth=0,
            antialiased=False,
        )

    else:
        p = mpl.imshow(
            u[-1],
            cmap="hot",
            origin="lower",
            extent=[xn, xm, yn, ym],
            aspect=xm,
            animated=True,
        )
        cb = fig.colorbar(p)
        cb.set_label("Temperature")
        pt.append(p)

    ax.set_title(
        f"Heat conduction in a sheet\n with boundary [{xn}, {xm}]x[{yn}, {ym}] and μ = {mu}")

    if not show_graph:
        ax.get_xaxis().set_ticks([])
        ax.get_yaxis().set_ticks([])

    def animate(i):
        if show_graph:
            ax.plot_surface(
                a,
                b,
                u[i],
                cmap="hot",
                linewidth=0,
                antialiased=False,
            )
        else:
            p.set_array(u[i])

        return pt

    anim = an(
        fig,
        func=animate,
        frames=len(u),
        repeat=False,
        interval=1,
    )
    mpl.show()


twodim()
