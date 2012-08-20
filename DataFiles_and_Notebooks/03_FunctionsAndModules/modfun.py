#!/usr/bin/env python
"""
Some functions written to demonstrate a bunch of concepts like modules, import
and command-line programming


 PYTHON BOOT CAMP EXAMPLE; 
    created by Josh Bloom at UC Berkeley, 2012 (ucbpythonclass+bootcamp@gmail.com)

"""

import os
import sys

def getinfo(path=".",show_version=True):
    """
Purpose: make simple us of os and sys modules

Input: path (default = "."), the directory you want to list
    """
    if show_version:
        print "-" * 40
        print "You are using Python version ",
        print sys.version
        print "-" * 40

    print "Files in the directory " + str(os.path.abspath(path)) + ":"
    for f in os.listdir(path): print "  " + f
    print "*" * 40
    
def numop1(x,y,multiplier=1.0,greetings="Thank you for your inquiry."):
    """ 
Purpose: does a simple operation on two numbers. 

Input: We expect x,y are numbers 
       multiplier is also a number (a float is preferred) and is optional.  
       It defaults to 1.0. You can also specify a small greeting as a string.

Output: return x + y times the multiplier
    """
    if greetings is not None:
          print greetings
    return (x + y)*multiplier


if __name__ == "__main__":
    """
Executed only if run from the command line.
call with
  modfun.py <dirname> <dirname> ...
If no dirname is given then list the files in the current path
    """
    if len(sys.argv) == 1:
        getinfo(".",show_version=True)
    else:
        for i,dir in enumerate(sys.argv[1:]):
            if os.path.isdir(dir):
                # if we have a directory then operate on it
                # only show the version info if it's the first directory
                getinfo(dir,show_version=(i==0))
            else:
                print "Directory: " + str(dir) + " does not exist."
                print "*" * 40
                
