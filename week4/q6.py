import numpy as np
import matplotlib.pyplot as mpl

# code of Polynomal class from Assignment 3
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

        A, B, x, y = [],[],[],[]
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
        lp,x,y = [],[],[]

        min = np.inf
        max = -np.inf

        i = 0
        while i < num:
            t = lt[i]
            m,n = t[0],t[1]
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
                    val = Polynomal([a,b])
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

        ip = self.integral()
        return f"Area in the interval [{a}, {b}] is: {(ip[b] - ip[a]):.3f}"

# Sample Test 1
p = Polynomal([1, 2, 3])
pd = p.derivative()
print(pd)

# Sample Test 2
print(p.area(1,2))