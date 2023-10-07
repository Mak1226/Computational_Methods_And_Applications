import numpy as np
import matplotlib.pyplot as mpl
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
    mpl.title("Value of π")
    mpl.axhline(y=np.pi, color="g", label="Actual π")
    mpl.plot(x, up,  color="r", label="Upper Limit π")
    mpl.plot(x, low, color="b", label="Lower Limit π")

    mpl.grid()
    mpl.legend()
    mpl.show()

def graph_error(x, up, low):
    mpl.title("Error in π")
    mpl.plot(x, up,  color="r", label="Upper Limit Error in π")
    mpl.plot(x, low, color="b", label="Lower Limit Error in π")

    mpl.grid()
    mpl.legend()
    mpl.show()

def compute_pi():

    pi_upper, pi_lower = [], []
    sides = np.linspace(0, 10000000, num=5000001, dtype=int)
    sides = sides[2:]
    error_upper, error_lower = [], []

    value_of_pi = Decimal('3.141592653589793238462643383279')

    for i in sides:
        per_ins, per_cir = perimeter(i)
        pi_upper.append(per_cir/2)
        pi_lower.append(per_ins/2)

        error_upper.append(per_cir/2 - value_of_pi)
        error_lower.append(value_of_pi - per_ins/2)

    print(f"[ {pi_lower[-1]} , {pi_upper[-1]} ]")
    print(f"[ {error_lower[-1]} , {error_upper[-1]} ]")
    # graph_pi(sides, pi_upper, pi_lower)
    # graph_error(sides, error_upper, error_lower)

compute_pi()
