mark = {}
q = []
dp = {}


class Graph():
    def __init__(self):
        self.adjList = {}
        self.comp = 0

    def __addSingleVertex(self , node):
        if node not in self.adjList.keys():
            self.adjList[node] = []

    def addVertices(self , nodes):
        if type(nodes) == list:
            for node in nodes:
                self.__addSingleVertex(node)
        elif type(nodes) == int:
            self.__addSingleVertex(nodes) 

    def addEdge(self , node1 , node2):
        if node1 in self.adjList.keys() and node2 in self.adjList.keys():
            if node1 in self.adjList[node2] or node2 in self.adjList[node1]:
                return
            else:
                self.adjList[node1].append(node2)
                self.adjList[node2].append(node1)   

    def remNode(self , node):
        for adj in self.adjList[node]:
            self.adjList[adj].remove(node) 

        self.adjList.pop(node) 

    def remEdge(self , node1 , node2):
        self.adjList[node1].remove(node2)
        self.adjList[node2].remove(node1)
        mark[node1] = False
        mark[node2] = False

    def BFS(self , v):
        mark[v] = True
        q.append(v)
        while(len(q) != 0):
            u = q[0]
            for i in self.adjList[u]:
                if mark[i] == False:
                    mark[i] = True
                    q.append(i)
                    dp[i] = dp[u] + 1
            q.remove(q[0])        
            
    def BFS_ALL(self):
        self.comp = 0
        for i in range(9): # if you don't want to do like this you should get input(vertexs' number is between 0 - 8)
            mark[i] = False
            dp[i] = 0
        for i in self.adjList:
            if mark[i] == False: 
                print("raas : " , i)
                self.comp += 1 
                self.BFS(i)
                          

    def isConnected(self):
        self.BFS_ALL()
        if self.comp == 1:
            print("It is connected")
        else:
            print("It isn't connected")    

    def shortestPath(self , node1 , node2):
        ans = abs(dp[node1] - dp[node2])
        print(f"the shortest path between {node1} and {node2} is {ans}")


g = Graph()
g.addVertices([0 , 1 , 2 , 3 , 4 , 5 , 6 , 7 , 8])

g.addEdge(0 , 1)
g.addEdge(0 , 2)
g.addEdge(0 , 3)
g.addEdge(0 , 4)
g.addEdge(0 , 2)
g.addEdge(1 , 5)
g.addEdge(1 , 6)
g.addEdge(6 , 7)
g.addEdge(6 , 8)
g.addEdge(4 , 8)
print("example 1")
print(g.adjList)
g.isConnected()
g.shortestPath(0 , 7)

# g.remNode()
# print(g.adjList)

g.remEdge(1 , 5)
g.remEdge(6 , 7)
print("example 2")
g.isConnected()
print("comp : " , g.comp)
print(g.adjList)

g.addEdge(2 , 6)
g.addEdge(6 , 4)
print("example 3")
g.isConnected()
print("comp : " , g.comp)
g.shortestPath(6 , 4)