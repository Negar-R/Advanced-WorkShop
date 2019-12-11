import math

mark = {}
dist = {}
par = {}
st = {}

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

    def addEdge(self , node1 , node2 , w):
        if node1 in self.adjList.keys() and node2 in self.adjList.keys():
            if node1 in self.adjList[node2] or node2 in self.adjList[node1]:
                return
            else:
                self.adjList[node1].append((node2 , w))
                self.adjList[node2].append((node1 , w))   

    def remNode(self , node):
        for adj in self.adjList[node]:
            self.adjList[adj].remove(node)

        self.adjList.pop(node) 

    def remEdge(self , node1 , node2):
        self.adjList[node1].remove(node2)
        self.adjList[node2].remove(node1)

    def dijekstra(self):
        while(len(st) != 0):
            for i in st.keys():
                u = i
                break
            del st[u]

            mark[u] = True
            for i in range(len(self.adjList[u])):
                # for pair in self.adjList[adj]:
                v = self.adjList[u][i][0]
                w = self.adjList[u][i][1]
                # if mark[v] == True:
                #     continue
                if dist[u] + w < dist[v]:
                    par[v] = u
                    dist[v] = dist[u] + w
                    st[v] = dist[v]           

    # def isConnected(self):
    #     self.dijekstra()
    #     for vertex in self.adjList:
    #         if mark[vertex] == False:
    #             print("It isn't connected")
    #             break
    #         else:
    #             print("It is connected")    

    def shortestPath(self , s , t):
        self.dijekstra()
        if dist[t] != math.inf:            
            print(f"the shortes path between {s} and {t} is {dist[t]}") 
        else:
            print(f"{t} is unrechable")   


g = Graph()
g.addVertices([0 , 1 , 2 , 3 , 4 , 5])
# print("Enter the number of vertex (0-base) : ")
# n = int(input())
# print("Enter the number of edge : ")
# m = int(input())
# print("Enter the number of node1 then node2 and at last the weight of their edge : ")
# for i in range(m):
#     u  , v , w = map(int , input().split())
#     # v = int(input())
#     # w = int(input())
#     g.adjList[u].append(v)
# print("Enter the number of your source vertex and the destination vertex : ") 
# s , t = map(int , input().split())
s = 4
t = 5 
g.addEdge(0 , 1 , 10)
g.addEdge(0 , 2 , 5)
g.addEdge(0 , 3 , 1)
g.addEdge(3 , 4 , 1)
g.addEdge(5 , 2 , 3)
g.addEdge(1 , 5 , 2)
g.addEdge(1 , 4 , 10)
for i in range(6):
    dist[i] = math.inf
dist[s] = 0
par[s] = -1
st[s] = dist[s]
g.shortestPath(5 , 0)
print(g.adjList)
# print(g.adjList[1][1][0])
# for i in range(len(g.adjList[3])):
#     print(g.adjList[3][i][0])


