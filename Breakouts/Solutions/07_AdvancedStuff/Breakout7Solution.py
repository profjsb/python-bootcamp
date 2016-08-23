
# coding: utf-8

# In[ ]:

import numpy as np
from random import randint
from numpy.random import choice


# In[ ]:

# Define our parameters of interest
max_try = 100000
voc = ["x", "x", " ", "+", "-", "*", "/", "1", "2", "3"]
max_chars = 10

x_array = np.arange(-3,3,0.4)
real_function = lambda x: x**2 + x
y_real = real_function(x_array)


# In[ ]:

tries = []
funcs = []
for n in range(max_try):
    ## make some random function using the vocabulary
    thefunc = "".join(choice(voc, randint(1,max_chars)))
    
    ## construct two python statement, declaring the lambda function and evaluating it at X
    mylam = "y = lambda x: " + thefunc + '\n'
    mylam += 'rez = y(x_array)'
    funcs.append(thefunc)
    try:
        ## this may be volitile so be warned!
        ## Couch everything in error statements, and
        ##  simply throw away functions that aren't reasonable
        exec(mylam)
    except (SyntaxError, NameError):
        continue
    except OverflowError:
        print("I couldn't even finish, the number was too big...")
        continue
        
    try:
        err = abs(rez - y_real).sum() 
    except OverflowError:
        print('Whoah, chill out dude.\nYour number was: {0}\nYour func was: {1}\n'.              format(rez, thefunc))
        err = np.inf
    tries.append( ( err ,thefunc))
    if (err < 0.0001):
        ## we got something really close
        break
    del rez
    del y

### numpy arrays handle NaN and INF gracefully, so we put
### answer into an array before sorting
a = np.array(tries, dtype=[('rez','f'), ("func",'|S10')])
a.sort()

if a[0]["rez"] < 0.001:
    print("took us ntries = {0}, but we eventually found that '{1}' is functionally equivalent to f(X)".format(n,a[0]["func"]))
else:
    print("after ntries = {0}, we found that '{1}' is close to f(x) (metric = {2})".format(n,a[0]["func"],a[0]["rez"]))


# In[ ]:

for err, func in a:
    print('Error: {0} | Function: {1}'.format(err, func))


# In[ ]:



