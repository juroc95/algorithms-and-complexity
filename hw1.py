
# CS 350: Homework 1
# Due: Week of 4/4
# Name: Juhwan Lee

# This homework is largely review, and to make sure you have a working version of python.

############################################################################
#
# Problem 1
# Find the largest two elements in a list.
# Return your answer in a tuple as (largest, secondLargest)
#
# Running Time: theta(2n)
############################################################################

def largest2(l):
    """
    >>> largest2([1, 2, 3, 4, 5, 6, 7])
    (7, 6)
    >>> largest2([7, 6, 5, 4, 3, 2, 1])
    (7, 6)
    """
    largest = 0
    secondLargest = 0
    for x in l:
        if x > largest:
            largest = x
    for x in l:
        if x < largest and x > secondLargest:
            secondLargest = x
    return (largest, secondLargest)

############################################################################
#
# Problem 2
# Reverse a list in place,
# and returned the reversed list.
#
# Running Time: theta(1/2n)
############################################################################

def reverse(l):
    """
    >>> l = [1, 2, 3, 4, 5]
    >>> reverse(l)
    [5, 4, 3, 2, 1]
    >>> l
    [5, 4, 3, 2, 1]
    """
    for i in range(len(l)/2):
        temp1 = l[i]
        temp2 = l[-i-1]
        l[i] = temp2
        l[-i-1] = temp1
    return l

############################################################################
#
# Problem 3
# Compute the transpose of a matrix in place.
#
# What is the input size measuring? size of matrix m
# Running Time: theta(n^2)
############################################################################

def transpose(m):
    """
    >>> m = [[1,2,3],[4,5,6],[7,8,9]]
    >>> transpose(m)
    [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
    >>> m
    [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
    """
    lst = []
    mtrx = []
    for i in range(len(m[0])):
        for j in range(len(m)):
            lst.append(m[j][i])
        mtrx.append(lst)
        lst = []
    m[:] = mtrx
    return m

############################################################################
#
# Problem 4
# Given a list of points, return the distance between the two closest points.
# The distance between two points (x1,y1) and (x2,y2) is:
# d = sqrt((x2-x1)^2 + (y2-y1)^2)
#
# Running Time: theta(n^2)
############################################################################

import math
def pointDist(points):
    """
    >>> pointDist([(1,1), (4,5), (13,6)])
    5
    """
    closest = 0
    for i in range(0, len(points) - 1):
        for j in range(i+1, len(points)):
            distance = math.sqrt(((points[j][0]-points[i][0])**2) + ((points[j][1]-points[i][1])**2))
            if i == 0 and j == 1:
                closest = distance
            if distance < closest:
                closest = distance
    return int(closest)

############################################################################
#
# Problem 5
# multiply two matrices A and B.
# For the running time A is an m*n matrix, and B is an n*l matrix.
#
# what is the size of the output? m*l matrix
# Running Time: theta(n^3)
############################################################################

def matMul(A,B):
    """
    >>> matMul([[1, 2, 3], [4, 5, 6]], [[7, 8], [9, 10], [11, 12]])
    [[58, 64], [139, 154]]
    """
    lst = []
    mtrx = []
    element = 0
    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(B)):
                element += A[i][k] * B[k][j]
            lst.append(element)
            element = 0
        mtrx.append(lst)
        lst = []
    return mtrx

############################################################################
#
# Problem 6
# Compute the number of 1s that would be in the binary representation of x
# for example: 30 = 11110 in base 2, and it has 4 1s.
#
# For full credit, you should assume that 
# arithmetic operations are *not* constant time.
# bitwise operations are constant time though.
#
# What is the input size? size of number x
# Running Time: theta(logn)
############################################################################

def popcount(x):
    """
    >>> popcount(7)
    3
    >>> popcount(30)
    4
    >>> popcount(256)
    1
    """
    count = 0
    while x:
        count += x & 1
        x >>= 1
    return count

############################################################################
#
# Problem 7
# compute the integer square root of x.
# This is the largest number s such that s^2 <= x.
#
# You can assume that arithmetic operations are constant time for this algorithm.
#
# What is the input size? size of number x
# Running Time: theta(logn)
############################################################################

def isqrt(x):
    """
    >>> isqrt(6)
    2
    >>> isqrt(121)
    11
    >>> isqrt(64)
    8
    """
    result = 0
    while result ** 2 <= x:
        result += 1
    return result - 1

############################################################################
#
# Problem 8: Word Search
#
# determine if string s is any where in the word grid g.
#
# for example s = "bats"
# g = ["abrql",
#      "exayi",
#      "postn",
#      "cbkrs"]
#
# Then s is in the word grid
#     [" b   ",
#      "  a  ",
#      "   t ",
#      "    s"]
#
# what is your input size? size of word + size of gird
# Running Time: theta(n^3)
############################################################################

def wordSearch(word,grid):
    """
    >>> s = "bats"
    >>> g = ["abrql", "exayi", "postn", "cbkrs"]
    >>> wordSearch(s,g)
    True
    >>> s = "ages"
    >>> g = ["axmy", "bgdf", "xeet", "raks"]
    >>> wordSearch(s,g)
    True
    >>> s = "bird"
    >>> g = ["abcd", "wert", "uiop", "bnmq"]
    >>> wordSearch(s, g)
    True
    """
    word_length = len(word)
    x_length = len(grid[0])
    y_length = len(grid)
    result = False
    k = 0
    for j in range(y_length):
        for i in range(x_length):
            if word[k] == grid[j][i]:
                k = 1
                temp1 = j
                temp2 = i
                # (1) x - 1 , y
                while i > 0 and k < word_length:
                    i -= 1
                    if word[k] == grid[j][i]:
                        k += 1
                    else:
                        i = temp2
                        k = 1
                        break
                # if word is found, return
                if k == word_length:
                    result = True
                    break
                else:
                    i = temp2
                    k = 1
                # (2) x - 1 , y - 1
                while i > 0 and j > 0 and k < word_length:
                    i -= 1
                    j -= 1
                    if word[k] == grid[j][i]:
                        k += 1
                    else:
                        j = temp1
                        i = temp2
                        k = 1
                        break
                # if word is found, return
                if k == word_length:
                    result = True
                    break
                else:
                    j = temp1
                    i = temp2
                    k = 1
                # (3) x , y - 1
                while j > 0 and k < word_length:
                    j -= 1
                    if word[k] == grid[j][i]:
                        k += 1
                    else:
                        j = temp1
                        k = 1
                        break
                # if word is found, return
                if k == word_length:
                    result = True
                    break
                else:
                    j = temp1
                    k = 1
                # (4) x + 1 , y - 1
                while i + 1 < x_length and j > 0 and k < word_length:
                    i += 1
                    j -= 1
                    if word[k] == grid[j][i]:
                        k += 1
                    else:
                        j = temp1
                        i = temp2
                        k = 1
                        break
                # if word is found, return
                if k == word_length:
                    result = True
                    break
                else:
                    j = temp1
                    i = temp2
                    k = 1
                # (5) x + 1, y
                while i + 1 < x_length and k < word_length:
                    i += 1
                    if word[k] == grid[j][i]:
                        k += 1
                    else:
                        i = temp2
                        k = 1
                        break
                # if word is found, retrun
                if k == word_length:
                    result = True
                    break
                else:
                    i = temp2
                    k = 1
                # (6) x + 1 , y + 1
                while i + 1 < x_length and j + 1 < y_length and k < word_length:
                    i += 1
                    j += 1
                    if word[k] == grid[j][i]:
                        k += 1
                    else:
                        j = temp1
                        i = temp2
                        k = 1
                        break
                # if word is found, return
                if k == word_length:
                    result = True
                    break
                else:
                    j = temp1
                    i = temp2
                    k = 1
                # (7) x , y + 1
                while j + 1 < y_length and k < word_length:
                    j += 1
                    if word[k] == grid[j][i]:
                        k += 1
                    else:
                        j = temp1
                        k = 1
                        break
                # if word is found, return
                if k == word_length:
                    result = True
                    break
                else:
                    j = temp1
                    k = 1
                # (8) x - 1 , y + 1
                while i > 0 and j + 1 < y_length and k < word_length:
                    i -= 1
                    j += 1
                    if word[k] == grid[j][i]:
                        k += 1
                    else:
                        j = temp1
                        i = temp2
                        k = 1
                        break
                # if word is found, return
                if k == word_length:
                    result = True
                    break
                else:
                    j = temp1
                    i = temp2
                    k = 1
            # reset k
            k = 0
        # if word is found, return
        if result == True:
            break
    # return the result
    return result

############################################################################
#
# Problem 9: Convex Hull
#
# In class we learned about the convex hull problem.
# We also learned that for any line segment on the convex hull,
# every other point will be on the same side of that line.
#
# Use this fact to write an algorithm to find all of the points in the convex hull.
#
# for example: [(1,1), (4,2), (4,5), (7,1)] are the points shown below
#
#    *
#
#    *
# *     *
#
# The convex hull is [(1,1), (4,5), (7,1)]
#    *
#   / \
#  /   \
# *-----*
#
# Running Time: theta(n^3)
############################################################################

def convexHull(points):
    """
    >>> convexHull([(1,1), (4,2), (4,5), (7,1)])
    [(1, 1), (4, 5), (7, 1)]
    >>> convexHull([(18, 44), (4, 6), (28, 24), (1, 33), (45, 23), (38, 29), (16, 48), (19, 12), (29, 10), (17, 20)])
    [(4, 6), (1, 33), (16, 48), (45, 23), (29, 10)]
    >>> convexHull([(34, 48), (19, 3), (21, 11), (1, 15), (21, 48), (47, 20), (44, 12), (22, 0), (28, 26), (18, 0)])
    [(18, 0), (1, 15), (21, 48), (34, 48), (47, 20), (44, 12), (22, 0)]
    """
    lowest_y = points[0][1]
    lowest_x = points[0][0]
    first_point = (lowest_x, lowest_y)
    for (x,y) in points:
        if y == lowest_y and x < lowest_x:
            first_point = (x,y)
            lowest_x = x
        elif y < lowest_y:    
            first_point = (x,y)
            lowest_y = y
            lowest_x = x
    right_counter = same_counter = left_counter = 0
    convex_hull = []
    convex_hull.append(first_point)
    points.remove(first_point)
    flag = True

    while flag == True:
        point_1 = first_point

        for i in range(len(points)):
            point_2 = points[i]

            for j in range(len(points)):
                point_3 = points[j]
                if point_3 == point_2:
                    continue
                
                value = ((point_2[0] - point_1[0]) * (point_3[1] - point_1[1]) 
                        - (point_2[1] - point_1[1]) * (point_3[0] - point_1[0]))
                if value > 0:
                    left_counter += 1
                elif value == 0:
                    same_counter += 1
                elif value < 0:
                    right_counter += 1

            if left_counter != 0 and same_counter == 0 and right_counter == 0:
                if point_2 == convex_hull[0]:
                    flag = False
                    break
                convex_hull.append(point_2)
                points.append(point_1)
                first_point = point_2
                points.remove(first_point)
            elif left_counter == 0 and same_counter == 0 and right_counter != 0:
                if point_2 == convex_hull[0]:
                    flag = False
                    break
                convex_hull.append(point_2)
                points.append(point_1)
                first_point = point_2
                points.remove(first_point)
            left_counter = same_counter = right_counter = 0
        if flag == False:
            break

    return convex_hull
            
############################################################################
#
# Problem 10: Running time
#
# Find the Theta time complexity for the following functions.
# If the problem is a summation, give a closed form first.
#
# 1. f(n) = n^2 + 2n + 1
# 1. theta(n^2)
# 2. f(n) = sum(i=0, n, sum(j=0, i, 1))
# 2. theta(n^2)
# 3. f(n) = (n+1)!
# 3. theta(n!)
# 4. f(n) = sum(i=0, n, log(i))
# 4. theta(nlogn)
# 5. f(n) = log(n!)
# 5. theta(nlogn)
############################################################################

if __name__ == "__main__":
    import doctest
    doctest.testmod()
