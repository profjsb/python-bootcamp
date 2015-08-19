#!/usr/bin/env python

# This demonstrates how to write a simple command line tool using the very
# clever "docopt" library:
#
#   http://docopt.org/
#
# You need to have installed 'docopt' to run this command.
# Try:
#   conda install docopt
# Or if that doesn't work, try:
#   pip install docopt
#
# There are also other libraries for writing command line tools in
# Python. E.g., the "argparse" library is included with Python by default (no
# need to install anything extra):
#   https://docs.python.org/3/library/argparse.html

"""
Usage:
  age1-docopt.py days-since YEAR MONTH DAY
  age1-docopt.py days-from-now DAYS
  age1-docopt.py -h | --help | --version

Options:
  -h --help      Show this screen.
  --version      Show version.

"""

import datetime

from docopt import docopt

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
    arguments = docopt(__doc__, version="1.0")
    if arguments["days-since"]:
        print(days_since(int(arguments["YEAR"]),
                         int(arguments["MONTH"]),
                         int(arguments["DAY"])))
    elif arguments["days-from-now"]:
        print(days_from_now(int(arguments["DAYS"])))
    else:
        # It should be impossible to get here:
        print("....huh?")
