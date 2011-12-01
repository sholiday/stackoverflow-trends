#!/usr/bin/env python
# encoding: utf-8
"""
2_convert_to_ngrams.py

Created by Stephen Holiday on 2011-11-20.
Copyright (c) 2011 Stephen Holiday. All rights reserved.
"""

import sys
from itertools import groupby
from operator import itemgetter

def read_input(file):
    for line in file:
        date,raw = line.split('\t',2)
        
        yield (date,raw.count(',')+1)

def main(separator='\t'):
    #data = read_input(['2011-12-18\t["hey", "there", "how", "are", "you"]','2011-12-19\t["hey", "there", "how"]'])
    data = read_input(sys.stdin)
    counts = list()
    for date, group in groupby(data, itemgetter(0)):
        tot = 0
        for date, count in group:
            tot+=count
        counts.append('%s:%d'%(date,tot))
    print '|'.join(sorted(counts))

if __name__ == "__main__":
    main()