import numpy as np
from random import randint

def generate_function(X,Y, voc, max_try=1000000, max_chars=10):
    ''' find the analytic form that describes Y on X '''
    tries = []
    for n in xrange(max_try):
        ## make some random function using the vocabulary
        thefunc = "".join([voc[randint(0,len(voc)-1)] for x in range(randint(1,max_chars))])
        ## construct two python statement, declaring the lambda function and evaluating it at eval_places
        mylam = "y = lambda x: " + thefunc + "\n"
        mylam += "rez = y(X)"
        try:
            ## this may be volitile so be warned!
            ## Couch everything in error statements, and
            ##  simply throw away functions that aren't reasonable
            exec(mylam)
        except:
            continue
        try: 
            tries.append( ( (abs(rez - Y).sum()) ,thefunc))
            if (abs(rez - Y)).sum() < 0.0001:
                ## we got something really close
                break
        except:
            pass
        del rez
        del y
        
    ### numpy arrays handle NaN and INF gracefully, so we put
    ### answer into an array before sorting
    a = np.array(tries,dtype=[('rez','f'),("func",'|S10')])
    a.sort()
    
    if a[0]["rez"] < 0.001:
        print "took us ntries = {0}, but we eventually found that '{1}' is functionally equivalent to f(X)".format(n,a[0]["func"])
    else:
        print "after ntries = {0}, we found that '{1}' is close to f(x) (metric = {:.3f})".format(n,a[0]["func"],a[0]["rez"])
    
    return a[0]
    
    
    

voc = ["x","x"," ","+","-","*","/","1","2","3"]

x_array       = np.arange(-3,3,0.4)
real_function = x_array**2 + x_array
generate_function(x_array, real_function, voc)
