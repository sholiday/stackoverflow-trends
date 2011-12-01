#!/usr/bin/env python
# encoding: utf-8
"""
3_reduce_ngrams.py

Created by Stephen Holiday on 2011-11-21.
Copyright (c) 2011 Stephen Holiday. All rights reserved.
"""

from itertools import groupby
from operator import itemgetter
import sys

def read_mapper_output(file):
    for line in file:
        date,gram,count = line.rstrip().split('\t', 2)
        yield (gram,(date,count))

def main(separator='\t'):
    # input comes from STDIN (standard input)
    #d = ["2011-08-31\tziparchive\t3", "2011-08-29\tziparchive\t3","2011-08-27\tziparchive\t3", "2011-08-31\tcreates\t1", "2011-08-31\tthe\t6", "2011-08-31\tthe\t2"]
    data = read_mapper_output(sys.stdin)#, separator=separator)
    # groupby groups multiple word-count pairs by word,
    # and creates an iterator that returns consecutive keys and their group:
    #   current_word - string containing a word (the key)
    #   group - iterator yielding all ["<current_word>", "<count>"] items
    for current_word, group in groupby(data, itemgetter(0)):
        #print current_word
        counts = list()
        for gram, date_count in group:
            counts.append('%s:%s'%(date_count[0],date_count[1]))
            
        print '%s\t%s'%(current_word,"|".join(counts))

if __name__ == "__main__":
    main()