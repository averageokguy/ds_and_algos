from collections import deque

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
    def bfs(node: GraphNode):
        queue = deque()
        queue.append(node)
        visited.add(node.val)
        while queue:
            queue_len = len(queue)
            for _ in range(queue_len):
                node = queue.popleft()
                val = node.val
                print("visiting node with val", val)
                for neigh_tuple in node.neighbors:
                    neigh,neigh_val,neigh_weight = neigh_tuple[0],neigh_tuple[0].val,neigh_tuple[1]
                    if neigh_val in visited:
                        print("node with val", neigh_val, "already visited")
                        continue
                    print(val, " => ", neigh_val, ", weight", neigh_weight)
                    visited.add(neigh_val)
                    queue.append(neigh)

    for node in graph.nodes:
        node.val not in visited and bfs(node)


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
