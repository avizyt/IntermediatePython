# DFS graph graph traversal complete

from typing import Collection


from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)
    
    def DFSUtil(self, v, visited)