import heapq

class GraphNode:
    def __init__(self,val,neighbors=[]) -> None:
        self.val = val
        self.neighbors = neighbors

class Graph:
    def __init__(self, nodes=[]) -> None:
        self.nodes = nodes
        self.size = len(nodes)

def reconstruct_paths(ancestor_arr, node_idx_map: dict):
    idx_node_map = {}
    for node_val,idx in node_idx_map.items():
        idx_node_map[idx] = node_val
    for node_val,idx in node_idx_map.items():
        if ancestor_arr[idx] is None:
            print("No direct path to", node_val)
            continue
        res = []
        curr_idx = idx
        curr_val = node_val
        while ancestor_arr[curr_idx] is not None:
            res.append(curr_val)
            curr_idx = ancestor_arr[curr_idx]
            curr_val = idx_node_map[curr_idx]
        res.append(curr_val)
        for i in range(len(res)-1,-1,-1):
            print(res[i],"=>",end=" ")
        print("\n")

def dijkstras(graph: Graph):
    min_dist,node_idx_map,ancestor_arr = [],{},[]
    for i in range(len(graph.nodes)):
        min_dist.append(float("inf"))
        node_idx_map[graph.nodes[i].val] = i
        ancestor_arr.append(None)
    start_node = graph.nodes[0]
    start_node_idx = node_idx_map[start_node.val]
    min_dist[start_node_idx] = 0
    heap = []
    for neigh,weight in start_node.neighbors:
        heap.append((weight, start_node_idx, neigh))
    heapq.heapify(heap)
    while heap:
        curr_wt,ancestor_idx,curr_end = heapq.heappop(heap)
        curr_end_idx = node_idx_map[curr_end.val]
        if min_dist[curr_end_idx] <= curr_wt:
            continue
        min_dist[curr_end_idx] = curr_wt
        ancestor_arr[curr_end_idx] = ancestor_idx
        for neighb,w in curr_end.neighbors:
            heapq.heappush(heap, (w+curr_wt,curr_end_idx,neighb))
    return (min_dist,ancestor_arr,node_idx_map)        

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
    four.neighbors = [(one, 1), (six, 4)]
    six.neighbors = [(five, 2)]
    arr = [zero,one,two,three,four,five,six]
    g = Graph(arr)
    (res,ancestor_arr,node_idx_map) = dijkstras(g)
    print(res)
    reconstruct_paths(ancestor_arr,node_idx_map)