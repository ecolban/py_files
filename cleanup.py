#!/usr/bin/python

import os
import os.path

def empty_dir(directory):
    files = os.listdir(directory)
    for f in files:
        f = '/'.join([directory, f])
        if os.path.isdir(f):
            empty_dir(f)
            try:
                os.rmdir(f)
            except OSError:
                print('%s was not removed' % f)
        else:
            try:
                os.remove(f)
            except OSError:
                print('%s was not removed' % f)
                
            
directory = os.path.expanduser('~league')
for d in os.listdir(directory):
    d = '/'.join([directory, d])
    if os.path.isdir(d): empty_dir(d)

    
    
