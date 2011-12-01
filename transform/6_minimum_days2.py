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
        if dates.count(':') > 15:            
            yield line

def main(separator='\t'):
    #d = ["' '''''\t2010-04-21:1","' ''''''\t2009-03-20:1|2009-06-23:1|2011-03-12:1","' '''''''''\t2009-06-11:1|2009-06-23:1|2010-04-08:1|2010-10-18:2"]

    #data = read_input(['2011-12-18\t["hey", "there", "how", "are", "you"]','2011-12-18\t["hey", "there", "how"]'])
    data = read_input(sys.stdin)
    for line in data:
        print line

if __name__ == "__main__":
    main()