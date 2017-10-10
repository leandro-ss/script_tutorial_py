#! /usr/bin/env python3

# Last update: "test_trie.py: 2017-10-06 (Fri)  13:52:11 BRT (tk)" 

# Test program for task Tries

import sys, os
import traceback

## This seems to be necessary when executing this program through a sym link on  SuSy
sys.path.insert(0,os.getcwd())

from trie import Trie

# Input from stdin two lists of integers

try:
    
    tr = Trie()  ## empty trie
    
    for line in sys.stdin.readlines():
        op = line[0]
        word = line[1:-1].strip() ## remove first and last (\n)
        if op=='*':
            print()
            print("%d words" % len(tr))
            print("%d letters" % tr.num_letters())
            print("%d nodes" % tr.num_nodes())
            print()
            continue
        if  not word:
            continue  # skip blank word
        print("%-12s:" % word, end=" ")
        if line[0]=="+":
            res = tr.insert(word)
            print("inserted" if res else "repeated")
        elif line[0]=="-":
            res = tr.delete(word)
            print("removed" if res else "not found")
        else:
            print("illegal data")
            
except:
    print("Unexpected exception")
    traceback.print_exc()
    
