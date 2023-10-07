from matplotlib.animation import FuncAnimation as an
import matplotlib.pyplot as mpl
import numpy as np
from scipy.integrate import solve_ivp as ivp

# method to return the normal of vector (v2 - v1)
def normal(v1, v2):
    return max(np.linalg.norm(v2 - v1), 10)

# this method will return the 2nd derivative of system of ode
def derv2(r1, r2, r3):
    d1 = r2 - r1
    d2 = r3 - r1
    n1 = np.power(normal(r2, r1), 3)
    n2 = np.power(normal(r3, r1), 3)

    val = d1/n1 + d2/n2
    return list(val)

# defining the bodies
def body(ax, cor, rad, c, l):
    b = ax.add_patch(mpl.Circle(cor, rad, fc=c, label=l))
    return b

# method to solve ode using forward euler method
def ODEsolve(R, V):

    t0 = 0
    T = 400
    n = 1000

    # method to return the derivates of system of diff. eqn.
    def derv(_, y):
        r1x, r1y, r2x, r2y, r3x, r3y, v1x, v1y, v2x, v2y, v3x, v3y = y
        v1 = [v1x, v1y]
        v2 = [v2x, v2y]
        v3 = [v3x, v3y]
        r1 = np.array([r1x, r1y])
        r2 = np.array([r2x, r2y])
        r3 = np.array([r3x, r3y])
        d1 = derv2(r1, r2, r3)
        d2 = derv2(r2, r3, r1)
        d3 = derv2(r3, r1, r2)
        return [*v1, *v2, *v3, *d1, *d2, *d3]

    t = np.linspace(t0, T, n)

    # solving using the solve_ivp method of scipy library
    sol = ivp(fun=derv, t_span=[t0, T], y0=[*R, *V], t_eval=t)

    r1x, r1y, r2x, r2y, r3x, r3y, *vs = sol.y
    f = mpl.figure()
    ax = f.add_subplot()

    r = 0.1
    b1 = body(ax, (r1x[0], r1y[0]), r, "r", "Point_1")
    b2 = body(ax, (r2x[0], r2y[0]), r, "b", "Point_2")
    b3 = body(ax, (r3x[0], r3y[0]), r, "g", "Point_3")

    p = [b1, b2, b3]

    # method to initialize necessary elements
    def init():
        ax.set_title("Three-Body Problem")
        ax.set_xlim(-2, 6)
        ax.set_ylim(-4, 4)
        ax.set_xlabel("x")
        ax.set_ylabel("y")

        return p

    # method to animate the graph
    def animate(i):
        # Update the positions of the circles
        b1.set_center((r1x[i], r1y[i]))
        b2.set_center((r2x[i], r2y[i]))
        b3.set_center((r3x[i], r3y[i]))

        return p

    fps = len(r1x)
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
    mpl.legend()
    mpl.show()

# Test Case
r10 = [0, 0]
r20 = [3, 1.73]
r30 = [3, -1.73]
v10 = [0, 0]
v20 = [0, 0]
v30 = [0, 0]
R = [*r10, *r20, *r30]
V = [*v10, *v20, *v30]
ODEsolve(R, V)