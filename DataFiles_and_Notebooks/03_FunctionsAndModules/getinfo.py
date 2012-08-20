"""
this is a demo of some methods used in the os and sys.
usage:
  import getinfo
  getinfo.getinfo()
  getinfo.getinfo("/tmp/")
  
 PYTHON BOOT CAMP EXAMPLE; 
   created by Josh Bloom at UC Berkeley, 2012 (ucbpythonclass+bootcamp@gmail.com)

"""
import os
import sys

def getinfo(path="."):
    """
Purpose: make simple use of os and sys modules
Input: path (default = "."), the directory you want to list
    """
    print "You are using Python version ",
    print sys.version
    print "-" * 40
    print "Files in the directory " + str(os.path.abspath(path)) + ":"
    for f in os.listdir(path): print f
