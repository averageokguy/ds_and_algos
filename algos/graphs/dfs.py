class GraphNode:
    def __init__(self,val,neighbors=[]) -> None:
        self.val = val
        self.neighbors = neighbors

class Graph:
    def __init__(self, nodes=[]) -> None:
        self.nodes = nodes
        self.size = len(nodes)

def visit_all_nodes(graph: Graph):
    visited = set()
    def dfs(node: GraphNode):
        if node.val in visited:
            print("node with val", node.val, "already visited")
            return
        visited.add(node.val)
        print("visiting node with val", node.val)
        for (v,w) in node.neighbors:
            print(node.val," => ", v.val, ", weight", w)
            dfs(v)
    for node in graph.nodes:
        node.val not in visited and dfs(node)


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
    visit_all_nodes(g)
