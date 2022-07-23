import heapq

class GraphNode:
    def __init__(self,val,neighbors=[]) -> None:
        self.val = val
        self.neighbors = neighbors

class Graph:
    def __init__(self, nodes=[]) -> None:
        self.nodes = nodes
        self.size = len(nodes)

def prims(graph: Graph):
    # seed node
    starting_node = graph.nodes[0]
    edges = []
    # add all edges originating from seed node
    for neigh,weight in starting_node.neighbors:
        # added starting_node.val just to please heapq
        # internal comparator
        edges.append((weight, starting_node.val, starting_node, neigh))
    # getchur heap
    heapq.heapify(edges)
    # short-circuiting mechanism. probably not a huge time
    # saver, but w/e. rationale => MST has exactly V - 1 edges
    target_edges = len(graph.nodes) - 1
    visited = set()
    visited.add(starting_node.val)
    res,total_weight = [],0
    while target_edges != 0:
        curr_weight,_,curr_node,curr_neigh = heapq.heappop(edges)
        if curr_neigh.val in visited:
            continue
        visited.add(curr_neigh.val)
        node_val,neigh_val = curr_node.val,curr_neigh.val
        # maintenance
        total_weight+=curr_weight
        target_edges-=1
        res.append((node_val,neigh_val,curr_weight))
        for neigh_neigh,neigh_weight in curr_neigh.neighbors:
            heapq.heappush(edges,(neigh_weight,curr_neigh.val,curr_neigh,neigh_neigh))
    return (res,total_weight)

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
    res = prims(g)