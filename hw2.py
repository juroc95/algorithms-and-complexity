
# CS 350: Homework 2
# Due: Week of 4/11
# Name: Juhwan Lee



#########################################3
# Problem 1:
#
# Find a pair with a given sum.
#
# input: a list of integers l, an integer s
# return None if this sum doesn't exist in the array.
# output: a pair of numbers (a,b) where a,b are in l, and a + b == s
# findSum([1,3,5], 8) returns (3, 5)
# 
# What data structure did you use? array
# Running Time: theta(n^2)
#########################################3

def findSum(l, s):
    """
    >>> findSum([1,3,5], 8)
    (3, 5)
    >>> findSum([1,2,5], 8)
    None
    """
    result = []
    for i in range(len(l) - 1):
        for j in range(i+1, len(l)):
            if l[i] + l[j] == s:
                result = (l[i], l[j])
                return result
    print(None)

#########################################3
# Problem 2:
#
# Find the mode of a list of numbers.
# The mode of a list is the most commonly occurring number in the list.
#
# input: a list of integers l
# output: the mode of l.
# mode([1,2,3,3,4,5]) returns 3
# 
# What data structure did you use? array
# Running Time: theta(n^2)
#########################################3

def mode(l):
    """
    >>> mode([1,2,3,3,4,5])
    3
    """
    mode = l[0]
    mode_counter = 0
    max = 0
    for i in range(len(l)):
        for j in range(len(l)):
            if i == j:
                continue
            if l[i] == l[j]:
                mode_counter += 1
        if max < mode_counter:
            max = mode_counter
            mode = l[i]
    return mode

#########################################3
# Problem 3:
#
# We talked about a ring buffer in class
# A ring buffer has four methods
# pushFront(x)
# pushBack(x)
# popFront()
# popBack()
#
# Your job is to implement these four methods.
# We can't just use the list append method to resize the ring buffer.
# we might have front and back in the middle of the buffer,
# and append only adds new space at the end.
# for that reason, you're going to have to copy
# the array over to a bigger one manually.
#
# I've provided a malloc function to allocate a new array.
# You need to copy the old array into the new one
# but be sure to keep elements in the correct position
#
# For example if we have the buffer :
#
#     v back
# [3, 4, 1, 2]
#        ^ front
#
# and we were to resize it, then the new buffer should be
#     v back
# [3, 4, None, None, None, None, 1, 2]
#                                ^ front
#    
# pushFront Running Time: theta(n)
# pushBack Running Time: theta(n)
# popFront Running Time: theta(1)
# popBack Running Time: theta(1)
#########################################3

def malloc(size):
    return [None] * size

class RingBuffer():
    """
    >>> r = RingBuffer()
    >>> r.pushBack(3)
    >>> r.pushBack(4)
    >>> r.pushBack(5)
    >>> r.pushFront(2)
    >>> r.pushFront(1)
    >>> r.popFront()
    1
    >>> r.popFront()
    2
    >>> r.popFront()
    3
    >>> r.popFront()
    4
    >>> r.popFront()
    5
    """

    def __init__(self):
        self.size = 0
        self.body = []
        self.front = 0
        self.back = 0

    # This method isn't mandatory,
    # but I suggest you implement it anyway.
    # It will help to test this method on it's own.
    # Think carefully about what cases you can have with front and back.
    def reSize(self):
        pass

    def pushFront(self, x):
        self.size += 1
        if self.size > len(self.body):
            temp = malloc(len(self.body) + 10)
            for i in range(len(self.body)):
                if i <= self.back:
                    temp[i] = self.body[i]
                else:
                    break
            for i in range(-1, -len(self.body)):
                if i >= self.front:
                    temp[i] = self.body[i]
                else:
                    break
            self.body = temp
        i = 0
        while i != -len(self.body):
            if self.body[i] != None:
                i -= 1
            else :
                self.body[i] = x
                self.front = i
                break
        return

    def pushBack(self, x):
        self.size += 1
        if self.size > len(self.body):
            temp = malloc(len(self.body) + 10)
            for i in range(len(self.body)):
                if i <= self.back:
                    temp[i] = self.body[i]
                else:
                    break
            for i in range(-1, -len(self.body)):
                if i >= self.front:
                    temp[i] = self.body[i]
                else:
                    break
            self.body = temp
        i = 0
        while i != len(self.body):
            if self.body[i] != None:
                i += 1
            else :
                self.body[i] = x
                self.back = i
                break
        return


    def popFront(self):
        x = self.body[self.front]
        self.body[self.front] = None
        self.front += 1
        self.size -= 1
        return x

    def popBack(self):
        x = self.body[self.back]
        self.body[self.back] = None
        self.back -= 1
        self.size -= 1
        return x

#########################################3
# Problem 4:
#
# We talked about a heap in class
# A heap is a data structure that has a constructor,
# a push method, and a pop method.
# Your job is to implement these methods in Python.
# I've given you the skeleton for the class,
# you need to fill it in.
# 
# 
# push Running Time: theta(logn)
# pop Running Time: theta(logn)
#########################################3

class Heap():
    """
    >>> h = Heap()
    >>> h.push(3)
    >>> h.push(2)
    >>> h.push(4)
    >>> h.push(1)
    >>> h.push(5)
    >>> h.pop()
    1
    >>> h.pop()
    2
    >>> h.pop()
    3
    >>> h.pop()
    4
    >>> h.pop()
    5
    """
    def __init__(self):
        self.data = [None]

    def push(self, x):
        self.data.append(x)
        i = len(self.data) - 1
        while i > 1:
            if self.data[i] < self.data[(i // 2)]:
                self.data[i], self.data[(i // 2)] = self.data[(i // 2)], self.data[i]
                i = i // 2
            else:
                break        

    def pop(self):
        if len(self.data) > 1:
            self.data[1], self.data[-1] = self.data[-1], self.data[1]
            data = self.data.pop(-1)
            flag = 1
            i = 1
            while flag == 1:
                left = 2 * i
                right = (2 * i) + 1
                root = i
                if left < len(self.data) and self.data[i] > self.data[left]:
                    root = left
                if right < len(self.data) and self.data[i] < self.data[right]:
                    root = right
                if root != i:
                    self.data[i], self.data[root] = self.data[root], self.data[i]
                    flag = 1
                    i = root
                else:
                    flag = 0
        else:
            data = None
        return data

if __name__ == "__main__":
    import doctest
    doctest.testmod()
