#! /usr/bin/env python3

# Last update: "test_diff.py: 2017-08-12 (Sat)  14:11:59 BRT (tk)" 

# Test program for task Diff

import sys, os
import traceback

## This seems to be necessary when executing this program through a sym link on  SuSy
sys.path.insert(0,os.getcwd())

from diff import diff

# Input from stdin two lists of integers

try:

    in_1 = [ int(x) for x in sys.stdin.readline().split() ]
    in_2 = [ int(x) for x in sys.stdin.readline().split() ]
    d1, d2 = diff(in_1, in_2)
    print("d1:", d1)
    print("d2:", d2)
    
except:  ## any error
    
    print("Illegal input or processing error\n")
    traceback.print_exc()
    sys.exit(0)


