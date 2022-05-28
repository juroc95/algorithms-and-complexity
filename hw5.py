# CS 350: Homework 5
# Due: Week of 5/9
# Name: Juhwan Lee

# You should not assume anything about the data for these problems
# other than it's valid.
# Adjacency lists might not be in any particular order
# and graphs may not be connected.

############################################################################
#
# Problem 1
#
# write a function that returns the set of connected components 
# of an undirected graph g.
# g is represented as an adjacency list
# you should return a list of components, where each component is a list of vertices.
# Example g = [[1,2], [0,2], [0,1], [4], [3]]
# Should return a list of two components [[0,1,2],[3,4]]
#
# Running time? theta(V+E)
#
############################################################################

def components(g):
    """
    >>> components([[1,2], [0,2], [0,1], [4], [3]])
    [[0, 1, 2], [3, 4]]
    >>> components([[0,1], [1,0], [2,3], [3,2,4], [4,3]])
    [[0, 1], [2, 3, 4]]
    """
    num = len(g)
    visited = [False] * num
    stack = []
    result = []

    def components_rec(g, v, visited, stack):
        visited[v] = True
        stack.append(v)
        for adj in g[v]:
            if visited[adj] == False:
                components_rec(g, adj, visited, stack)

    for i in range(num):
        if visited[i] == False:
            components_rec(g, i, visited, stack)
            result.append(stack)
            stack = []
    return result


############################################################################
#
# Problem 2
#
# write a function the returns True if, and only if, graph g is bipartite
# g is represented as an adjacency list
#
# Running time? theta(V+E)
#
############################################################################

from collections import deque

def bipartite(g):
    """
    >>> bipartite([[3,4,7], [3,5,6], [4,5,7], [0,1], [0,2], [1,2], [1], [0,2]])
    True
    >>> bipartite([[1,3], [0,2], [1,3], [0,2]])
    True
    """
    num = len(g)
    color_list = [-1] * num
    for i in range(num):
        if color_list[i] != -1:
            continue
        q = deque()
        q.append((i, 0))
        #bfs
        while q:
            vertex, color = q.popleft()
            if color_list[vertex] == -1:
                color_list[vertex] = color
                for adj in g[vertex]:
                    if color == 1:
                        q.append((adj, 0))
                    else:
                        q.append((adj, 1))
            if color_list[vertex] != color:
                return False
    return True


############################################################################
#
# Problem 3
#
# write a function the returns True if, and only if, graph g is a forrest
# g is represented by a adjacency list.
#
# Running time? theta(V+E)
#
############################################################################

def isForrest(g):
    """
    >>> isForrest([[1,2], [3,4], [5,6], [], [], [], []])
    True
    >>> isForrest([[1,2], [3,4], [5,4], [], [], []])
    False
    """
    num = len(g)
    visited = [False] * num

    def isForrest_rec(vertex, prev):
        if visited[vertex] == True:
            return False
        visited[vertex] = True
        for adj in g[vertex]:
            if adj == None:
                return True
            if adj != prev:
                if not isForrest_rec(adj, vertex):
                    return False
        return True

    for vertex in range(num):
        if visited[vertex] == False and not isForrest_rec(vertex, -1):
            return False
    return True


############################################################################
#
# Problem 4
#
# write a function to topologically sort the vertices of a directed graph d
# Assume d is an adjacency list.
#
# Running time? theta(V+E)
#
############################################################################

def topsort(d):
    """
    >>> topsort([[1, 2], [3], [3], []])
    [0, 2, 1, 3]
    >>> topsort([[], [], [3], [1], [0,1], [0,2]])
    [5, 4, 2, 3, 1, 0]
    """
    num = len(d)
    visited = [False] * num
    stack = []
    result = []

    def topsort_rec(d, v, visited, stack):
        visited[v] = True
        for adj in d[v]:
            if visited[adj] == False:
                topsort_rec(d, adj, visited, stack)
        stack.append(v)

    for i in range(num):
        if visited[i] == False:
            topsort_rec(d, i, visited, stack)

    while stack:
        result.append(stack.pop())

    return result


############################################################################
#
# Problem 5
#
# write a function to determine the strongly connected components of digraph d.
# Just like the components example, you should return a list of strongly connected components.
#
# Running time? theta(V+E)
#
############################################################################

def scc(d):
    """
    >>> scc([[1], [2], [0,3], [1,2], [3,5,6], [4], [7], [8], [6]])
    [[0, 1, 2, 3], [4, 5], [6, 7, 8]]
    """
    num = len(d)
    visited = [False] * num
    stack = []
    result = []

    def scc_rec(d, v, visited, stack):
        visited[v] = True
        for adj in d[v]:
            if visited[adj] == False:
                scc_rec(d, adj, visited, stack)
        stack.append(v)

    for i in range(num):
        if visited[i] == False:
            scc_rec(d, i, visited, stack)
    
    dt = [[] for _ in range(num)]
    for i in range(num):
        for x in d[i]:
            dt[x].append(i)
    
    visited = [False] * num
    scc = []

    while stack:
        i = stack.pop()
        if visited[i] == False:
            scc_rec(dt, i, visited, scc)
            scc.sort()
            result.append(scc)
            scc = []

    result.sort()
    return result


############################################################################
#
# Problem 6
#
# a. What do we need to change about BFS/DFS if we use an adjacency matrix?
# Create a matrix of size n*n where every element is 0 representing there is no edge in the graph
# and for every edge of the graph between the vertices i and j set matrix[i][j] = 1.
# In BFS/DFS, instead of iterating every adj of vertices, we check if matrix[i][j] == 1
#
# b. What is the running time for BFS/DFS if we use and adjacency matrix?
# theta(V^2)
#
# c. Give an example of a weighted graph where BFS doesn't return the shortest path.
# A to B weight 3
# A to C weight 1
# C to B weight 1
# shortest path from A to B, BFS will return A to B weight 3
# not A to C to B weight 2
#
############################################################################

if __name__ == "__main__":
    import doctest
    doctest.testmod()