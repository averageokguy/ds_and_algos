class GraphNode:
    def __init__(self,val,neighbors=[]) -> None:
        self.val = val
        self.neighbors = neighbors

class Graph:
    def __init__(self, nodes=[]) -> None:
        self.nodes = nodes
        self.size = len(nodes)

# use case - all-pairs shortest path
# high level - sort of dp. main idea to wrap your head around is
#              dist[u][v] is min(dist[u][v], dist[u][k] + dist[k][v]).
#              it'll make more sense once you look through the code

def floyd_warshall(graph: Graph):
    # little bitta python magic here, sorrey
    res = [[float("inf") for _ in range(len(graph.nodes))] for _ in range(len(graph.nodes))]
    node_idx_map = {}
    # populate node_idx_map
    for i in range(len(graph.nodes)):
        node = graph.nodes[i]
        node_val = node.val
        node_idx_map[node_val] = i
    # populate node_idx_map for future reference
    for i in range(len(graph.nodes)):
        node = graph.nodes[i]
        node_val = node.val
        node_idx = node_idx_map[node_val]
        # coding this assuming no self-loops. ez to change tho
        res[node_idx][node_idx] = 0
        for neigh,weight in node.neighbors:
            neigh_val = neigh.val
            neigh_idx = node_idx_map[neigh_val]
            res[node_idx][neigh_idx] = weight
            res[neigh_idx][neigh_idx] = 0
    all_nodes = graph.nodes
    ROWS = len(all_nodes)
    for k in range(ROWS):
        intrmd_node = all_nodes[k]
        intrmd_node_val = intrmd_node.val
        k_idx = node_idx_map[intrmd_node_val]
        for u in range(ROWS):
            for v in range(ROWS):
                res[u][v] = min(res[u][v], res[u][k_idx] + res[k_idx][v])
    for u in range(ROWS):
        for v in range(ROWS):
            for k in range(ROWS):
                intrmd_node = all_nodes[k]
                intrmd_node_val = intrmd_node.val
                k_idx = node_idx_map[intrmd_node_val]
                if res[u][k_idx] + res[k_idx][v] < res[u][v]:
                    res[u][v] = float("-inf")
    return res

if __name__ == "__main__":
    zero = GraphNode('a')
    one = GraphNode('b')
    two = GraphNode('c')
    three = GraphNode('d')
    four = GraphNode('e')
    five = GraphNode('f')
    six = GraphNode('g')
    zero.neighbors = [(two, 2), (four, 3)]
    one.neighbors = [(three, 1)]
    two.neighbors = [(six, 6)]
    three.neighbors = [(four, 4)]
    # line below induces negative weight cycle
    # three.neighbors = [(four, -5)]
    four.neighbors = [(one, 1), (six, 4)]
    six.neighbors = [(five, 2)]
    arr = [zero,one,two,three,four,five,six]
    g = Graph(arr)
    res = floyd_warshall(g)
    for r in res:
        print(r)