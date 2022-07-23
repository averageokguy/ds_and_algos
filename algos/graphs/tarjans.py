class GraphNode:
    def __init__(self,val,neighbors=[]) -> None:
        self.val = val
        self.neighbors = neighbors

class Graph:
    def __init__(self, nodes=[]) -> None:
        self.nodes = nodes

def tarjans(graph: Graph):
    # dict to keep track of node's llv and stack status
    dict = {}
    stack = []
    res = []
    visited = set()
    # global index used to keep track order of when a
    # node was visited (for llv). mistake i kept making
    # while coding this was trying to use the node's val
    # as the llv, which clearly doesn't work. keep that
    # in mind
    encounter_num = [0]

    for node in graph.nodes:
        # key: [llv, on_stack]
        dict[node.val] = [-1,False]

    def dfs(node: GraphNode):
        # don't process if already visited
        if node.val in visited:
            return
        visited.add(node.val)
        stack.append(node.val)
        # establish initial llv as the order it was 
        # encountered at
        dict[node.val][0] = encounter_num[0]
        # keep a local reference as to when this node
        # was encountered
        tmp_encountered_num = encounter_num[0]
        encounter_num[0]+=1
        dict[node.val][1] = True
        for neigh,_ in node.neighbors:
            dfs(neigh)
            if dict[neigh.val][1]:
                dict[node.val][0] = min(dict[neigh.val][0],dict[node.val][0])
        # start accumulating the actual scc if the node's
        # llv is the same as when it was encountered
        if tmp_encountered_num == dict[node.val][0]:
            scc = []
            while stack:
                node_val = stack.pop()
                scc.append(node_val)
                # no longer on stack
                dict[node_val][1] = False
                # if nothing left to process or if the
                # popped node has a different llv than
                # what's currently on top of the stack,
                # implying it's part of a different scc,
                # wrap it up
                if (not stack or stack and dict[stack[len(stack)-1]][0] != dict[node_val][0]):
                    res.append(scc)
                    break

    for node in graph.nodes:
        node.val not in visited and dfs(node)
    return res      

if __name__ == "__main__":
    # zero = GraphNode(0)
    # one = GraphNode(1)
    # two = GraphNode(2)
    # zero.neighbors = [(one, 2)]
    # one.neighbors = [(two, 1)]
    # two.neighbors = [(zero, 6)]
    # arr = [zero,one,two]
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
    sccs = tarjans(g)
    print(sccs)