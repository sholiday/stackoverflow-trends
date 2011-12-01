#!/usr/bin/env python
# encoding: utf-8
"""
1_parse_to_ngrams.py

Created by Stephen Holiday on 2011-11-16.
Copyright (c) 2011 Stephen Holiday. All rights reserved.
"""

import sys
import os
import re
#import nltk
import xml.parsers.expat
import iso8601
import time
import hashlib
import json
import random
from datetime import datetime
import cjson

def safe_unicode(obj): # Converts a string easily
    try:
        return str(obj)
    except UnicodeEncodeError:
        # obj is unicode
        return unicode(obj).encode('utf-8')

def string_to_token_list(string,stopwords=False):
    string=string.lower()

    tokens_raw = re.findall('[a-zA-Z0-9\-\'\`\+]+',string)

    #lowercase them
    words=map(lambda x: safe_unicode(x.lower()),tokens_raw)

    #if we want to remove the stop words...
    tokens=list()
    if stopwords:
        stop_words = nltk.corpus.stopwords.words('english')
        for word in words:
            if not word in stop_words:
                tokens.append(word)
    else:
        tokens=words
    return tokens

def ngrams(s=None,token_list=None,n=2):
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

def remove_tags(data):
    p = re.compile(r'<.*?>')
    return p.sub('', data)

def main():
    def store_tokens(token_dict,date):
        for token in token_dict:
            print '%s\t%s\%s'%(date,token,token_dict[token])

    def start_element(name, attrs):
        if name!='posts':
            #print remove_html_tags(attrs['Body'])
            #print int(time.mktime(().timetuple())))
            date=iso8601.parse_date(attrs['CreationDate']).strftime("%Y-%m-%d")
            #print date


            #token_dict=mkgram.mkgram.token_list_to_dict(mkgram.mkgram.string_to_token_list(mkgram.stringCleaner.remove_tags(attrs['Body']),False))
            #store_tokens(token_dict,date)
            
            print '%s\t%s'%(date,cjson.encode(string_to_token_list(remove_tags(attrs['Body']))))
            
            ## now do something with the tokens
            #for token in token_dict:
            #    if not token in tokens:
            #        tokens[token]=dict()
            #    
            #    if not date in tokens[token]:
            #        tokens[token][date]=token_dict[token]
            #    else:
            #        tokens[token][date]+=token_dict[token]


    def end_element(name):
        print 'End element:', name
    def char_data(data):
        print 'Character data:', repr(data)

    p = xml.parsers.expat.ParserCreate()

    p.StartElementHandler = start_element
    #p.EndElementHandler = end_element
    #p.CharacterDataHandler = char_data

    p.ParseFile(open('posts.xml'))

    p.close()


if __name__ == '__main__':
    main()