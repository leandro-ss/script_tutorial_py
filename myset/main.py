#! /usr/bin/env python3
# Last update: "main.py: 2017-07-19 (Wed)  18:35:40 BRT (tk)" 
# Test main program for task # 1

import os
import sys
import traceback

## This seems to be necessary when executing this program through a sym link
sys.path.insert(0,os.getcwd())

from myset import MySet

# Dictionary of set operations. Each method is followed by a boolean
# flag which indicates whether both arguments are sets or not; first
# argument is always a set.

operations = { 
                "a":  [MySet.add, False] ,
                "r":  [MySet.remove, False] ,
                "s":  [MySet.issubset, True],
                "S":  [MySet.issuperset, True],
                "e":  [MySet.__eq__, True],
                "c":  [MySet.__contains__, False],
                "u":  [MySet.union, True],
                "i":  [MySet.intersection, True],
                "d":  [MySet.difference, True],
              }

def set_input():
    """ Read a line with set data. """
    try:
        line = sys.stdin.readline().strip()
        line = "[%s]" % line.replace(' ',',')
        return MySet(eval(line))
    except:
        traceback.print_exc()
        print("Illegal set input data")
        sys.exit(1)

def apply_op(op, i, j):
    """ Applies 'op' to args i and j """
    global s1, s2
    set_vars = [s1, s2]
    try:
        method, two_sets = operations[op]
        if two_sets:
            return method(set_vars[i-1],set_vars[j-1])
        else:
            return method(set_vars[i-1],j)
    except:
        raise
        
if __name__=="__main__":        
        
    ## Read and print set data
    s1 = set_input()
    print(s1)
    s2 = set_input()
    print(s2)

    ## Interpreting operations
    for line in sys.stdin.readlines():
        if line.strip():  ## skip blank line
            try:
                op, i, j = line.split()
                i = int(i)
                j = int(j)
                print(apply_op(op, i, j))
            except:
                traceback.print_exc()
                print("Illegal operation:", line)
    print("Done!")
