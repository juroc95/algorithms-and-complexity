
# CS 350: Homework 1
# Due: Week of 4/18
# Name: Juhwan Lee

# for this homework, unless I'm asking you to sort a list,
# you are allowed to use the sorted function in Python.
# sorted takes a list, and returns a sorted copy of the list in Theta(n*log(n)) time.

############################################################################
#
# Problem 1
# Compute the largest gap between two numbers in a list.
#
# for example: gap([1,6,2,4,9]) == 3 because the gap between 6 and 9 is 3.
############################################################################

def gap(l):
    sorted_list = sorted(l)
    previous = l[0]
    largest_gap = 0
    for i in range(len(sorted_list)):
        gap = sorted_list[i] - previous
        if gap > largest_gap:
            largest_gap = gap
        previous = sorted_list[i]
    return largest_gap

############################################################################
#
# Problem 2
# We can concatenate two numbers together to get a new number.
# for example: 44 concatenated with 55 = 4455
# We can concatenate a list of numbers by concatenating all the numbers.
# concat([1,2,55,3]) = 12553
#
# If we rearrange the list, we can get a different number.
# concat([2,55,1,3]) = 25513
#
# Write a function to find the largest value we can get from concatenating a list.
#
# Running Time: theta(n^2)
############################################################################

def concatenate(l):
    out = ""
    for x in l:
        out = out + str(x)
    return int(out)

def largestConcat(l):
    result = []
    for x in l:
        result.append(str(x))
    sorted_list = sorted(result, reverse=True)
    return concatenate(sorted_list)

############################################################################
#
# Problem 3
# Write a function to return the number of unique elements in an array.
# for example the list [3,6,2,3,2,7,4] has 3 unique elements, 6, 7, and 4.
#
# Running Time: theta(n^2)
############################################################################

def numberUnique(l):
    result = []
    copy_list = l
    counter = 0
    for x in copy_list:
        copy_list.remove(x)
        if x not in copy_list:
            result.append(x)
            counter += 1
        copy_list.append(x)
    return counter

############################################################################
#
# Problem 4
# Implement insertion sort from class.
#
# Running Time: theta(n^2)
############################################################################

def insertionSort(l):
    if len(l) <= 1:
        return l
    result = []
    result.append(l[0])
    for i in range(1,len(l)):
        j = i - 1
        while j >= 0:
            if l[i] < result[j]:
                j -= 1
            else:
                break
        result.insert(j+1, l[i])
    return result

############################################################################
#
# Problem 5
# Use the heap from last homework to sort an array.
#
# Running Time: theta(nlogn)
############################################################################

def heapify(l, idx):
    left = (idx * 2) + 1
    right = (idx * 2) + 2
    smallest = idx
    if left < len(l) and l[smallest] > l[left]:
        smallest = left
    if right < len(l) and l[smallest] > l[right]:
        smallest = right
    if smallest != idx:
        l[idx], l[smallest] = l[smallest], l[idx]
        return heapify(l, smallest)

def heapSort(l):
    result = []
    for i in range(len(l)):
        heapify(l, i)
    while len(l) > 0:
        l[0], l[-1] = l[-1], l[0]
        data = l.pop(-1)
        result.append(data)
        heapify(l,0)
    l[:] = result

l = [3,1,6,5,2,4]
heapSort(l)
print(l)
l = [8,71,41,31,10,11,16,46,51,31,21,13]
heapSort(l)
print(l)