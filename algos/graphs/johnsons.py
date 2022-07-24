import heapq

class GraphNode:
    def __init__(self,val,neighbors=None) -> None:
        self.val = val
        self.neighbors = neighbors or []

class Graph:
    def __init__(self, nodes=None) -> None:
        self.nodes = nodes or []

# video reference - if you want to see someone a lot smarter than i explain and
#                   draw out the exact process i describe below, watch this:
#                   https://www.youtube.com/watch?v=qDDat59ylv4
# fair warning - this was a lot to take in for me. this is my first ever
#                attempt, so there's definitely room for improvement. however,
#                it's operationally sound and is bound by the proper time
#                complexity (pretty sure it is anyway)
# use case - alternative to floyd-warshall APSP solution. this will not work
#            at all if there are negative weight cycles. if that's the case,
#            roll with floyd-warshall.
# high level - create augmented graph which has dummy node with an edge to
#              each vertex with weight 0. run bellman-ford on the augmented
#              graph. the array returned is critical in creation of helper
#              graph. the helper graph is a clone of the og graph, but the
#              edge weights are transformed with the help of the array returned
#              by bellman-ford earlier => this step ensures no negatively
#              weighted edges. then, run dijkstra's algo from each node and
#              untransform the weight before appending to res[]

# utility function
def _get_edge_map(graph: Graph):
    res = {}
    for node in graph.nodes:
        for neigh,weight in node.neighbors:
            res[(node.val,neigh.val)] = weight
    return res

def _get_helper_graph(graph: Graph, augmented_sssp_map):
    edge_map,new_node_map = _get_edge_map(graph),{}
    helper_graph = Graph()
    # clone graph
    for node in graph.nodes:
        if node.val not in new_node_map:
            new_node_map[node.val] = GraphNode(node.val)
        new_node = new_node_map[node.val]
        for neigh,_ in node.neighbors:
            if neigh.val not in new_node_map:
                new_node_map[neigh.val] = GraphNode(neigh.val)
            new_neigh = new_node_map[neigh.val]
            # p + og edge weight - q => transformation
            augmented_weight = augmented_sssp_map[node.val] + edge_map[(node.val,neigh.val)] - augmented_sssp_map[neigh.val]
            new_node.neighbors.append((new_neigh,augmented_weight))
    helper_graph.nodes = list(new_node_map.values())
    return helper_graph

def _get_augmented_graph(graph: Graph):
    new_node_map = {}
    # clone graph - sorrey, i know dfs for graph cloning is
    # over engineering in a sense, but it's already done 🤷‍♂️
    def dfs(node: GraphNode):
        if node.val in new_node_map:
            return new_node_map[node.val]
        new_node = GraphNode(node.val)
        new_node_map[node.val] = new_node
        for neigh,weight in node.neighbors:
            new_node.neighbors.append((dfs(neigh),weight))
        return new_node
    for node in graph.nodes:
        node.val not in new_node_map and dfs(node)
    new_nodes = list(new_node_map.values())
    augmented_graph = Graph(new_nodes)
    dummy_node = GraphNode("dummy")
    new_node_map["dummy"] = dummy_node
    # add edge with zero weight to all nodes
    for node in augmented_graph.nodes:
        dummy_node.neighbors.append((node,0))
    augmented_graph.nodes.append(dummy_node)
    return (augmented_graph,dummy_node)

def bellman_ford(graph: Graph, start_node: GraphNode):
    min_dist,node_idx_map = [],{}
    vert_count = len(graph.nodes)
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
        for u,v,w in edges:
            u_idx,v_idx = node_idx_map[u],node_idx_map[v]
            u_wt = min_dist[u_idx]
            prev_dist = min_dist[v_idx]
            min_dist[v_idx] = min(prev_dist,u_wt + w)
    for i in range(vert_count - 1):
        for u,v,w in edges:
            u_idx,v_idx = node_idx_map[u],node_idx_map[v]
            u_wt = min_dist[u_idx]
            if u_wt + w < min_dist[v_idx]:
                min_dist[v_idx] = float("-inf")
    sssp_map = {}
    for node_val,idx in node_idx_map.items():
        sssp_map[node_val] = min_dist[idx]
    return sssp_map

def dijkstras(graph: Graph, start_node: GraphNode):
    min_dist,node_idx_map = [],{}
    for i in range(len(graph.nodes)):
        min_dist.append(float("inf"))
        node_idx_map[graph.nodes[i].val] = i
    start_node_idx = node_idx_map[start_node.val]
    min_dist[start_node_idx] = 0
    heap = []
    for neigh,weight in start_node.neighbors:
        heap.append((weight, start_node_idx, neigh))
    heapq.heapify(heap)
    while heap:
        curr_wt,_,curr_end = heapq.heappop(heap)
        curr_end_idx = node_idx_map[curr_end.val]
        if min_dist[curr_end_idx] <= curr_wt:
            continue
        min_dist[curr_end_idx] = curr_wt
        for neighb,w in curr_end.neighbors:
            heapq.heappush(heap, (w+curr_wt,curr_end_idx,neighb))
    return (min_dist,node_idx_map)

def johnsons(graph: Graph):
    augmented_graph,start_node = _get_augmented_graph(graph)
    augmented_sssp_map = bellman_ford(augmented_graph,start_node)
    if float("-inf") in list(augmented_sssp_map.values()):
        raise Exception()
    helper_graph = _get_helper_graph(graph,augmented_sssp_map)
    res = []
    # run dijkstra's sssp algo from each node
    for node in helper_graph.nodes:
        curr_res = {node.val: []}
        min_dist,node_idx_map = dijkstras(helper_graph,node)
        for neigh_val,idx in node_idx_map.items():
            augmented_neigh_val,augmented_start_val = augmented_sssp_map[neigh_val],augmented_sssp_map[node.val]
            # q + helper edge weight - p => untransformation
            neigh_val != node.val and curr_res[node.val].append((neigh_val,augmented_neigh_val + min_dist[idx] - augmented_start_val))
        res.append(curr_res)
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
    one.neighbors = [(three, -1)]
    two.neighbors = [(six, 6)]
    three.neighbors = [(four, 2)]
    four.neighbors = [(one, 5), (six, 4)]
    six.neighbors = [(five, 2)]
    arr = [zero,one,two,three,four,five,six]
    g = Graph(arr)
    res,ancestor_arr,node_idx_map = None,None,None
    try:
        res = johnsons(g)
    except Exception:
        print("negative weight cycle detected. cannot proceed")
    finally:
        for r in res:
            print(r)