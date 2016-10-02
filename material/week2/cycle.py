#!/usr/bin/env python3
import random

def cycle_xover(a,b):
    child = [None]*len(a)
    while None in child:
        ind = child.index(None)
        indices = []
        values = []
        while ind not in indices:
            val = a[ind]
            indices.append(ind)
            values.append(val)
            ind = a.index(b[ind])
        for ind,val in zip(indices, values):
            child[ind] = val
        a,b = b,a
    return child

def cycle_xover_pair(a,b):
    return cycle_xover(a,b) , cycle_xover(b,a)

if __name__ == "__main__":
    a = [2,4,7,1,3,6,8,9,5]
    b = [5,9,8,6,2,4,1,3,7]
    c,d = cycle_xover_pair(a,b)
    print("Parents:")
    print(a)
    print(b)
    print("Children:")
    print(c)
    print(d)
