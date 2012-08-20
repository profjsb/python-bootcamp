#!/usr/bin/env python
"""
  PYTHON BOOT CAMP BREAKOUT3 SOLUTION; 
    created by Josh Bloom at UC Berkeley, 2010 (ucbpythonclass+bootcamp@gmail.com)
"""

import datetime
import sys

def days_since_now(year,month,day):
    now  = datetime.datetime.now() 
    print "days since then...", (now - datetime.datetime(year,month,day,12,0,0)).days
    return
    
def date_from_now(ndays):
    now  = datetime.datetime.now() 
    print "date in " + str(ndays) + " days", now + datetime.timedelta(days=ndays)
    
if __name__ == "__main__":
    if len(sys.argv) == 2:
        date_from_now(int(sys.argv[1]))
    elif len(sys.argv) == 4:
        days_since_now(int(sys.argv[1]),int(sys.argv[2]),int(sys.argv[3]))
    else:
        print "dont know what to do with", repr(sys.argv[1:])
