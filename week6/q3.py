import numpy as np
import matplotlib.pyplot as mpl
from matplotlib.animation import FuncAnimation as an

# method to return the coordinate for a given theta
def coordinate(L, th):
    return L * np.sin(th), -L * np.cos(th)

# method to apply euler method
def Euler(ode, t, th, a, v):
    h = 0.001
    while t <= 10:
        fn = ode(t, a, v, 10, 0.1)
        v += fn[1] * h
        a += fn[0] * h
        th.append(a)
        t  += h
    return th

# method to solve ode using forward euler method
def ODEsolve(ode):

    th0 = np.pi / 4
    v0 = 0
    t0 = 0
    L = 0.1

    # calling Euler method
    th = Euler(ode, t0, [th0], th0, v0)
    f = mpl.figure()
    ax = f.add_subplot()

    # Initial position
    x0, y0 = coordinate(L, th0)
    (l,) = ax.plot([0, x0], [0, y0], lw=3, c="k")

    # bob
    r = 0.008
    bob = ax.add_patch(mpl.Circle(coordinate(L, th0), r, fc="r", zorder=3))
    p = [l, bob]

    # method to initialize necessary elements
    def init():
        ax.set_title("Simple Gravity Pendulum")
        ax.set_xlim(-L * 1.5, L * 1.5)
        ax.set_ylim(-L * 1.5, L * 1.5)

        return p

    # method to animate the graph
    def animate(i):
        x, y = coordinate(L, th[i])
        l.set_data([0, x], [0, y])
        bob.set_center((x, y))

        return p

    fps = len(th)
    inv = 1
    
    # Starting the animation
    animation = an(
        f,
        animate,
        init_func=init,
        frames=fps,
        repeat=True,
        interval=inv,
        blit=True,
    )
    mpl.grid()
    mpl.show()

# Test Case
ode = lambda t, a, v, g, L: (v, -(g / L) * np.sin(a))
ODEsolve(ode)
