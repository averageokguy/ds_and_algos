class GraphNode:
    def __init__(self,val,neighbors=[]) -> None:
        self.val = val
        self.neighbors = neighbors

class Graph:
    def __init__(self, nodes=[]) -> None:
        self.nodes = nodes
        self.size = len(nodes)

def topsort(graph: Graph):
    # visited so we don't duplicate work
    # cycle so we can detect cycle
    visited,cycle = set(),set()
    res = []
    # big pic idea - visit all nodes. once you've visited
    # all neighbors of any given node (all neighbors have)
    # been processed, you know it's safe to add said node
    # to res[]
    def dfs(node: GraphNode):
        if node.val in cycle:
            cycle.remove(node.val)
            return False
        # general trend in backtracky sort of solutions
        # you add some value, do some operations based on
        # arr with new val, and then remove new val after
        # the fact
        cycle.add(node.val)
        visited.add(node.val)
        for neigh,_ in node.neighbors:
            # don't reprocess
            if neigh.val in visited:
                continue
            # cascade cycle detection as boolean and pass
            # back up the stack
            if not dfs(neigh):
                return False
        cycle.remove(node.val)
        res.append(node.val)
        return True
    for node in graph.nodes:
        if node.val not in visited:
            if not dfs(node):
                return "cycle detected"
    # nodes with no kiddos will be the first appended to
    # res[]. nodes analogous to the duggar family will be
    # the last nodes added. thus, it's worth it, let's work
    # it, put our things down, flip it and reverse it
    res.reverse()
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
    # if you draw this graph out, you'll see there's a cycle,
    # which is quite problematic
    print(topsort(g))
    # remove one of the problematic edges
    four.neighbors = [(six, 4)]
    print(topsort(g))
