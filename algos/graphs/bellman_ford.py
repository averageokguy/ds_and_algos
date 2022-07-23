class GraphNode:
    def __init__(self,val: str,neighbors=[]) -> None:
        self.val = val
        self.neighbors = neighbors

class Graph:
    def __init__(self, nodes=[]) -> None:
        self.nodes = nodes

# use case - single-source shortest path (SSSP)
# high level - iterate through all edges |V|-1 times,
#              reducing along the way as necessary. run
#              the exact same process again, except this
#              time around, if you're able to make a change,
#              it's because there's a negative weight
#              cycle - set value in dist to -inf to indicate
#              as such. less efficient than dijkstra in
#              terms of complexity, but can handle negative
#              edge weights and detect cycles

def bellman_ford(graph: Graph, start_node: GraphNode):
    # node_idx_map used to map node values to indices in
    # min_dist[]
    min_dist,node_idx_map = [],{}
    vert_count = len(graph.nodes)
    # i like edge lists, sorrey. can probably find a better
    # alternative if this doesn't float ur boat
    edges = []
    for i in range(len(graph.nodes)):
        node = graph.nodes[i]
        node_val = node.val
        min_dist.append(float("inf"))
        node_idx_map[node_val] = i
        for neigh,weight in node.neighbors:
            edges.append((node_val,neigh.val,weight))
    start_node_idx = node_idx_map[start_node.val]
    min_dist[start_node_idx] = 0
    for i in range(vert_count - 1):
        # used to detect whether this current iteration has
        # any changes. if not, we can terminate - won't
        # magically change the next time around
        has_changes = False
        for u,v,w in edges:
            u_idx,v_idx = node_idx_map[u],node_idx_map[v]
            u_wt = min_dist[u_idx]
            prev_dist = min_dist[v_idx]
            # updating min_dist at v_idx if we find better
            # val
            min_dist[v_idx] = min(prev_dist,u_wt + w)
            has_changes = has_changes or prev_dist != min_dist[v_idx]
        if not has_changes:
            break
    for i in range(vert_count - 1):
        has_changes = False
        for u,v,w in edges:
            u_idx,v_idx = node_idx_map[u],node_idx_map[v]
            u_wt = min_dist[u_idx]
            # if we can still reduce, must be part of
            # negative cycle
            if u_wt + w < min_dist[v_idx]:
                has_changes = True
                min_dist[v_idx] = float("-inf")
        if not has_changes:
            break
    return min_dist

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
    three.neighbors = [(four, -5)]
    four.neighbors = [(one, 1), (six, 4)]
    # four.neighbors = [(six, 4)]
    six.neighbors = [(five, 2)]
    arr = [zero,one,two,three,four,five,six]
    start_node = zero
    g = Graph(arr)
    res = bellman_ford(g,start_node)
    print(res)