# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <markdowncell>

# <p class="title">Breakout 2 Solutions</p>
# 

# ### First, copy over the airport and flight information from [airline.py](https://raw.github.com/profjsb/python-bootcamp/master/DataFiles_and_Notebooks/02_AdvancedDataStructures/airline.py). ###


airports = {"DCA": "Washington, D.C.", "IAD": "Dulles", "LHR": "London-Heathrow", \
            "SVO": "Moscow", "CDA": "Chicago-Midway", "SBA": "Santa Barbara", "LAX": "Los Angeles",\
            "JFK": "New York City", "MIA": "Miami", "AUM": "Austin, Minnesota"}


# airline, number, heading to, gate, time (decimal hours) 
flights = [("Southwest",145,"DCA",1,6.00),("United",31,"IAD",1,7.1),("United",302,"LHR",5,6.5),\
           ("Aeroflot",34,"SVO",5,9.00),("Southwest",146,"CDA",1,9.60), ("United",46,"LAX",5,6.5),\
           ("Southwest",23,"SBA",6,12.5),("United",2,"LAX",10,12.5),("Southwest",59,"LAX",11,14.5),\
           ("American", 1,"JFK",12,11.3),("USAirways", 8,"MIA",20,13.1),("United",2032,"MIA",21,15.1),\
           ("SpamAir",1,"AUM",42,14.4)]


# Sort the list of flights.
flights.sort() 

# Print out the header. the \t character prints a tab.
print "Flight    \tDestination\t\tGate\tTime"
print "-"*53 #53 instances of the "-" character

# Loop through each of the flight tuples in the sorted list
# Recall that each tuple contains the elements: (airline, number, destination lookup code, gate, time)
for flight in flights:
    # Use the dest lookup code (3rd element of the flight tuple) to get the full destination string from the airports dict
    dest = airports[flight[2]]
    dest += " "*(20 - len(dest))  # add the appropriate amount of whitespace after the Destination string
    # Print the nicely formatted string. Don't forget to convert int and float types to strings using str()
    print flight[0] + " " + str(flight[1]) + "\t" + dest + "\t" + str(flight[3]) + "\t" + str(flight[4])

# Sorting by Departure Time
# ### Sorting the information by time requires a bit more coding. ###
# First, we create a new list, time_ordered_flights, which initially just contains the first element of the list flights.


# Create a new list, time_ordered, which initially just contains the first element of the list flights
time_ordered_flights = [flights[0]]

print time_ordered_flights

# We then loop through the remaining flights and insert it into the proper 
# position in time_ordered_flights by comparing the time element in each flight 
# tuple (at the fifth index position).
# We determine where the current flight belongs by manually comparing the times 
# of the flights  already added to time_ordered_flights.  (This is really 
# trivial with lambda functions, which you'll learn later.)


# Iterate through each of the remaining elements in flights to see where it 
# should go in the sorted list
for flight in flights[1:]:
    # Does it belong in the beginning?
    # is current flight's time less than the time in the first list element?
    if flight[4] < time_ordered_flights[0][4]: 
        # insert the flight tuple at position 0 in the list
        time_ordered_flights.insert(0,flight)   
        continue
    ## ... or the end?
    # is current flight's time greater than the time in the last list element?
    if flight[4] > time_ordered_flights[-1][4]:
        # append the flight tuple to the end of the list 
        time_ordered_flights.append(flight) 
        continue
    ## Or is it in the middle? 
    # Loop through each element and see if the current flight is between two adjacent ones
    ## note that range(N) returns a list [0, 1, ... , N-1] 
    for i in range(len(time_ordered_flights) - 1): 
        if flight[4] >= time_ordered_flights[i][4] and flight[4] <= time_ordered_flights[i+1][4]:
            time_ordered_flights.insert(i+1,flight) # insert the flight tuple at position i+1 in the list
            break


print "Flight    \tDestination\t\tGate\tTime"
print "-"*53
for flight in time_ordered_flights:
    dest = airports[flight[2]]
    dest += " "*(20 - len(dest))
    print flight[0] + " " + str(flight[1]) + "\t" + dest + "\t" + str(flight[3]) + "\t" + str(flight[4])  



# ### One line sorting solution. ###
# We can use the operator.itemgetter() function as the key in sort and sort by the time (4th) element.


import operator
flights.sort(key=operator.itemgetter(4))
print "Flight    \tDestination\t\tGate\tTime"
print "-"*53
for flight in flights:
    dest = airports[flight[2]]
    dest += " "*(20 - len(dest))
    print flight[0] + " " + str(flight[1]) + "\t" + dest + "\t" + str(flight[3]) + "\t" + str(flight[4])

# Alternate printing solution 

print "%.20s %.20s %.6s %.5s" % ("Flight"+20*' ', "Destination"+20*' ', "Gate"+20*' ', "Time"+20*' ')
print "-"*53
for flight in flights:
    print "%.20s %.20s %.6s %.5s" % (flight[0] + ' ' + str(flight[1])+20*' ', airports[flight[2]]+20*' ', str(flight[3])+20*' ', str(flight[4])+20*' ')