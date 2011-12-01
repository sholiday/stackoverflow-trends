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
import collections

def read_mapper_output(file):
    for line in file:
        gram,dates = line.rstrip().split('\t', 1)
        yield (gram,dates.split('|'))

def main(separator='\t'):
    # input comes from STDIN (standard input)
    #d = ["php\t2008-09-29:96|2008-10-06:96|2008-12-12:96|2009-02-13:96|2009-03-14:96|2009-07-22:96|2009-07-26:96|2009-08-11:96|2009-09-01:96|2009-11-01:96|2010-02-08:96|2010-05-19:96|2010-06-02:96|2010-06-04:96|2010-08-08:96|2010-08-22:96|2010-09-05:96|2010-09-23:96|2010-11-12:96|2010-11-22:96|2010-12-23:96|2010-12-28:96|2011-01-02:96|2011-01-06:96|2011-01-27:96|2011-01-27:96|2011-02-01:96|2011-03-28:96|2011-04-03:96|2011-05-29:96|2011-05-29:96|2008-10-05:97|2008-10-13:97|2008-11-28:97|2009-04-21:97|2009-04-28:97|2010-05-24:97|2010-06-28:97|2010-07-07:97|2010-07-15:97|2010-11-14:97|2010-12-15:97|2010-12-29:97|2009-05-24:98|2009-07-29:98|2009-07-31:98|2009-08-28:98|2009-09-23:98|2009-12-12:98|2010-02-28:98|2010-07-11:98|2010-08-10:98|2010-09-02:98|2010-10-23:98|2010-12-18:98|2010-12-24:98|2010-12-30:98",
     #   "php\t2008-10-09:99|2009-03-26:99|2009-07-22:99|2009-10-12:99|2009-12-06:99|2009-12-21:99|2010-01-25:99|2010-06-20:99|2010-07-05:99|2010-07-20:99|2010-08-09:99|2010-10-04:99|2010-11-02:99|2010-11-04:99|2010-11-24:99|2010-12-17:99|2011-01-22:99|2011-07-31:99"]
    data = read_mapper_output(sys.stdin)#, separator=separator)
    # groupby groups multiple word-count pairs by word,
    # and creates an iterator that returns consecutive keys and their group:
    #   current_word - string containing a word (the key)
    #   group - iterator yielding all ["<current_word>", "<count>"] items
    for gram, group in groupby(data, itemgetter(0)):
        #print current_word
        counts = collections.Counter()
        for gram,dates in group:
            #print (gram,g)
            for date_count in dates:
                date, count = date_count.split(':',1)
                counts[date]+=int(count)
            
        dates = list()
        for index, count in counts.items():
            dates.append("%s:%d"%(index,count))
        
        print "%s\t%s"%(gram,"|".join(sorted(dates)))
if __name__ == "__main__":
    main()