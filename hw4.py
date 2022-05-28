# CS 350: Homework 4
# Due: Week of 4/4
# Name: Juhwan Lee

############################################################################
# Problem 1: Quicksort
# 
# implement quicksort described in class.
#
# Recurrence worst case: N + T(N-1)
# Recurrence average case: 2T(N/2) + N
# Running time worst case: theta(n^2)
# Running time average case: theta(nlogn)
# 
# When does the worst case happen? If the list is already sorted
############################################################################

def quicksort(l):
    """
    >>> quicksort([3, 2, 6, 1, 4])
    [1, 2, 3, 4, 6]
    >>> quicksort([5, 4, 3, 2, 1])
    [1, 2, 3, 4, 5]
    """
    if len(l) < 2:
        return l
    pivot = l[0]
    smaller = []
    larger = []
    equal = [pivot]
    for i in range(1, len(l)):
        if l[i] < pivot:
            smaller.append(l[i])
        elif l[i] > pivot:
            larger.append(l[i])
        else:
            equal.append(l[i])
    return quicksort(smaller) + equal + quicksort(larger)

############################################################################
# Problem 2: maximum sublist sum
# 
# A sublist is a contiguous piece of a list
# [1,2,1] is a sublist of [4,1,2,1,3]
# but [1,2,3] isn't.
#
# the sum of a list is just adding all of the elements.
#
# compute the maximum sum of any sublist.
# For example:  [-2,1,-3,4,-1,2,1,-5,4]
# the maximum sublist is [4,-1,2,1] with a sum of 6
# 
# Running time: theta(n^3)
############################################################################

def maxSublist(l):
    """
    >>> maxSublist([-2, 1, -3, 4, -1, 2, 1, -5, 4])
    [4, -1, 2, 1]
    """
    max = 0
    result = []
    temp = []
    for i in range(0, len(l)):
        buffer = l[i]
        temp = [l[i]]
        if buffer > max:
            max = buffer
            result[:] = temp
        if i < len(l):
            for j in range(i+1, len(l)):
                buffer += l[j]
                temp.append(l[j])
                if buffer > max:
                    max = buffer
                    result[:] = temp
    return result

############################################################################
# Problem 3: Parenthesizing matrices.
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
# Running time: theta(n^3)
############################################################################

def matrixParens(sizes):
    """
    >>> matrixParens([(3,5), (5,4), (4,7)])
    144
    >>> matrixParens([(5,4), (4,6), (6,2), (2,7)])
    158
    """
    table = [[999 for _ in range(len(sizes))] for _ in range(len(sizes))]
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
# Problem 4: Convex Hull again!
# 
# Use the Divide and Conquer algorithm described in class to compute
# the convex hull of a set of points.
#
# Recurrence worst case: N + T(N-1)
# Recurrence average case: 2T(N/2) + N
# Running time worst case: theta(n^2)
# Running time average case: theta(nlogn)
# 
# When does the worst case happen? If the points are in the border of a circle
############################################################################

def convexHull(points):
    """
    >>> convexHull([(1,1), (2,2)])
    [(1, 1), (2, 2)]
    >>> convexHull([(1,1), (4,2), (4,5), (7,1)])
    [(1, 1), (7, 1), (4, 5)]
    >>> convexHull([(18, 44), (4, 6), (28, 24), (1, 33), (45, 23), (38, 29), (16, 48), (19, 12), (29, 10), (17, 20)])
    [(1, 33), (45, 23), (16, 48), (4, 6), (29, 10)]
    >>> convexHull([(34, 48), (19, 3), (21, 11), (1, 15), (21, 48), (47, 20), (44, 12), (22, 0), (28, 26), (18, 0)])
    [(1, 15), (47, 20), (21, 48), (34, 48), (22, 0), (44, 12), (18, 0)]
    """
    if len(points) == 1:
        return points
    left = right = points[0]
    for (x,y) in points:
        if x < left[0]:
            left = (x,y)
    for (x,y) in points:
        if x > right[0]:
            right = (x,y)
    result = []
    result.append(left)
    result.append(right)
    furthest(left, right, points, result)
    furthest(right, left, points, result)
    return result

def furthest(left, right, points, result):
    max_t = 0
    top = left
    flag = 0
    for i in range(len(points)):
        if points[i] == left or points[i] == right:
            continue
        t1 = ((left[0] * right[1]) + (right[0] * points[i][1]) + (points[i][0] * left[1])) - ((right[0] * left[1]) + (points[i][0] * right[1]) + (left[0] * points[i][1]))
        t2 = (0.5) * abs(((left[0] - points[i][0]) * (right[1] - left[1]) - (left[0] - right[0]) * (points[i][1] - left[1])))
        if t1 > 0:
            if t2 > max_t:
                max_t = t2
                top = points[i]
                flag = 1
    if flag == 1:
        result.append(top)
        furthest(left, top, points, result)
        furthest(top, right, points, result)
    else:
        return

############################################################################
# Problem 5: Recurrence relations
# 
# Give a closed form, and bit Theta for the following recurrence relations.
# If it's a divide and conquer relation, then you only need to give the Theta.
#
# a. Give the recurrence relation for Karatsuba's algorithm, and solve it.
#   T(n) = 3T(n/2) + 3n             T(1) = 1
#   T(n) = theta(n^log3)
# b. Give the recurrence relation for Strassen's algorithm, and solve it.
#   T(n) = 7T(n/2) + theta(n^2)     T(1) = 1
#   T(n) = theta(n^log7)
# c.
# T(1) = 1
# T(n) = T(n-1) + n
#   T(n) = theta(n^2)
# d. 
# T(1) = 1
# T(n) = 2T(n-2) + 1
#   T(n) = theta(n)
# 
############################################################################

if __name__ == "__main__":
    import doctest
    doctest.testmod()