import sys
import matplotlib.pyplot as mpl

class UndirectedGraph:
    def __init__(self , ver = None):
        self.adj = {}
        self.ne = 0

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
     
    def addNode(self , add ):
        if not isinstance(add, int) or add > self.mxn or add < 0:
            raise Exception("Node index cannot exceed number of nodes")            

        else:
            if add not in self.adj.keys():
                self.adj[add] = []
                self.nn += 1
            return
       
    def addEdge(self , x , y):
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
        s = f"Graph with {self.nn} nodes and {self.ne} edges. Neighbours of the nodes are belows:\n"
        for i in self.adj:
            s += f"Node {i}: " + str(self.adj[i]) + '\n'
        return s
    
    def __add__(self , val):
        if isinstance(val , tuple):
            self.addNode(val[0])
            self.addNode(val[1])
            self.addEdge(val[0] , val[1]) 
        
        elif isinstance(val , int):
            self.addNode(val)          
        
        return self            

    def graph(self, x, f, v):
        mpl.scatter(x, f, s = 12, color = 'b', label = "Actual degree distribution")
        mpl.axvline(v , color = 'r' , label = "Avg node degree")
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
            k+=1

        avg -= 1
        print(avg)
        
        self.graph(x, fracn, avg)

g = UndirectedGraph()
print(g)

g = UndirectedGraph(10)
print(g)

g = UndirectedGraph()
g.addNode(1)
g.addNode(100)
print(g)

g = UndirectedGraph(10)
g.addNode(4)
print(g)


g = UndirectedGraph()
g.addEdge(10,25)
print(g)

g = UndirectedGraph(10)
g.addEdge(1,2)
print(g)

g = UndirectedGraph()
g = g + 10
print(g)

g = UndirectedGraph()
g = g + (12,15)
print(g)

g = UndirectedGraph(10)
g = g + (1,2)
g = g + (3,4)
print(g)

g = UndirectedGraph(5)
print(g)

g = UndirectedGraph()
g = g + 10
g = g + (11, 12)
print(g)    

g = UndirectedGraph(5)
g = g + (1, 2)
g = g + (3, 4)
g = g + (1, 4)
print(g)
g.plotDegDist()

g = UndirectedGraph(10)
g.addNode(11)
print(g)