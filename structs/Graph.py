class GraphNode:
    def __init__(self,val,neighbors=[]) -> None:
        self.val = val
        self.neighbors = neighbors

class Graph:
    def __init__(self, nodes=[]) -> None:
        self.nodes = nodes

    def invert_graph(self):
        visited_edge_set = set()
        node_map = {}
        def dfs(node: GraphNode):
            if node.val not in node_map:
                node_map[node.val] = GraphNode(node.val)
            new_end_node = node_map[node.val]
            for (neigh,weight) in node.neighbors:
                if (neigh.val,node.val) in visited_edge_set or (node.val,neigh.val) in visited_edge_set:
                    continue
                visited_edge_set.add((neigh.val,node.val))
                if neigh.val not in node_map:
                    node_map[neigh.val] = GraphNode(neigh.val)
                new_start_node = node_map[neigh.val]
                new_start_node.neighbors.append((new_end_node, weight))
                dfs(neigh)
        for node in self.nodes:
            node.val not in node_map and dfs(node)
        self.nodes = node_map.values()
    
if __name__ == "__main__":
    zero = GraphNode(0)
    one = GraphNode(1)
    two = GraphNode(2)
    three = GraphNode(3)
    four = GraphNode(4)
    five = GraphNode(5)
    six = GraphNode(6)
    zero.neighbors = [(two, 2), (four, 3)]
    one.neighbors = [(three, 1)]
    two.neighbors = [(six, 6)]
    three.neighbors = [(four, 4)]
    four.neighbors = [(one, 1), (six, 4)]
    six.neighbors = [(five, 2)]
    arr = [zero,one,two,three,four,five,six]
    g = Graph(arr)
    g.invert_graph()
    