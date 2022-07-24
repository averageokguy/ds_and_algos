class GraphNode:
    def __init__(self,val,neighbors=None) -> None:
        self.val = val
        self.neighbors = neighbors or []

class Graph:
    def __init__(self, nodes=None) -> None:
        self.nodes = nodes or []

    # thanks to @trincot from SO, i now have an elegant and
    # much simpler graph inversion solution
    def invert_graph(self):
        for node in self.nodes:
            # create partition on top of existing neighbors.
            # anything that comes before this partition will
            # eventually be deleted
            node.neighbors.append((None, 0))

        for node in self.nodes:
            for i, (neighbor, weight) in enumerate(node.neighbors):
                # once we reach the partition, we're free to
                # delete the stale/original edges
                if neighbor is None:
                    del node.neighbors[:i + 1]  # Remove original edges
                    break
                neighbor.neighbors.append((node, weight))
    
# use case - strongly connected components
# high level - look at it like you're doing a topological sort,
#              inverting the graph, then doing another top sort

def kosarajus(graph: Graph):
    # need val_node_map for our second traversal
    visited,stack,val_node_map = set(),[],{}
    def dfs(node: GraphNode):
        val_node_map[node.val] = node
        visited.add(node.val)
        for neigh,_ in node.neighbors:
            neigh.val not in visited and dfs(neigh)
        stack.append(node.val)
    for node in graph.nodes:
        node.val not in visited and dfs(node)
    # housekeeping
    visited.clear()
    # create copy of stack to pop from since defined dfs() uses
    # the stack array by default
    stack_copy = stack[:]
    graph.invert_graph()
    res = []
    while stack_copy:
        curr_node_val = stack_copy.pop()
        curr_node = val_node_map[curr_node_val]
        if curr_node_val not in visited:
            # in dfs(), we're already appending to stack. thus,
            # we can take advantage by clearing out the stack
            # before each traversal and append the resultant
            # stack to our final res[]
            stack = []
            dfs(curr_node)
            res.append(stack)
    return res

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
    res = kosarajus(g)
    print(res)
    