import matplotlib.pyplot as mpl
import networkx as nx
import random

class Lattice:
    def __init__(self, n):
        self.maze = nx.empty_graph(n**2)
        self.len = n
        self.p = False
        self.e = []
        self.t = []
        self.b = []
        self.r = {}

        for i in range(n ** 2):
            self.r[i] = (i//n, i % n)

        for i in range(n):
            self.t.append(n * (i+1) - 1)
            self.b.append(n * i)

    def graph(self):
        c = nx.get_edge_attributes(self.maze, 'color').values()
        w = nx.get_edge_attributes(self.maze, 'width').values()

        if not self.p:
            nx.draw(self.maze, self.r, node_size=1, node_color='b')

        else:
            nx.draw(self.maze, self.r, node_size=0, node_color='b',
                    edge_color=c, width=list(w))
        mpl.axis('off')
        mpl.show()

    def add(self, x, y):
        self.e.append((y, x))
        self.e.append((x, y))
        self.maze.add_edge(x, y, color='r', width=1)

    def possible(self):
        r = []
        l = self.len
        l1 = l * l
        l2 = l * (l-1)

        for n in range(l1):
            if (n+1) % l != 0:
                r.append((n, n+1))

        for n in range(l2):
            r.append((n, n+l))

        return r

    def percolate(self, p):
        if p != 0:
            self.p = True

        r = self.possible()
        w1 = p * 100
        w2 = (1 - p) * 100

        for i in r:
            t = random.choices([True, False], weights=[w1, w2])

            if not t[0]:
                continue

            else:
                self.add(i[0], i[1])

    def exist(self):
        for t in self.t:

            for b in self.b:

                if not nx.has_path(self.maze, t, b):
                    continue

                else:
                    return True
                
        return False

    def flag(self, c1, l1, c2):

        if c1 not in l1 and c2 in self.e:
            return True
        else:
            return False    

    def breadthfirstsearch(self, s):
        n = self.len
        queue = [s]
        v = []
        while queue:
            c = queue.pop(0)

            if c not in v:
                v.append(c)

                if self.flag(c+1, v, (c, c+1)):
                    queue.append(c+1)

                if self.flag(c-1, v, (c, c-1)):
                    queue.append(c-1)

                if self.flag(c+n, v, (c, c+n)) and (c+n < n*n):
                    queue.append(c+n)

                if self.flag(c-n, v, (c, c-n)) and (c-n > -1):
                    queue.append(c-n)

        return v

    def showPaths(self):
        s = {}
        bt = self.b

        for t in self.t:
            print(f"{t//100 + 1}/{len(self.t)}")

            for b in bt:

                if not nx.has_path(self.maze, t, b):
                    bt.remove(b)

                else:
                    l = nx.shortest_path(self.maze, t, b)
                    if t not in s.keys():
                        s[t] = l

                    else:
                        if len(s[t]) > len(l):
                            s[t] = l

        for i in self.t:
            if i not in s.keys():
                t = self.breadthfirstsearch(i)
                l = nx.shortest_path(self.maze, i, t[-1])
                s[i] = l

        for i in s:

            for j in range(len(s[i])-1):
                self.maze.add_edge(s[i][j], s[i][j+1], color='#458B00', width=2)

        self.graph()

def graph(x,y):
    mpl.plot(x, y, color='b')
    mpl.title("Critical cut-off in 2-D bond percolation")
    mpl.ylabel("Fraction of runs end-to-end perccolation occured")
    mpl.xlabel("p")
    mpl.show()

def verification(trial):
    x,y = [],[]
    
    for i in range(trial+1):
        x.append(float(i)/float(trial))

    x = x[1:]

    for i in x:
        pos = 0
        neg = 0
        for _ in range(trial):
            m = Lattice(100)
            m.percolate(i)

            if not m.exist():
                neg += 1

            else:
                pos += 1

        print(f"{int(i*trial)}/{trial}")
        val = pos/(pos+neg)
        y.append(val)
    
    graph(x,y)

maze = Lattice(100)
maze.percolate(0.7)
maze.showPaths()
