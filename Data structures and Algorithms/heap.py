class Node:
    def __init__(self, data, neighbors = None):
        self.data = data
        if neighbors is None:
            self.neighbors = [ ]
        else:
            self.neighbors = neighbors
    def has_neighbors(self):
        if len(self.neighbors) != 0:
            return True
        else:
            return False
    def number_of_neighbors(self):
        return len(self.neighbors)
    def add_neighbors(self, neighbors):
        self.neighbors.append(neighbors)

class Graph:
    def __init__(self, nodes = None):
        if not nodes:
            self.nodes = []
        else:
            self.nodes = nodes
    def add_nodes(self, data, neighbors = None):
        self.nodes.append(Node(data, neighbors))
    def get_nodes(self, node):
        for nodes in self.nodes:
            if nodes.data == node:
                return nodes
            
        return None
        
    def add_edges(self, node1, node2, weight = 1, directed = False):
        node_a = self.get_nodes(node1)
        node_b = self.get_nodes(node2)
        
        if (node_a is not None) and (node_b is not None):
            if not directed:
                node_a.add_neighbors((node_b, weight))
                node_b.add_neighbors((node_a, weight))
            else:
                node_a.add_neighbors((node_b, weight))
        else:
            raise Exception("One or more nodes are missing")
    def are_connected(self, node1, node2):
        node_a = self.get_nodes(node1)
        node_b = self.get_nodes(node2)
        for neighbors in node_a.neighbors:
            if neighbors[0].data == node_b.data:
                return True
            
        return False
            
            
            
graph = Graph()
graph.add_nodes("John")
graph.add_nodes("Mary")
graph.add_edges("John", "Mary", directed = True)
graph.are_connected("John", "Mary")
#graph.prit()