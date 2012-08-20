"""
  PYTHON BOOT CAMP BREAKOUT3 SOLUTION; 
    created by Josh Bloom at UC Berkeley, 2010 (ucbpythonclass+bootcamp@gmail.com)
"""

import datetime

born = datetime.datetime(1985,9,11,0,0,0)
now  = datetime.datetime.now()     # note... .utcnow() gives the universal time, .now()
                                   #   gives the local time. We're ignoring timezone stuff here.
                                   
diff = now - born  # cool! I can subtract two dates
print diff

# 1. how many days have you been alive? How many hours? 
print "days alive:", diff.days
print "hours alive:", diff.days*24.0

# 2. What will be the date in 1000 days from now?

# let's create a timedelta object
td = datetime.timedelta(days=1000)


print "in 1000 days it will be",now + td  # this is a datetime object