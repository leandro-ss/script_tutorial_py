#! /usr/bin/env python3

# Last update: "test_sum.py: 2017-08-23 (Wed)  16:31:41 BRT (tk)" 

# Test program for task Parentheses

import sys, os
import traceback

## This seems to be necessary when executing this program through a sym link on  SuSy
sys.path.insert(0,os.getcwd())

from sum import sum

try:
    line = sys.stdin.readline()[:-1]  ## remove '\n'
    d = eval(line)
    print(sum(d))
except:
    print("Illegal input or processing error\n")
    traceback.print_exc()
    sys.exit(0)
    
