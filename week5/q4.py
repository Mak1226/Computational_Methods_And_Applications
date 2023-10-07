import numpy as np
import matplotlib.pyplot as mpl
import scipy.integrate as sp

# code of Polynomal class from Assignment 4


class Polynomal:

    def temp(self, len):
        t = []
        for i in range(len):
            t.append(0)
        return t

    def calc(self, val, op, len, num):
        if op == 1:
            t = [self.cf[i] + val.cf[i] for i in range(len)]
        elif op == 2:
            t = [self.cf[i] - val.cf[i] for i in range(len)]
        elif op == 3:
            t = [num * self.cf[i] for i in range(len)]
        return t

    def __init__(self, lt):
        self.cf = lt
        self.len = len(self.cf)
        self.t = "NULL"

    def __str__(self):

        val = " ".join(str(i) for i in self.cf)
        s = "Coefficients of the polynomial are:\n" + val
        return s

    def __getitem__(self, x):
        ans = 0
        n = len(self.cf)
        i = 0
        while i < n:
            v = np.power(x, i) * self.cf[i]
            i += 1
            ans += v

        return ans

    def __add__(self, val):

        d = val.len - self.len
        flag = True if d > 0 else False

        if flag:
            k = self.cf
            for i in range(d):
                k.append(0)
            self = Polynomal(k)
        else:
            k = val.cf
            for i in range(-d):
                k.append(0)
            val = Polynomal(k)

        t = self.temp(self.len)
        tp = self.calc(val, 1, len(t), None)
        return Polynomal(tp)

    def __sub__(self, val):

        d = val.len - self.len
        flag = True if d > 0 else False

        if flag:
            k = self.cf
            for i in range(d):
                k.append(0)
            self = Polynomal(k)
        else:
            k = val.cf
            for i in range(-d):
                k.append(0)
            val = Polynomal(k)

        t = self.temp(self.len)

        tp = self.calc(val, 2, len(t), None)
        return Polynomal(tp)

    def __mul__(self, num):
        if isinstance(self, Polynomal) and isinstance(num, Polynomal):
            d = self.len - num.len
            flag = True if d > 0 else False

            if flag:
                for i in range(d):
                    num.cf.append(0)
            else:
                for i in range(-d):
                    self.cf.append(0)

            sum = self.len + num.len
            t = self.temp(sum)

            for i in range(self.len):
                for j in range(num.len):
                    t[i+j] += num.cf[j] * self.cf[i]

            while (not t[-1]):
                t.pop()
            return Polynomal(t)

        t = self.temp(self.len)

        tp = self.calc(None, 3, self.len, num)
        return Polynomal(tp)

    def __rmul__(self, p):
        return self.__mul__(p)

    def __radd__(self, v):
        return self.__add__(v)

    def __pow__(self, n):
        ans = Polynomal([1])
        for _ in range(n):
            ans *= self

        return ans

    def __rpow__(self, n):
        return self.__pow__(n)

    def plot(self, x, y):
        ay = []
        ax = list(np.linspace(x, y, num=50))
        for i in ax:
            ay.append(self[i])

        mpl.plot(ax, ay, color='b')

        if self.t == 'fitMat':
            mpl.title("Interpolation using matrix method")
        elif self.t == 'fitLag':
            mpl.title("Interpolation using Lagrange polynomial")
        elif self.t == 'NULL':
            s = f"Plot of the polynomial ({self.cf[0]}) "
            for i in range(1, len(self.cf)):
                s += '+(' + str(self.cf[i]) + ') x^' + str(i)
            mpl.title(s)

        mpl.ylabel("p(x)")
        mpl.xlabel("x")
        mpl.grid()
        mpl.legend()
        mpl.show()

    def fitViaMatrixMethod(self, lt):
        num = len(lt)

        A, B, x, y = [], [], [], []
        min = np.inf
        max = -np.inf

        l = 0
        while l < len(lt):
            t = []
            m, n = lt[l]
            if m < min:
                min = m
            if m > max:
                max = m
            for k in range(num):
                v = np.power(m, k)
                t.append(v)
            x.append(m)
            y.append(n)
            A.append(t)
            B.append([n])
            l += 1

        inv = np.linalg.inv(A)
        ra = np.dot(inv, A)
        rb = np.dot(inv, B)

        [[ra[i][j] for j in range(num)] for i in range(num)]

        final = [i[0] for i in rb]
        mat = Polynomal(final)
        mat.t = 'fitMat'
        mpl.scatter(x, y, color='r')
        mat.plot(min, max)

    def fitViaLagrangePoly(self, lt):
        num = len(lt)
        lp, x, y = [], [], []

        min = np.inf
        max = -np.inf

        i = 0
        while i < num:
            t = lt[i]
            m, n = t[0], t[1]
            j = n

            if m < min:
                min = m

            if m > max:
                max = m

            x.append(m)
            y.append(j)
            i += 1

        for i in range(num):
            t = Polynomal([])
            for j in range(num):
                if i == j:
                    continue
                else:
                    a = (-lt[j][0]) / (lt[i][0] - lt[j][0])
                    b = 1 / (lt[i][0] - lt[j][0])
                    val = Polynomal([a, b])
                    if t.len:
                        t *= val
                    else:
                        t += val
            lp.append(t)

        fp = lt[0][1]*lp[0]
        for i in range(1, len(lt)):
            fp += lt[i][1] * lp[i]

        fp.t = "fitLag"
        mpl.scatter(x, y, color='r')
        fp.plot(-1, 3)

    # method to return the coefficient of derivative of polynomial
    def derivative(self):

        r = []
        for i in range(1, len(self.cf)):
            r.append(i * self.cf[i])
        return Polynomal(r)

    # method to return the coefficient of integral of polynomial
    def integral(self):

        r = [0]
        for i in range(len(self.cf)):
            r.append(self.cf[i] / (i + 1))
        return Polynomal(r)

    # method to return the area under the curve
    def area(self, a, b):

        if a > b:
            raise Exception('Invalid input, expected b>=a')
        ip = self.integral()
        return f"Area in the interval [{a}, {b}] is: {(ip[b] - ip[a]):.3f}"

    def show(self, a, b, s1, s2, s3):
        mapper = {
            "0": "\u2070",
            "1": "\u00B9",
            "2": "\u00B2",
            "3": "\u00B3",
            "4": "\u2074",
            "5": "\u2075",
            "6": "\u2076",
            "7": "\u2077",
            "8": "\u2078",
            "9": "\u2079"
        }

        s = ""
        for i in range(len(self.cf)):
            match self.cf[i]:
                case 0:
                    continue
                case default:
                    if not i:
                        s += str(round(self.cf[i], 2)) + " "
                    else:
                        z = ""
                        if self.cf[i] > 0:
                            z = "+"
                        s += z + \
                            str(round(self.cf[i], 2)) + "x" + mapper[str(i)] + " "

        # Plotting computed polynomial
        px = min(a, b)
        py = max(a, b)
        p = 100
        xp = list(np.linspace(px, py, p))
        yp = [self[i] for i in xp]

        K = "Best fit polynomial:\n" + s
        mpl.title(K)
        mpl.xlabel(s1)
        mpl.ylabel(s2)
        mpl.plot(xp, yp, c='blue', label=s3)
        mpl.grid()
        mpl.legend()
        mpl.show()

    # method to compute the best fit polynomial for the given points
    def bestPoint(self, pt, n):

        if n < 0:
            raise Exception("Expected a non-negative integer")

        # Number of points
        m = len(pt)

        # Placing the coordinates into different lists.
        x, y = [], []
        for i in pt:
            x.append(i[0])
            y.append(i[1])

        # Creating b vector
        b = []
        for i in range(n + 1):
            add = 0
            for j in range(m):
                add += y[j] * np.power(x[j], i)
            b.append(add)

        # Creating matrix S
        S = []
        for i in range(n + 1):
            r = []
            for j in range(n + 1):
                add = 0
                for k in range(m):
                    add += np.power(x[k], (i+j))
                r.append(add)
            S.append(r)

        # Solving the linear system
        P = list(np.linalg.solve(S, b))
        ans = Polynomal(P)

        # Plotting given points
        mpl.plot(x, y, "rD", label='Given Points')
        ans.show(min(x), max(x), "x", "f(x)", "Polynomial")
        return ans

    def input(self, x):
        return np.exp(x)

    # method to compute and graph polynomial of degree n with best approx to the fun in [0,pi]

    def bestFunc(self, n):

        if n < 0:
            raise Exception("Can't accept non negative integer")

        x = 0
        y = np.pi
        s = "sin(x) + cos(x)"

        # Creating the vector b
        b = []
        for i in range(n + 1):
            l = sp.quad(lambda x: (np.power(x, i)) * self.input(x), x, y)
            b.append(l[0])

        # Creating the matrix S
        S = []
        for i in range(n + 1):
            r = []
            for j in range(0, n + 1):
                l = sp.quad(lambda x: np.power(x, (i + j)), x, y)
                r.append(l[0])
            S.append(r)

        # Solving the linear system
        P = list(np.linalg.solve(S, b))
        ans = Polynomal(P)

        # Plotting the actual function
        xp = np.linspace(x, y, 100)
        yp = [self.input(i) for i in xp]
        s = "Actual: " + s
        mpl.plot(xp, yp, "r", label=s)

        # Plotting the computed polynomial
        ans.show(x, y, "x", "P(x)", "Approx Polynomial")

        return ans

    # method to compute the Nth lagender polynomial
    def legendrePoly(self, n):

        if n < 0:
            raise Exception("Can't accept negative value")

        num = n ** Polynomal([-1, 0, 1])

        for i in range(n):
            num = num.derivative()

        den = 2 ** n
        for i in range(1, n + 1):
            den *= i

        return num * (1 / den)

    # method to compute the best fit legendre polynomial for the function e^x
    def bestLegendre(self, n):
        if n < 0:
            raise Exception("Expected  a non-negative integer")

        # The interval
        a = -1
        b = 1
        s = "e^x"

        lp = []
        for i in range(n + 1):
            lp.append(self.legendrePoly(i))

        # Coefficients of the polynomial
        c = []
        for j in range(n + 1):

            cj = sp.quad(lambda x: lp[j][x] * lp[j][x], a, b)
            kj = sp.quad(lambda x: lp[j][x] * self.input(x), a, b)
            aj = (1 / cj[0]) * kj[0]
            c.append(aj)

        # Q_n(x)
        ans = Polynomal([0])
        for i in range(n + 1):
            ans += (c[i] * lp[i])

        # Plotting the actual function
        x = np.linspace(a, b, 100)
        y = [self.input(i) for i in x]
        mpl.plot(x, y, "r", label=s)

        # Plotting the computed polynomial
        ans.show(a, b, "x", "P(x)", "Polynomial")
        return ans


# Test Case
p = Polynomal([])
p_n = p.bestLegendre(3)
