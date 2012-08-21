"""
 randomly generate lambda functions to find one that evaluates the same as x**2 + x
    over some range around 0
  
 breakout 1 of day 2
 
  PYTHON BOOT CAMP BREAKOUT 1 (DAY 2) answer; 
    created by Josh Bloom at UC Berkeley, 2010 (ucbpythonclass+bootcamp@gmail.com)
"""


import numpy
# could use the numpy.random stuff but we'll use the builtin random module instead
import random

voc =["x","x"," ","+","-","*","/","1","2","3"]

# want to create a string like "y = lambda x: ..."
nfunc = 1000000L
maxchars = 10
eval_places = numpy.arange(-3,3,0.4)
sin_val     = eval_places**2 + eval_places
tries = []
for n in xrange(nfunc):
    ## make some random function using the vocabulary
    thefunc = "".join([voc[random.randint(0,len(voc)-1)] for x in range(random.randint(1,maxchars))])
    ## construct two python statement, declaring the lambda function and evaluating it at eval_places
    mylam = "y = lambda x: " + thefunc + "\n"
    mylam += "rez = y(eval_places)"
    try:
        ## this may be volitile so be warned!
        exec(mylam)
    except:
        continue
    try: 
        tries.append( ( (abs(rez - sin_val).sum()) ,thefunc))
        if (abs(rez - sin_val)).sum() < 0.0001:
            ## we got something really close
            break
    except:
        pass
        
    ## get rid of rez and y out of the namespace just in case rez or y 
    ## working within the next try
    del rez
    del y

## find the best results
# tries.sort()
# print tries[0]
# print tries[1]
##  ... NOTE: this turns out to be volitle because the sort method
##            on lists does not know how to deal with numpy values like -nan and inf


### but ... we can do a proper sort if we get this stuff into a numpy array
a = numpy.array(tries,dtype=[('rez','f'),("func",'|S10')])
a.sort()

if a[0]["rez"] < 0.001:
    print "took us ntries = %i, but we eventually found that '%s' is functionally equivalent to x**2 + x" % (n,a[0]["func"])
else:
    print "after ntries = %i, we found that '%s' is close to x**2 + x (metric = %.3f)" % (n,a[0]["func"],a[0]["rez"])