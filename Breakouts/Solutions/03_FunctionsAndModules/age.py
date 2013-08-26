#!/usr/bin/env python
"""
  PYTHON BOOT CAMP BREAKOUT3 SOLUTION;
      created by Josh Bloom at UC Berkeley, 2010
      (ucbpythonclass+bootcamp@gmail.com)
      modified by Katy Huff at UC Berkeley, 2013
"""

# First, we want to import datetime, which is a python module for dates
# and times and such.
import datetime

# Next, we want to use datetime.datetime() to create a variable representing 
# when John Cleese was born.
# Note that utcnow() gives the universal time, while .now() gives the
# local time. We're ignoring timezone stuff here.
born = datetime.datetime(1939, 10, 27)

# Then use datetime.datetime.now() to create a variable representing now.
now = datetime.datetime.now()

# Next, subtract the two, forming a new variable, which will be a
# datetime.timedelta() object.
cleese_age = now - born

# Finally, print that variable.
print cleese_age

# Grab just the days :
print "days John Cleese has been alive : ", cleese_age.days

# There is no hours data member, so let's multiply to find the hours :
print "hours John Cleese has been alive : ", cleese_age.days * 24

# What will be the date in 1000 days from now?
td = datetime.timedelta(days=1000)

# Print it.
print "in 1000 days it will be ", now + td  # this is a datetime object
