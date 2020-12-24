class Network:  
  
    def __init__(self, vertices):  
        self.V = vertices
        self.graph = []  
  
    def addLink(self, u, v, w):  
        self.graph.append([u, v, w])  
          
    def printTable(self, dist, src):
        print("Vector Table of {}".format(chr(ord('A')+src)))  
        for i in range(self.V):  
            print("{0}\t{1}".format(chr(ord('A')+i), dist[i]))
       
    def BellmanFord(self, src):  
    
        dist = [float("Inf")] * self.V  
        dist[src] = 0
  
  
        for _ in range(self.V - 1):  
            for u, v, w in self.graph:  
                if dist[u] != float("Inf") and dist[u] + w < dist[v]:  
                        dist[v] = dist[u] + w  
  
        for u, v, w in self.graph:  
                if dist[u] != float("Inf") and dist[u] + w < dist[v]:  
                        print("Graph contains negative weight cycle") 
                        return
                           
        self.printTable(dist, src)

def main():
    matrix=[]
    print("Enter No. of Nodes : ")
    n=int(input())
    print("Enter the Adjacency Matrix :")
    for i in range(n):
        m=list(map(int,input().split(" ")))
        matrix.append(m)
    g = Network(n)
    for i in range(n):
        for j in range(n):
            if matrix[i][j]==1:
                g.addLink(i,j,1)
    
    for _ in range(n):
        g.BellmanFord(_)
main()
