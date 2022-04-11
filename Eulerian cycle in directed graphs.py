# A class to represent a graph object
class Graph:
    def __init__(self, n, edges=[]):
        # resize both lists to hold `n` elements each
        self.adjList = [[] for _ in range(n)]
        self.indegree = [0] * n

        for edge in edges:
            self.addEdge(edge[0], edge[1])

    # Function to add an edge (u, v) to the graph
    # and update in-degree for each edge
    def addEdge(self, u, v):
        # add an edge from source to destination
        self.adjList[u].append(v)
        # increment in-degree of destination vertex by 1
        self.indegree[v] = self.indegree[v] + 1


# Function to perform DFS traversal on the graph
def DFS(graph, v, discovered):
    discovered[v] = True  # mark the current node as discovered

    # do for every edge (v, u)
    for u in graph.adjList[v]:
        if not discovered[u]:  # `u` is not discovered
            DFS(graph, u, discovered)


# Function to create transpose of a graph, i.e., the same graph
# with the direction of every edge reversed
def buildTranspose(graph, n):
    g = Graph(n)
    for u in range(n):
        # for every edge (u, v), create a reverse edge (v, u)
        # in the transpose graph
        for v in graph.adjList[u]:
            g.addEdge(v, u)
    return g


# Function to check if all vertices of a graph with a non-zero degree are discovered
def isdiscovered(graph, discovered):
    for i in range(len(discovered)):
        if len(graph.adjList[i]) and not discovered[i]:
            return False
    return True


# Function to check if all vertices with a non-zero degree in a graph belong to a
# single strongly connected component using Kosaraju’s algorithm
def isSC(graph, n):
    # keep track of all previously discovered vertices
    discovered = [False] * n

    # find the first vertex `i` with a non-zero degree, and start DFS from it
    for i in range(n):
        if len(graph.adjList[i]):
            DFS(graph, i, discovered)
            break

    # return false if DFS couldn't visit all vertices with a non-zero degree
    if not isdiscovered(graph, discovered):
        return False

    # reset the discovered array
    discovered[:] = [False] * n

    # create a transpose of the graph
    g = buildTranspose(graph, n)

    # perform DFS on the transpose graph using the same starting vertex as
    # used in the previous DFS call
    DFS(g, i, discovered)

    # return true if second DFS also explored all vertices with a non-zero degree;
    # false otherwise
    return isdiscovered(g, discovered)


# Function to check if a directed graph has an Eulerian cycle
def hasEulerianCycle(graph, n):
    # check if every vertex has the same in-degree and out-degree
    for i in range(n):
        if len(graph.adjList[i]) != graph.indegree[i]:
            return False

    # check if all vertices with a non-zero degree belong to a single
    # strongly connected component
    return isSC(graph, n)


if __name__ == '__main__':

    # List of graph edges as per the above diagram
    edges = [(0, 1), (1, 2), (2, 3), (3, 1), (1, 4), (4, 3), (3, 0)]

    # total number of nodes in the graph (labelled from 0 to 4)
    n = 5

    # build a directed graph from the above edges
    graph = Graph(n, edges)

    if hasEulerianCycle(graph, n):
        print('The graph has an Eulerian cycle')
    else:
        print('The Graph does not contain Eulerian cycle')