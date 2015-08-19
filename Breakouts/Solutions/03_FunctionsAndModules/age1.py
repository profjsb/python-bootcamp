#!/usr/bin/env python
"""
  PYTHON BOOT CAMP BREAKOUT3 SOLUTION
"""

import datetime
import sys

def days_from_now(ndays):
  """Returns the date ndays from now"""
  now = datetime.datetime.now()
  new = now + datetime.timedelta(int(ndays))
  return "in " + str(ndays) + " days the date+time will be : " + str(new)

def days_since(year, month, day):
  """Returns a string reporting the number of days since some time"""
  now = datetime.datetime.now()
  then = datetime.datetime(year, month, day)
  diff = now - then
  return "days since then . . . " + str(diff.days)

if __name__ == "__main__":
  """
  Executed only if run from the command line.
  call with
  age1.py <year> <month> <day>
  to list the days since that date

  or

  age1.py <days>
  to list the dat in some number of days

  NOTE: if you're ever writing a little command line utility like this for
  real, then you should consider using a helper library to take care of the
  boring parts. Python has a number of fancy tools for this. One that's
  built-in to the standard library is 'argparse':

    https://docs.python.org/3/library/argparse.html

  or a nice one that you can install from PyPI is 'docopt':

    http://docopt.org/
  """
  if len(sys.argv) == 2 :
    result = days_from_now(int(sys.argv[1]))
  elif len(sys.argv) == 4 :
    year = int(sys.argv[1])
    month = int(sys.argv[2])
    day = int(sys.argv[3])
    result = days_since(year, month, day)
  else :
    result = "Error : don't know what to do with "+repr(sys.argv[1:])

  print(result)
