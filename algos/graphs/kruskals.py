import heapq

class GraphNode:
    def __init__(self,val: str,neighbors=[]) -> None:
        self.val = val
        self.neighbors = neighbors

class Graph:
    def __init__(self, nodes=[]) -> None:
        self.nodes = nodes

# use case - minimum spanning tree
# high level - union find algo. don't forget to compress
#              during the find operation in order to retain
#              true/expected runtime

def kruskals(graph: Graph):
    # node_idx_dict - necessary mapping for access to
    # par_arr and size_arr
    edges,node_idx_dict,par_arr,size_arr = [],{},[],[]
    i=0
    for node in graph.nodes:
        node_idx_dict[node.val] = i
        par_arr.append(i)
        size_arr.append(1)
        for neigh,weight in node.neighbors:
            edges.append((weight,node.val,neigh.val))
        i+=1
    heapq.heapify(edges)
    res = []
    total_weight = 0

    # find root
    def find(u):
        curr_idx = u
        root = par_arr[u]
        while curr_idx != root:
            curr_idx = par_arr[curr_idx]
            root = par_arr[root]
        # compression
        while u != root:
            tmp = par_arr[u]
            par_arr[u] = root
            u = tmp
        return root
    # merge two currently independent components
    # optimization - smaller comp should always
    # be merged into larger comp
    def union(u, v):
        if size_arr[u] > size_arr[v]:
            size_arr[u]+=size_arr[v]
            size_arr[v] = 0
            par_arr[v] = u
        else:
            size_arr[v]+=size_arr[u]
            size_arr[u] = 0
            par_arr[u] = v

    while edges:
        wt,u,v = heapq.heappop(edges)
        u_idx,v_idx = node_idx_dict[u],node_idx_dict[v]
        u_par = find(u_idx)
        v_par = find(v_idx)
        # check if they already belong to same component
        if u_par == v_par:
            continue
        # housekeeping
        total_weight+=wt
        res.append((u,v,wt))
        union(u_par,v_par)

    return (res, total_weight)

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
    res = kruskals(g)
    print(res)