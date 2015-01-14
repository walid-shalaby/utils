# -*- coding: utf-8 -*-
"""
Created on Tue Jan 13 20:07:18 2015

@author: walid-shalaby
"""

"""
Download a list of urls and store them to disk.

Parameters
-----------
--urls: optional, a tuples target urls to download. Each one must be enclosed in "()". 
        Can't be used with '--urls_file'
--urls-file: path to a file containing target urls each in a separate line. Can't be used with 
             '--urls'
--output-dir: path to an existing directory where downloaded urls are stored

"""

def get_it(url, output_dir):
    '''download given url to output directory'''
    from urllib2 import urlopen

    output_file = os.path.join(output_dir, url[url.rfind('/')+1:])
    print 'Downloading: {0}'.format(url)
    open(output_file, "wb").write(urlopen(url).read())
    
import argparse
import os
import re

def downloader(urls, output_dir):
    # loop on urls
    for url in urls:
        get_it(url, output_dir)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('--urls', help=''' optional, a tuples target urls to download. Each one must 
                                          be enclosed in "()". Can't be used with '--urls_file' ''')
    group.add_argument('--urls_file', help=''' path to a file containing target urls each in 
                                                 a separate line. Can't be used with '--urls' ''')
                                                 
    parser.add_argument('--output_dir', help=''' path to an existing directory where downloaded 
                                                 urls are stored ''', required=True)
    # parse command line 
    args = parser.parse_args()

    # make sure output directory is there'''
    if os.path.exists(args.output_dir):        
        urls = []
        if not args.urls == None: # urls in command line
            # loop on urls
            matches = re.findall('\(([^\)]+)+',args.urls)
            for m in matches:
                urls.append(m)
        else: # urls in file
           f = open(args.urls_file, 'r')
           for line in f:
               urls.append(line)
               
        downloader(urls, args.output_dir)
    else:
        print 'Output path does not exist. Please provide existing one'
        