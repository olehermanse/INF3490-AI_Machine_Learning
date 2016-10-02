#!/usr/bin/env python3
import random

def pmx(a,b, start, stop):
    child = [None]*len(a)

    # Copy a slice from first parent:
    child[start:stop] = a[start:stop]

    # Map the same slice in parent b to child using indices from parent a:
    for ind,x in enumerate(b[start:stop]):
        ind += start
        if x not in child:
            while child[ind] != None:
                ind = b.index(a[ind])
            child[ind] = x

    # Copy over the rest from parent b
    for ind,x in enumerate(child):
        if x == None:
            child[ind] = b[ind]

    return child

def pmx_pair(a,b):
    half = len(a) // 2
    start = random.randint(0, len(a)-half)
    stop = start + half
    return pmx(a,b,start,stop) , pmx(b,a,start,stop)

if __name__ == "__main__":
    a = [2,4,7,1,3,6,8,9,5]
    b = [5,9,8,6,2,4,1,3,7]
    c,d = pmx_pair(a,b)
    print("Parents:")
    print(a)
    print(b)
    print("Children:")
    print(c)
    print(d)
