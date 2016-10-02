#!/usr/bin/env python3
import random

def order_xover(a,b, start, stop):
    child = [None]*len(a)

    # Copy a slice from first parent:
    child[start:stop] = a[start:stop]

    # Fill using order from second parent:
    b_ind = stop
    c_ind = stop
    l = len(a)
    while None in child:
        if b[b_ind % l] not in child:
            child[c_ind % l] = b[b_ind % l]
            c_ind += 1
        b_ind += 1
    return child

def order_xover_pair(a,b):
    half = len(a) // 2
    start = random.randint(0, len(a)-half)
    stop = start + half
    return order_xover(a,b,start,stop) , order_xover(b,a,start,stop)

if __name__ == "__main__":
    a = [2,4,7,1,3,6,8,9,5]
    b = [5,9,8,6,2,4,1,3,7]
    c,d = order_xover_pair(a,b)
    print("Parents:")
    print(a)
    print(b)
    print("Children:")
    print(c)
    print(d)
