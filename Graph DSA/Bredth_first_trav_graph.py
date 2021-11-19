# BFS traversal of a graph

from collections import defaultdict

# This class represented a directed graph

class Graph:
    def __init__(self):
        # default dictionary to store graph
        self.graph = defaultdict(list)

    # function to add an edge to graph
    def addEdge(self, u, v):
        self.graph[u].append(v)

    # function to print a BFS pf graph
    def BFS(self, s):
        visited = [False] * (max(self.graph) + 1)
        
        # create a queue for BFS
        queue = []

        # mark the source node as visited and enqueue it
        queue.append(s)
        visited[s] = True

        while queue:
            # dequeue a vertex from queue and print it
            s = queue.pop(0)
            print(s, end = ' ')

            # get all adjacent vertices of the dequeued vertex s. If a adjacent has not been visited, then mark it visited and enqueue it
            for i in self.graph[s]:
                if visited[i] == False:
                    queue.append(i)
                    visited[i] = True