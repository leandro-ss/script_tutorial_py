#! /usr/bin/env python3

# Last update: "test_counts.py: 2017-09-21 (Thu)  12:42:09 BRT (tk)" 

# Test program for task Counts

import sys, os
import traceback
from random import seed, randint

## This seems to be necessary when executing this program through a sym link on  SuSy
sys.path.insert(0,os.getcwd())

from counts import counts ## import submitted solution
from bintree import BinTree



class Pair:
    """ Auxiliary class to build pairs of numbers, where the first number
    will be used as a key in comparisons.
    """
    def __init__(self, v1, v2):
        self.v1 = v1
        self.v2 = v2
        
    def __lt__(self, other):
        return self.v1<other.v1
        
def clean_tree(t):
    """ Will return a new tree without keys. """
    if t is None:
        return None
    return  BinTree(t.data.v2, left=clean_tree(t.left), right=clean_tree(t.right))


try:

    data = sys.stdin.readline()[:-1].split()  ## remove '\n' and split values
    N, minv, maxv = int(data[0]), int(data[1]), int(data[2]) 
    
    ## Generate a random tree with N nodes
    if N==0:
        tree = None
    else:
        seed(207133107) # generates always the same sequence
        first = True
        for k in range(N):
            pair = Pair(randint(minv, maxv), randint(minv, maxv)) ## pair to be inserted
            if first:
                tree = BinTree(pair)
                first = False
            else:
                tree.insert(pair)
                
    tree = clean_tree(tree) ## remove keys

    ## Draw if a small tree (N<=10)
    if 1<N<=10:
        tree.draw()
        print()
        
    count_neg, count_nul, count_pos = counts(tree)
    
    print("Tree with %d nodes\n" % N)
    print("    %3d negative value(s)" % count_neg)
    print("    %3d null value(s)" % count_nul)
    print("    %3d positive value(s)" % count_pos)
    print()
    
except:
    print("Illegal input or processing error\n")
    traceback.print_exc()
    sys.exit(0)
    
