import numpy as np
import matplotlib.pyplot as mpl
from matplotlib.animation import FuncAnimation as an
import math
from decimal import Decimal, getcontext
getcontext().prec = 30

def inscribe(a):
    r = Decimal(1)
    side = 2 * r * Decimal(math.sin(a))
    return side

def circumscribe(a):
    r = Decimal(1)
    side = 2 * r * Decimal(math.tan(a))
    return side

def perimeter(n):
    radians = Decimal(math.radians(180/n))
    side_inscribe = inscribe(radians)
    side_circumscribe = circumscribe(radians)

    perimeter_inscribe = n * side_inscribe
    perimeter_circumscribe = n * side_circumscribe

    return perimeter_inscribe, perimeter_circumscribe

def graph_pi(x, up, low):

    fig,axes = mpl.subplots(figsize=(20, 15))
    axes.set_title("Value of π")
    axes.axhline(y=np.pi,color="g",label="Actual π")
    axes.grid()

    def animate(i):
        if i==0:
            axes.legend(loc=1)
        axes.plot(x[:i],up[:i],color="r",label="Upper Limit π")
        axes.plot(x[:i],low[:i],color="b",label="Lower Limit π")

    ani = an(fig, animate, interval=0.1,repeat=False)
    mpl.show()

def graph_error(x, up, low):

    fig,axes = mpl.subplots(figsize=(20, 15))
    axes.set_title("Error in π")
    axes.grid()

    def animate(i):
        if i==0:
            axes.legend(loc=1)
        axes.plot(x[:i],up[:i],color="r",label="Upper Limit error in π")
        axes.plot(x[:i],low[:i],color="b",label="Lower Limit error in π")

    ani = an(fig, animate, interval=0.1,repeat=False)
    mpl.show()

def compute_pi():

    pi_upper, pi_lower = [], []
    sides = np.linspace(0, 500, num=251, dtype=int)
    sides = sides[2:]
    error_upper, error_lower = [], []

    value_of_pi = Decimal('3.141592653589793238462643383279')

    for i in sides:
        per_ins, per_cir = perimeter(i)
        pi_upper.append(per_cir/2)
        pi_lower.append(per_ins/2)

        error_upper.append(per_cir/2 - value_of_pi)
        error_lower.append(value_of_pi - per_ins/2)

    # print(f"[ {pi_lower[-1]} , {pi_upper[-1]} ]")
    # print(f"[ {error_lower[-1]} , {error_upper[-1]} ]")
    # graph_pi(sides, pi_upper, pi_lower)
    graph_error(sides, error_upper, error_lower)

compute_pi()
