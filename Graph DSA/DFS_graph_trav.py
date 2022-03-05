"""
What is DFS trav in graph?
DFS stands for Depth First search. The algorithm starts at the root node and explores as far as possible along arbitrary node and mark the node and move to the adjacent unmarked node and continues this loop until there is no unmarked adjacent node.

1. create as recursive function that takes the index of the node and a visited array.
2. Mark the current node as visited and print the node.
3. traverse all the adjacent and unmarked nodes and call the recursive function with the index of the adjacent node.

"""
from collections import defaultdict


class Graph:
    def __init__(self) -> None:
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def DFSUtil(self, v, visited):

        visited.add(v)
        print(v, end=" ")

        for neighbour in self.graph[v]:
            if neighbour not in visited:
                self.DFSUtil(neighbour, visited)
    

    def DFS(self, v):
        visited = set()

        self.DFSUtil(v, visited)

g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)

print("Following is DFS from (starting from vertex 2)")
g.DFS(2)
  