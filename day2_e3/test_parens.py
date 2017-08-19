#! /usr/bin/env python3

# Last update: "test_parens.py: 2017-08-17 (Thu)  11:53:59 BRT (tk)" 

# Test program for task Parentheses

import sys, os
import traceback

## This seems to be necessary when executing this program through a sym link on  SuSy
sys.path.insert(0,os.getcwd())

from parens import parens

## Process line by line

try:

    for line in sys.stdin.readlines():
        k = line.find('#')       ##  finds # or -1 (\n)
        ls = line[:k].strip()    ##  strips initial and final blanks
        print(ls, end=": ")
        if parens(ls):
            print("balanced")
        else:
            print("unbalanced")
    
except IndexError:

    print("unbalanced")  ## tried to pop empty stack

except:    ## any other error
    
    print("Illegal input or processing error\n")
    traceback.print_exc()
    sys.exit(0)


