
# CS 350: Homework 7
# Due: Week of 5/25
# Name: Juhwan Lee

################################################################
# Problem 1
# 
# We're going to take the job scheduling problem from class,
# but this time, I want to make sure every job is scheduled.
# If I have a set of n jobs where each job is represented
# by a tuple (s,f),
# Give a greedy algorithm to schdule the jobs on the fewest
# number of processors total
#
# Running Time: O(n^4)
#
################################################################

def schedule(jobs):
    """
    >>> schedule([(5,40), (30,35), (6,20), (19, 31), (23, 29), (28, 32)])
    [[(6, 20), (23, 29), (30, 35)], [(19, 31)], [(28, 32)], [(5, 40)]]
    """
    result = []
    scheduled = []
    current_time = 0
    sorted_jobs = sorted(jobs, key=lambda x: x[1])
    while sorted_jobs:
        for x in sorted_jobs:
            if current_time <= x[0]:
                scheduled.append(x)
                current_time = x[1]
        for x in scheduled:
            if x in sorted_jobs:
                sorted_jobs.remove(x)
        result.append(scheduled)
        scheduled = []
        current_time = 0
    return result

################################################################
# Problem 2
# 
# Given a list of string (strings)
# Find s short string (bigstring) that 
# for every s in string, s is a substring of bigstring.
#
# Use the approximation algorithm we gave in class.
#
# Running Time: O(n^4)
#
################################################################

def superstring(strings):
    """
    >>> superstring(["CADBC", "CDAABD", "BCDA", "DDCA", "ADBCADC"])
    'BCDAABDDCADBCADC'
    >>> superstring(["catg", "ctaagt", "gcta", "ttca", "atgcatc"])
    'gctaagttcatgcatc'
    """
    result = []
    back_front = []
    front_back = []

    for x in strings:
        result.append(x)

    while len(result) != 1:

        # str1 back str2 front
        largest = 0
        for i in range(0, len(result)-1):
            for j in range(i+1, len(result)):
                str1 = len(result[i])
                str2 = len(result[j])
                counter = 0
                if str1 <= str2:
                    a = 0
                    b = 0
                else:
                    a = str1 - str2
                    b = 0
                for k in range(min(str1, str2)):
                    if result[i][a] == result[j][b]:
                        counter += 1
                        a += 1
                        b += 1
                    else:
                        counter = 0
                        if str1 <= str2:
                            a = k + 1
                        else:
                            a = str1 - str2 + k + 1
                        b = 0
                if counter > largest:
                    largest = counter
                    str1_pos = i
                    str2_pos = j

        back_front.append(largest)
        back_front.append(str1_pos)
        back_front.append(str2_pos)

        # str1 front str2 back
        largest = 0
        for i in range(0, len(result)-1):
            for j in range(i+1, len(result)):
                str1 = len(result[i])
                str2 = len(result[j])
                counter = 0
                if str1 >= str2:
                    a = 0
                    b = 0
                else:
                    a = 0
                    b = str2 - str1
                for k in range(min(str1, str2)):
                    if result[i][a] == result[j][b]:
                        counter += 1
                        a += 1
                        b += 1
                    else:
                        counter = 0
                        a = 0
                        if str1 >= str2:
                            b = k + 1
                        else:
                            b = str2 - str1 + k + 1
                if counter > largest:
                    largest = counter
                    str1_pos = i
                    str2_pos = j
                    
        front_back.append(largest)
        front_back.append(str1_pos)
        front_back.append(str2_pos)

        if back_front[0] >= front_back[0]:
            new_str = result[back_front[1]] + result[back_front[2]][back_front[0]:]
            del result[back_front[1]]
            del result[back_front[2] - 1]
            result.append(new_str)

        else:
            new_str = result[front_back[2]] + result[front_back[1]][front_back[0]:]
            del result[front_back[1]]
            del result[front_back[2] - 1]
            result.append(new_str)
        
        back_front = []
        front_back = []

    return result[0]


################################################################
# Problem 3
# 
# Find the shortest path from a to b
# in a weighted graph g that is represented by an adjacency matrix.
# You can assume all edge weights are positive.
#
# Running time: O(ElogV)
################################################################

import heapq

def dijkstra(g, a, b):
    """
    >>> g = [ [(1,3), (2,6)], \
              [(0,3), (4,4)], \
              [(0,6), (3,2), (5,7)], \
              [(2,2), (4,4), (8,1)], \
              [(1,4), (3,4), (6,9)], \
              [(2,7), (6,2), (7,8)], \
              [(4,9), (5,2), (9,4)], \
              [(5,8), (8,3)], \
              [(3,1), (7,3), (9,2)], \
              [(6,4), (8,2)] ]
    >>> dijkstra(g,0,9)
    [0, 2, 3, 8, 9]
    """
    q = []
    distance = [float('inf') for _ in range(len(g))]
    path = [None for _ in range(len(g))]
    heapq.heappush(q, (0, a))
    distance[a] = 0
    path[a] = 0
    result = []
    while q:
        dist, now = heapq.heappop(q)
        if dist > distance[now]:
            continue
        for i in g[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                path[i[0]] = now
                heapq.heappush(q, (cost, i[0]))
    result.append(b)
    while b != a:
        if path[b] != None:
            result.append(path[b])
            b = path[b]
        else:
            result = []
            b = a
    result.reverse()
    return result


################################################################

if __name__ == "__main__":
    import doctest
    doctest.testmod()
