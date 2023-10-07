import sys
import matplotlib.pyplot as mpl
import random
import math


class UndirectedGraph:
    def __init__(self, ver=None):
        self.adj = {}

        if ver is None:
            self.mxn = sys.maxsize
            self.nn = 0
            self.fg = True

        else:
            self.mxn = ver
            self.nn = ver
            self.fg = False

            for i in range(ver):
                self.adj[i+1] = []

        self.ne = 0

    def addNode(self, add):

        if not isinstance(add, int) or add > self.mxn or add < 0:
            raise Exception("Node index cannot exceed number of nodes")

        else:
            if add not in self.adj.keys():
                self.adj[add] = []
                self.nn += 1
            return

    def addEdge(self, x, y):

        if not self.fg:
            if x in self.adj.keys() or y in self.adj.keys():
                self.adj[x].append(y)
                self.adj[y].append(x)
                self.ne += 1

            else:
                raise Exception("Node index cannot exceed number of nodes")

        else:
            self.addNode(x)
            self.addNode(y)

            self.ne += 1
            if x in self.adj.keys():
                self.adj[x].append(y)
            else:
                self.adj[x] = [y]

            if y in self.adj.keys():
                self.adj[y].append(x)
            else:
                self.adj[y] = [x]

    def __str__(self):
        text = f"Graph with {self.nn} nodes and {self.ne} edges. n of the nodes are belows:\n"
        for i in self.adj:
            text += f"Node {i}: " + str(self.adj[i]) + '\n'
        return text

    def __add__(self, val):

        if isinstance(val, tuple):
            self.addNode(val[0])
            self.addNode(val[1])
            self.addEdge(val[0], val[1])

        elif isinstance(val, int):
            self.addNode(val)

        return self

    def graph(self, x, f, v):
        mpl.scatter(x, f, s=12, color='b', label="Actual degree distribution")
        mpl.axvline(v, color='r', label="Avg node degree")
        mpl.grid()
        mpl.xlabel("Node degree")
        mpl.ylabel("Fraction of nodes")
        mpl.title("Node Degree Distribution")
        mpl.legend()
        mpl.show()

    def plotDegDist(self):

        x = []
        fracn = []

        for i in range(self.nn):
            x.append(i)
            fracn.append(0)

        for i in self.adj:
            fracn[len(self.adj[i])] += 1
        total = sum(fracn)

        for i in range(len(fracn)):
            fracn[i] = fracn[i]/total

        k = 1
        avg = 0
        for i in fracn:
            avg += i * k
            k += 1

        avg -= 1
        print(avg)

        self.graph(x, fracn, avg)

    def breadthfirstsearch(self, s):
        # n = self.nn
        queue = [s]
        v = []
        while queue:
            c = queue.pop(0)

            if c not in v:
                v.append(c)
                for i in self.adj[c]:
                    queue.append(i)

        return v

    def isConnected(self):
        t1 = self.breadthfirstsearch(random.choice(list(self.adj.keys())))

        t2 = []
        for i in self.adj:
            t2.append(i)

        t1.sort()
        t2.sort()

        if t1 != t2:
            return False
        else:
            return True
        
    def OneTwoComponentSizes(self):
        c,p,s = [],[],[]

        for i in self.adj:
            if i  in p:
                continue
            else:
                t = self.breadthfirstsearch(i)
                for n in t:
                    p.append(n)
                c.append(tuple(t))
                
        for i in c:
          s.append(len(i))
        s.sort()
        l = len(s)

        if l == 1:
          return [s[l-1] , 0]    
        else:
          return [s[l-1] , s[l-2]]

class ERRandomGraph(UndirectedGraph):

    def sample(self, p):

        p1 = p * 100
        p2 = (1 - p) * 100
        for y in self.adj:
            for x in self.adj:
                if x > y:
                    t = random.choices([True, False], weights=[p1, p2])
                    if t[0]:
                        self.addEdge(x, y)


def verification(trial):

    x = []
    l1, l2 = [],[]
    for i in range(101):
        x.append(float(i)/float(10000))

    for i in x:
        pos = 0
        neg = 0

        for _ in range(trial):
            g = ERRandomGraph(1000)
            g.sample(i)
            t = g.OneTwoComponentSizes()
            pos += t[0]
            neg += t[1]

        print(f"{int(i*10000)}/100")
        v = g.nn * trial
        l1.append(pos/v)
        l2.append(neg/v)

    graph(x, l1, l2, g.nn)

def graph(x, l1, l2, n):

    mpl.plot(x , l1 , color = 'g' , label ="Largest connected component" )
    mpl.plot(x , l2 , color = 'b' , label = "2nd Largest connected component")
    mpl.axvline(1/n , label = "Largest CC size threshold" , color = 'r')
    mpl.axvline(math.log(n)/n , label = "Connectedness threshold" , color = 'y')
    mpl.title(f"Fraction of nodes in\nlargest and 2nd-largest (CC)\nof G({n}, p) as function of p")
    mpl.ylabel(f"Fraction of runs G({n},p) is connected")
    mpl.xlabel("p")
    mpl.legend()
    mpl.show()

verification(10)
