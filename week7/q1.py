from matplotlib.animation import FuncAnimation as an
import matplotlib.pyplot as mpl
import numpy as np

def tridiagonal(n, a, b, c):
    x = np.eye(n,k=-1) * a
    y = np.eye(n,k=0) * b
    z = np.eye(n,k=1) * c
    t = x + y + z
    return t

# 1D heat eqn
def onedim():

    uT0 = lambda x: np.exp(-x)
    u0 = lambda t: 0
    uL = lambda t: 0
    f = lambda x, t: 0
    L = 1
    mu = 5 * (10 ** (-5))
    T = 2000
    h = 0.01
    ht = 0.5

    v1 = int(L // h)
    v2 = int(T // ht)
    Nx = v1 + 2
    Nt = v2 + 2

    xs = np.linspace(0, L, Nx)
    ts = np.linspace(0, T, Nt)
    us = np.array([uT0(x) for x in xs])

    # Initialize the tri-diagonal matrix A
    A = tridiagonal(Nx, 1, -2, 1)
    res = [us]
    itr = ts[1:]

    for t in itr:
        for i in xs:
            fMat = np.array(f(i,t))

        v1 = mu / np.power(h,2)
        v2 = A @ us
        du = v1 * v2 + fMat
        us = us + ht * du

        us[0] = u0(t)
        us[-1] = uL(t)

        res.append(us)

    anime(res,xs,L,mu,False)
    anime(res,xs,L,mu,True)

# method to plot animation
def anime(u, xs, L, mu, show_graph):
    fig = mpl.figure()
    ax = mpl.axes()
    pt = []

    if show_graph:
        (p1,) = mpl.plot(xs, u[0])
        pt.append(p1)
    else:
        p1 = mpl.imshow([u[0]], cmap="hot", aspect="auto", animated=True)
        cb = fig.colorbar(p1)
        cb.set_label("Temperature")
        pt.append(p1)
    
    ax.set_title(f"Heat conduction in a rod\n with L = {L} and μ = {mu}")

    if not show_graph:
        ax.get_xaxis().set_ticks([])
        ax.get_yaxis().set_ticks([])

    def animate(i):
        # Update the plot
        if show_graph:
            p1.set_data(xs, u[i])
        else:
            p1.set_array([u[i]])

    anim = an(
        fig,
        func=animate,
        frames=len(u),
        repeat=False,
        interval=1,
    )
    mpl.show()

onedim()
