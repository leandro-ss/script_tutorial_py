#! /usr/bin/env python3

# Last update: "test_polynomial.py: 2017-08-10 (Thu)  12:42:31 BRT (tk)" 

# Test program for task # 2

import os
import sys
import traceback

## This seems to be necessary when executing this program through a sym link
sys.path.insert(0,os.getcwd())

from polynomial import Polynomial

def build_poly(s):
    """ Build a polynomial from a sequence of terms. """
    pol = Polynomial()
    for k in range(0,len(s),2):
        pol.new_term([int(s[k+1]), int(s[k])])
    return pol

try:
    p1, p2 = sys.stdin.readlines()
    s1 = p1[:-1].split()
    s2 = p2[:-1].split()
    l1 = len(s1)
    l2 = len(s2)
    if (l1%2)!=0 or (l2%2)!=0:
        raise ValueError
except:
    print("Illegal input data")
    sys.exit(1)
    

try:
    pol1 = build_poly(s1)
    pol2 = build_poly(s2)
    print(pol1)
    print(pol2)
    print(pol1.add_poly(pol2))
except:
    traceback.print_exc()
    sys.exit(1)
