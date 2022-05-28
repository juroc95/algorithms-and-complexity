
# CS 350: Homework 6
# Due: Week of 6/16
# Name: Juhwan Lee



def machine(data, code):
    i = 0
    value = 0
    for instruction in code:
        if i >= len(data):
            raise Exception("Ran out of numbers")
        if instruction == "ADD":
            value += data[i]
            i += 1
        elif instruction == "MUL":
            value += data[i] * data[i+1]
            i += 2
        else:
            raise Exception("Illegal Instruction: " + instruction)
    if i < len(data):
        raise Exception("has leftover numbers")
    return value

###########################################################################
# Problem 1:
#
# I've constructed a new data processing language that I call addmul.
# It is a very simple language, programs in addmul consist of two instructions.
# ADD take a value from the data stream and adds it to the current total
# MUL takes the next two number from the current data stream, multiplies them together
# and adds them to the total.
# That's it.
#
# Your job is to take the data stream (just a list of numbers), and determine
# the program that will produce the largest value.
#
# example:
# largetstProgram([2,3,5])
# should return
# ["ADD","MUL"]
# because this will return 17
# where ["MUL","ADD"] will return 11
# and ["ADD","ADD","ADD"] will return 10
#
# You can run your program by calling 
# machine([2,3,4], ["ADD", "MUL"]) 
# to run your program
#
# running time: O(n)
###########################################################################

def largestProgram(data):
    """
    >>> largestProgram([2,3,5])
    ['ADD', 'MUL']
    >>> largestProgram([1,2,3,4])
    ['ADD', 'ADD', 'MUL']
    """
    num = len(data)
    memos = [None] * num
    result = []
    val = largestProgram_rec(0, data, memos, result)
    return val[1]

def largestProgram_rec(current, data, memos, result):
    if current == len(data):
        return machine(data, result), result
    if memos[current] is not None:
        return memos[current]
    if len(data) - current == 1:
        result.append("ADD")
        val = largestProgram_rec(current+1, data, memos, result)
        memos[current] = val
        return val
    else:
        result2 = []
        result2[:] = result
        result.append("ADD")
        result2.append("MUL")
        val = max(largestProgram_rec(current+1, data, memos, result), largestProgram_rec(current+2, data, memos, result2))
        memos[current] = val
        return val


###########################################################################
# Problem 2
#
# Implemnt the Floyd-Warshal algorithm from class
#
# For example, the adjacency matrix:
#    [ [  0, inf,  -2, inf], 
#      [  4,   0,   3, inf], 
#      [inf, inf,   0,   2], 
#      [inf,  -1, inf,   0] ]
# should give the distance matrix:
#    [ [  0,  -1,  -2,   0], 
#      [  4,   0,   2,   4], 
#      [  5,   1,   0,   2], 
#      [  3,  -1,   1,   0] ]
# 
#
# Running Time: O(V^3)
###########################################################################

def floyd(g):
    """
    #>>> floyd([ [0, math.inf, -2, math.inf], [4, 0, 3, math.inf], [math.inf, math.inf, 0, 2], [math.inf, -1, math.inf, 0]])
    #[ [  0,  -1,  -2,   0], [  4,   0,   2,   4], [  5,   1,   0,   2], [  3,  -1,   1,   0] ]
    >>> floyd([ [0, float('inf'), -2, float('inf')], [4, 0, 3, float('inf')], [float('inf'), float('inf'), 0, 2], [float('inf'), -1, float('inf'), 0]])
    [[0, -1, -2, 0], [4, 0, 2, 4], [5, 1, 0, 2], [3, -1, 1, 0]]
    """
    n = len(g)
    for w in range(n):
        for u in range(n):
            for v in range(n):
                if u == v or u == w or v == w:
                    continue
                g[u][v] = min(g[u][v], g[u][w] + g[w][v])
    return g


###########################################################################
# Problem 3
#
# Congratulations! You know own a factory that cuts rods.
# Customers will pay a certain value for a length of rods
# for example
# rod length:  3  4  5  6   7
# price:       2  3  6  8  11
#
# You just received a rod of length d, 
# Write a function to determine the most efficient way to cut the rod
# to maximize the profit.
# You should return the maximum profit you can make.
#
###########################################################################

def rods(weights, prices, d):
    """
    >>> rods([3,4,5,6,7], [2,3,6,8,11], 20)
    30
    """
    memo = [[None for _ in range(d+1)] for _ in range(len(weights))]
    return rods_rec(weights, prices, len(weights)-1, d, memo)

def rods_rec(weights, prices, i, d, memo):
    if memo[i][d] is not None:
        return memo[i][d]
    if i == 0 or d == 0:
        result = 0
    elif weights[i] > d:
        result = rods_rec(weights, prices, i-1, d, memo)
    else:
        result = max(rods_rec(weights, prices, i, d-weights[i], memo) + prices[i], rods_rec(weights, prices, i-1, d, memo))
    memo[i][d] = result
    return result


############################################################################
# Problem 4: Parenthesizing matrices.
#
# This is the same problem as homework 4, problem 3,
# but this time I want you to do it in polynomial time using dynamic programming.
# 
# If I multiply and m*l matrix A by an l*n matrix B
# That will take O(n*l*m) time to compute.
#
# If I include a n*o matrix C in this product
# Then I have the m*o matrix A*B*C.
# This is perfectly well defined, but I have a choice.
# Do I multiply (A*B)*C (giving a running time of n*l*m + n*m*o)
# or do i multiply A*(B*C) (giving a running time of l*m*o + n*l*o)
#
# Since matrix multiplication is associative, We will get the same answer.
#
# So, given a list of dimensions of matrices
# (for example [(n,l), (l,m), (m,o)])
# compute the fastest running time that we can do matrix multiplication in. 
#
# example [(3,5), (5,4), (4,7)]
# is 3*5*4 + 3*4*7 = 144
# 
# Running time: O(n^3)
############################################################################

def matrixParens(sizes):
    """
    >>> matrixParens([(3,5), (5,4), (4,7)])
    144
    """
    table = [[float('inf') for _ in range(len(sizes))] for _ in range(len(sizes))]
    for i in range(len(sizes)):
        table[i][i] = 0
    for offset in range(1, len(sizes)):
        for start in range(len(sizes)):
            end = start + offset
            if end >= len(sizes):
                break
            for sep in range(start, end):
                table[start][end] = min(table[start][end], table[start][sep] + table[sep+1][end] + (sizes[start][0] * sizes[sep][1] * sizes[end][1]))
    return table[0][-1]

############################################################################

if __name__ == "__main__":
    import doctest
    doctest.testmod()
