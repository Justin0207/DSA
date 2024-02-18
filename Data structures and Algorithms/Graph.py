# -*- coding: utf-8 -*-
"""
Created on Tue Jan  2 20:39:27 2024

@author: HP
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.neighbors = set( )
    #def __str__(self):
     #   return self.data
    def __repr__(self):
        return self.data
    def add_neighbors(self, neighbors):
        self.neighbors.add(neighbors)
    def has_neighbors(self):
        if self.neighbors:
            return True
        else:
            return False
class Graph:
    def __init__(self):
        self.nodes = set()
        self._edges = { }
    def __str__(self):
        return self.data
    def __repr__(self):
        return self.data
    def add_edges(self, first, second):
        if first not in self._edges:
            self._edges[first] = set( )
        if first.has_neighbors == True:
            self._edges.union(first.neighbors)
        self._edges[first].add(second)
    def print_edges(self):
        return self._edges
    def dfs(self, start, visited = None):
        graph = self._edges
        if visited is None:
            visited = set( )
        visited.add(start)
        print(start)
        if start not in graph:
            return visited
        for next_node in graph[start] - visited:
            if next_node not in visited:
                self.dfs(next_node, visited)
    def bfs(self, start, visit= None):
        graph = self._edges
        queue = [ ]
        if visit is None:
            visit = [ ]
        queue.append(start)
        visit.append(start)
        
        while queue:
            actual_node = queue.pop(0)
            print(actual_node, end = ' ')
            if actual_node in graph:
                #return visit
                for node in graph[actual_node]:
                
                    if node not in visit:
                        visit.append(node)
                        queue.append(node)
            
                           
        
        
    
    
    
    
    
a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
e = Node('e')
#y.add_neighbors('7')
graph = Graph()
#graph.add_edges(m, x)
graph.add_edges(a, b)
graph.add_edges(a, c)
graph.add_edges(b, d)
graph.add_edges(d, e)
graph.add_edges(b, e)
graph.add_edges(c, a)
#graph.add_edges(z, m)
gra = graph.print_edges()
print(gra)
graph.bfs(a)

print(graph.dfs(a))