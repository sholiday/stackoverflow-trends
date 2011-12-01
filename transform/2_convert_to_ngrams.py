#!/usr/bin/env python
# encoding: utf-8
"""
2_convert_to_ngrams.py

Created by Stephen Holiday on 2011-11-20.
Copyright (c) 2011 Stephen Holiday. All rights reserved.
"""

import sys
import cjson

def ngrams(token_list,n=2):
    tokens=dict()
    
    for i in xrange(len(token_list)-n+1):
        token=list()
        for j in range(i,i+n):
            token.append(token_list[j])
        token=' '.join(token)
        
        if not tokens.has_key(token):
            tokens[token]=1
        else:
            tokens[token]+=1
    
    return tokens

def read_input(file):
    for line in file:
        date,raw = line.split('\t',2)
        token_list = cjson.decode(raw)
        grams = ngrams(token_list,1)
        #grams.update(ngrams(token_list,2))
        #grams.update(ngrams(token_list,3))
        #grams.update(ngrams(token_list,4))
        #grams.update(ngrams(token_list,5))
        
        for k,v in grams.items():
            #print '%s %s'%(k,v)
            yield (date,k,v)

def main(separator='\t'):
    #data = read_input(['2011-12-18\t["hey", "there", "how", "are", "you"]','2011-12-18\t["hey", "there", "how"]'])
    data = read_input(sys.stdin)
    for date,gram,count in data:
        print '%s\t%s\t%s'%(date,gram,count)

if __name__ == "__main__":
    main()