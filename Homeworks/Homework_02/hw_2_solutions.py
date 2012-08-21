#!/usr/bin/env python
"""
A small monte carlo code to simulate the growth of coins in a cookie jar over a 1 year period
  
  The following are assumed:
  1) you make X purchases each day with petty cash, starting out with only bills in your pocket (i.e., no change).
  2) Each purchase has a random chance of costing some dollar amount plus YY cents (where YY goes from 0-99). 
     You always get change in the smallest number of coins possible. For instance, 
      if you have a purchase of $2.34, then you assume you acquire 66 cents in change
       (2 quarters, 1 dime, 1 nickel, 1 penny). 
  3) If you have enough change to cover the YY cents of the current transaction, you use it. 
     Otherwise, you accumulate more change. For example, if you have $1.02 in loose change, 
     and you have a purchase of $10.34, then you use 34 cents (or as close to it as possible) in coins
     leaving you with 68 cents.
  4) At the end of each day you dump all your coins collected for the day in a Money Jar.

  PYTHON BOOT CAMP HOMEWORK2 SOLUTION; 
    created by Josh Bloom at UC Berkeley, 2010 (ucbpythonclass+bootcamp@gmail.com)


TO RUN:

from command line:
>> python hw_2_solutions.py

from within python, from the folder in which this file resides:
>> from hw_2_solutions import CookieJar, answer_homework_questions
>> answer_homework_questions()

"""


import random, math
import numpy

__version__ = "0.1"
__author__  = "J. Bloom (jbloom@astro.berkeley.edu)"

# define a global dictionary for values of the coins
val = {"nickels": 0.05, "quarters": 0.25, "dimes": 0.10, "pennies": 0.01}

class CookieJar:
    """
    the basic workhorse
    """
    ## set the contents upon create to nothing
    deplete_quarters_frequency=7 # remove quarters every 1 week
    num_quarters_to_deplete=8    # how many quarters to remove
    
    def __init__(self,transactions_per_day=8,number_of_days_until_fill=365,deplete_quarters=False,\
                print_summary_every_week=False,print_summary_of_every_transaction=False):
        
        self.contents = {"quarters": 0, "dimes": 0, "nickels": 0, "pennies": 0}
        self.final_value    = self._content_value(self.contents)
        self.final_contents = self.contents
        self.num_transactions_performed = 0
        self.day = 0
        self.days_to_reach_500_pennies = -1
        
        self.print_summary_of_every_transaction = print_summary_of_every_transaction
        self.print_summary_every_week = print_summary_every_week
        self.transactions_per_day = transactions_per_day
        self.number_of_days_until_fill=number_of_days_until_fill
        self.deplete_quarters = deplete_quarters
        
    def fill_er_up(self):
        """
        the main engine, it runs all the transactions and accumulates some final results for this cookie jar
        """
        while self.day < self.number_of_days_until_fill:
            if self.print_summary_every_week:
                print "Day %i" % (self.day + 1)
            self.perform_a_days_worth_of_transactions()
            self.day += 1
            if self.contents["pennies"] > 500 and self.days_to_reach_500_pennies == -1:
                self.days_to_reach_500_pennies = self.day
            if self.day % self.deplete_quarters_frequency == 0 and self.deplete_quarters:
                self.contents["quarters"] = max(0,self.contents["quarters"] - self.num_quarters_to_deplete)
       
        #print "all done after %i transactions" % self.num_transactions_performed
        self.final_value    = self._content_value(self.contents)
        self.final_contents = self.contents
        self.final_order    = self._order(self.contents)
        
    def __str__(self):
        """
        print a summary of yourself
        """
        a = "Value %.2f after %i transactions performed." % (self.final_value,self.num_transactions_performed)
        a += "  days to reach 500 pennies: %i" % self.days_to_reach_500_pennies
        return a
    
    def _order(self,purse):
        """
        determine the ordering of number of coins in the purse.
        here the purse is assumed to be a dict like 
           {"nickels": 0, "quarters": 12, "dimes": 3, "pennies": 32}
        returns
           {1: "pennies", 2: "quarters", 3: "dimes", 4: "nickels"}   
        """
        tmp = [(v,k) for k,v in purse.iteritems()]
        tmp.sort(reverse=True)
        return dict([(i+1,tmp[i][1]) for i in range(len(tmp))])
        
    def _content_value(self,purse):
        """
        determine the value of coins in the purse.
        here the purse is assumed to be a dict like 
           {"nickels": 0, "quarters": 12, "dimes": 3, "pennies": 32}
        """
        rez = 0.0
        for k in purse.keys():
            rez += val[k]*purse[k]
        return rez
    
    def best_change(self,cost,contents,verbose=False):
        """
        for given transaction cost determines the best combination of coins that
         gives as close to the exact change amount needed as possible given the contents of a purse
         
         returns a tuple where the first element is False if the contents of the purse cannot
          cover the change cost, True if it can
          
          the second element is a dict showing how much of each coin type is required to make the transaction
           as close to $x.00 as possible
         
         This is just a big ugly 4x nested for loop, trying out all combinations
          
        """
        cost_in_cents = cost % 1.0
        if cost_in_cents > self._content_value(contents):
            # there's no way we have enough...our purse value is less than the cost in cents 
            return (False,{})
        
        exact = False
        best_diff = 1.00
        best = {}
        for q in range(contents["quarters"] + 1):
            for d in range(contents["dimes"] + 1):
                for n in range(contents["nickels"] + 1):
                    for p in range(contents["pennies"] + 1):
                        v = round(q*0.25 + d*0.10 + n*0.05 + p*0.01,2)
                        if verbose:
                            print "val",p,n,d,q,v,cost_in_cents,best_diff
                        if abs(v - cost_in_cents) < 0.005:
                            ## this is within the tolerance of a floating point difference
                            best_diff = 0.0 
                            best      = {"nickels": n, "dimes": d, "pennies": p, "quarters": q}
                            exact     = True
                            break
                        elif (v - cost_in_cents) > 0.0 and (v - cost_in_cents) < best_diff:
                            best_diff = (v - cost_in_cents)
                            best      = {"nickels": n, "dimes": d, "pennies": p, "quarters": q}
                            exact     = False
                    if exact:
                        break
                if exact:
                    break
            if exact:
                break
        return (True,best)
                        
    def perform_a_days_worth_of_transactions(self):
        """
        loop over all the transactions in the day keeping track of the number of coins of each type
         in the purse.
         The random cost of a transaction is set to be:
            cost = round(random.random()*50,2)
            
         
        """
        #initialize how much booty we have in our pockets
        pocket_contents = {"nickels": 0, "quarters": 0, "dimes": 0, "pennies": 0}
        n_exact = 0
        for i in xrange(self.transactions_per_day):
            
            cost = round(random.random()*50,2)   # assume a transaction cost of $0 - $50
                                                 # round to the nearest cent
            
            if self.print_summary_of_every_transaction:
                print "Day %i, transaction %i" % (self.day + 1,i + 1)
                print "  pocket_contents = %s" % repr(pocket_contents)
                print "  cost = $%.2f" % cost
            
            ## do I have exact change?
            got_enough = self.best_change(cost,pocket_contents)            
            if got_enough[0]:
                ## we have enough change and it might just enough to get us where we need to be
                ## That is the cost + this change ends in .00. So, subtract the value to the cost
                cost -= sum([got_enough[1][x]*val[x] for x in val.keys()])
                
                ## now remove all that from our purse
                for k,v in got_enough[1].iteritems():
                    pocket_contents[k] -= v
            
            # print "...new cost", cost
            if cost % 1.0 == 0.0:
                n_exact += 1
            change = self.calc_change(cost)
            for k,v in change.iteritems():
                if v != 0:
                    pocket_contents[k] += v
            self.num_transactions_performed += 1
            
        if self.print_summary_of_every_transaction:
            print "  end the end of the day: pocket_contents = %s" % repr(pocket_contents)
            print "      we had %i exact change times out of %i transactions" % (n_exact,self.transactions_per_day)
        
        ## dump what we have into the cookie jar at the end of the day
        for k in self.contents.keys():
            self.contents[k] += pocket_contents[k]
                
    def calc_change(self,transaction_amount):
        """
        for a given transaction amount, determines how many coins of each type to return
        """
        change          = 1.0 - (transaction_amount % 1.0)  # make this a number from 0.0 - 0.99
        change_in_cents = int(round(change*100.0) % 100)        ## make from 0 - 99 as type int
        
        #print "change",change,"change_in_cents",change_in_cents
        oring_change_in_cents = change_in_cents
        n_quarters = change_in_cents / 25      ## since this is int / int we'll get back an int
        change_in_cents -= n_quarters*25
        n_dimes    = change_in_cents / 10
        change_in_cents -= n_dimes*10
        n_nickels = change_in_cents / 5
        change_in_cents -= n_nickels*5
        n_pennies = change_in_cents
        if self.print_summary_of_every_transaction:
            print "  Transaction is $%.2f (coin change was %i cents)" % (transaction_amount ,oring_change_in_cents)
            print "     %s: quarters: %i dimes: %i nickels: %i pennies: %i" % ("returned", \
                                                                               n_quarters ,n_dimes,n_nickels,n_pennies)
                                                                               
            print "*" * 40
        return {"nickels": n_nickels, "quarters": n_quarters, "dimes": n_dimes, "pennies": n_pennies}



def answer_homework_questions():
    
    """performs the monte carlo, making many instances of CookieJars under different assumptions."""
    ## a: What is the average total amount of change accumulated each year (assume X=5)? 
    #     What is the 1-sigma scatter about this quantity?

    ## let's simulate 50 cookie jars of 1 year each
    njars = 50
    
    jars = []
    for j in xrange(njars):
        jars.append(CookieJar(transactions_per_day=5,number_of_days_until_fill=365,deplete_quarters=False))
        jars[-1].fill_er_up()

    fin = numpy.array([x.final_value for x in jars])
    mn = fin.mean()
    st = numpy.std(fin)
    print "question a"
    print "-"*50
    
    print "mean value accumulated per year:",mn,"\nstandard deviation from {} trials:".format(njars), st
    print "-"*50
    # mean = $181.71
    # st   = $5.99

    ## b. What coin (quarter, dime, nickel, penny) are you most likely to accumulate 
    ##    over time? Second most likely? Does it depend on X?
    first  = {"nickels": 0, "quarters": 0, "dimes": 0, "pennies":0}
    second = {"nickels": 0, "quarters": 0, "dimes": 0, "pennies":0}
    for j in jars:
        first[j.final_order[1]] += 1
        second[j.final_order[2]] += 1

    print "\nquestion b"
    print "-"*50
    print "transactions per day:",5
    print "times each coin was the most common:\n",first
    print "times each coin was the second most common:\n",second
    # pennies always first, quarters usually second (sometimes dimes)
    
    ## now let's try # transaction changes
    for tr in [2,10,20]:
        jars = []
        for j in xrange(50):
            jars.append(CookieJar(transactions_per_day=tr,number_of_days_until_fill=365,deplete_quarters=False))
            jars[-1].fill_er_up()
        
        first  = {"nickels": 0, "quarters": 0, "dimes": 0, "pennies":0}
        second = {"nickels": 0, "quarters": 0, "dimes": 0, "pennies":0}
        for j in jars:
            first[j.final_order[1]] += 1
            second[j.final_order[2]] += 1
        print "\ntransactions per day:",tr
        print "times each coin was the most common:\n",first
        print "times each coin was the second most common:\n",second
    ## answer: no. it doesn't
    
    ## c. Let's say you need 8 quarters per week to do laundry. How many quarters do you have at the end of the year?
    ## (if you do not have enough quarters at the end of each week, use only what you have).
    jars = []
    for j in xrange(50):
        jars.append(CookieJar(transactions_per_day=5,number_of_days_until_fill=365,deplete_quarters=True))
        jars[-1].fill_er_up()
    nq = 0
    for j in jars:
        nq += j.final_contents["quarters"]
    
    print "-"*50
    print "\nquestion c"
    print "-"*50

    print "average # of quarters left after a year:",nq/len(jars)
    # answer = 28
    print "-"*50
    
if __name__ == "__main__":
    answer_homework_questions()