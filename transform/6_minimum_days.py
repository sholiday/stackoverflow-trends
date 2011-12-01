#!/usr/bin/env python
# encoding: utf-8
"""
2_convert_to_ngrams.py

Created by Stephen Holiday on 2011-11-20.
Copyright (c) 2011 Stephen Holiday. All rights reserved.
"""

import sys
import collections

def read_input(file):
    for line in file:
        line = line.strip()
        gram, dates = line.split('\t',1)
        
        yield (gram,dates.count(':'))

def main(separator='\t'):
    counts = collections.Counter()
    #data = read_input(['hey\t2011-12-1:3|2011-13-1:3'])
    data = read_input(sys.stdin)
    for gram,count in data:
        #print '%s\t%s'%(gram,count)
        counts[count]+=1
    
    i=1
    for index, count in counts.items():
        while index > i:
            print "%d,%d"%(i,0)
            i+=1
        print "%d,%d"%(index, count)
        i+=1

if __name__ == "__main__":
    main()