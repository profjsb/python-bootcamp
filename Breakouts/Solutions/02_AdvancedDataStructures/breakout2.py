# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <markdowncell>

# 02_AdvancedDataStructures
# =============
# ### First, copy over the airport and flight information from airline.py. ###

# solutions to the breakout #2 (Day 1)


# <codecell>

airports = {"DCA": "Washington, D.C.", "IAD": "Dulles", "LHR": "London-Heathrow", \
            "SVO": "Moscow", "CDA": "Chicago-Midway", "SBA": "Santa Barbara", "LAX": "Los Angeles",\
            "JFK": "New York City", "MIA": "Miami", "AUM": "Austin, Minnesota"}

# <codecell>

# airline, number, heading to, gate, time (decimal hours) 
flights = [("Southwest",145,"DCA",1,6.00),("United",31,"IAD",1,7.1),("United",302,"LHR",5,6.5),\
           ("Aeroflot",34,"SVO",5,9.00),("Southwest",146,"CDA",1,9.60), ("United",46,"LAX",5,6.5),\
           ("Southwest",23,"SBA",6,12.5),("United",2,"LAX",10,12.5),("Southwest",59,"LAX",11,14.5),\
           ("American", 1,"JFK",12,11.3),("USAirways", 8,"MIA",20,13.1),("United",2032,"MIA",21,15.1),\
           ("SpamAir",1,"AUM",42,14.4)]

# <markdowncell>

# ### We can sort the flight information by airline by running a simple sort on the list. ###
# Note that when printing we lookup the destination name by the airport code key in the airports dictionary.

# <codecell>

flights.sort()
print "Flight    \tDestination\t\tGate\tTime"
print "-"*53
for f in flights:
    dest = airports[f[2]]
    dest += " "*(20 - len(dest))
    print f[0] + " " + str(f[1]) + "\t" + dest + "\t" + str(f[3]) + "\t" + str(f[4])

# <markdowncell>

# When we called flights.sort() we resorted the list based on the first element of each tuple (airline) and then, when multiple flights are operated by one ariline, by the flight number.

# <markdowncell>

# ### Sorting the information by time requires a bit more coding. ###
# We create a new time_ordered list and loop through the flights inspecting each flight for its time. We then insert the flight at the beginning of time_ordered, at the end of time_ordered, or in between two other elements within time_ordered. We determine where the current flight belongs by manually comparing the times of the flights already added to time_ordered.
# This is really trivial (a one liner) with lambda functions, which you'll lear later. 

# <codecell>

# note: this is a really trivial (one liner!) thing do with lambda functions, which you'll 
# learn later
time_ordered = [flights[0]]
for f in flights[1:]:
    ## does it belong in the beginning
    if f[4] < time_ordered[0][4]:
        time_ordered.insert(0,f)
        continue
    ## ... or the end?
    if f[4] > time_ordered[-1][4]:
        time_ordered.append(f)
        continue
    ## or is it in the middle
    for i in range(len(time_ordered) - 1):
        if f[4] >= time_ordered[i][4] and f[4] <= time_ordered[i+1][4]:
            time_ordered.insert(i+1,f)
            break

# <markdowncell>

# The printing procedure is the same.

# <codecell>

print "Flight    \tDestination\t\tGate\tTime"
print "-"*53
for f in time_ordered:
    dest = airports[f[2]]
    dest += " "*(20 - len(dest))
    print f[0] + " " + str(f[1]) + "\t" + dest + "\t" + str(f[3]) + "\t" + str(f[4])  

# <markdowncell>

# ### One line sorting solution. ###
# We can use the operator.itemgetter() function as the key in sort and sort by the time (4th) element.

# <codecell>

import operator
flights.sort(key=operator.itemgetter(4))
print "Flight    \tDestination\t\tGate\tTime"
print "-"*53
for f in flights:
    dest = airports[f[2]]
    dest += " "*(20 - len(dest))
    print f[0] + " " + str(f[1]) + "\t" + dest + "\t" + str(f[3]) + "\t" + str(f[4])

### created by Josh Bloom at UC Berkeley, 2012 (ucbpythonclass+bootcamp@gmail.com)