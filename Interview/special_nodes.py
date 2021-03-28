from collections import deque
 
 
class Graph:
    
 
    # Intialisation of graph
    def __init__(self, vertices):
 
        # No. of vertices
        self.vertices = vertices
 
        # adjacency list
        self.adj = {i: [] for i in range(self.vertices)}
 
    def addEdge(self, u, v):
        # add u to v's list
        self.adj[u].append(v)
        # since the graph is undirected
        self.adj[v].append(u)
 
    # method return farthest node and its distance from node u
    def BFS(self, v):
        dic={}
        for u in v:
            visited = [False for i in range(self.vertices + 1)]
            # mark all distance with -1
            distance = [-1 for i in range(self.vertices + 1)]
     
            # distance of u from u will be 0
            distance[u] = 0
            print(u)
            # in-built library for queue which performs fast oprations on both the ends
            queue = deque()
            queue.append(u)
            # mark node u as visited
            visited[u] = True
     
            while queue:
     
                # pop the front of the queue(0th element)
                front = queue.popleft()
                # loop for all adjacent nodes of node front
     
                for i in self.adj[front]:
                    if not visited[i]:
                        # mark the ith node as visited
                        visited[i] = True
                        # make distance of i , one more than distance of front
                        distance[i] = distance[front]+1
                        # Push node into the stack only if it is not visited already
                        queue.append(i)
     
            
     
            # get farthest node distance and its index
            for i in range(self.vertices):
                dic[i] = distance[i]
                    
     
        return max(dic.values())
 
    # method prints longest path of given tree
    def LongestPathLength(self):
 
        # first DFS to find one end point of longest path
        
        # second DFS to find the actual longest path
        print(self.BFS(self.adj))
 
        
 
 
# create a graph given in the example
 
G = Graph(10)
G.addEdge(0, 1)
G.addEdge(1, 2)
G.addEdge(2, 3)
G.addEdge(2, 9)
G.addEdge(2, 4)
G.addEdge(4, 5)
G.addEdge(1, 6)
G.addEdge(6, 7)
G.addEdge(6, 8)
 
G.LongestPathLength()

