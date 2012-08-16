## solutions to the breakout #2 (Day 1)

airports = {"DCA": "Washington, D.C.", "IAD": "Dulles", "LHR": "London-Heathrow", \
            "SVO": "Moscow", "CDA": "Chicago-Midway", "SBA": "Santa Barbara", "LAX": "Los Angeles",\
            "JFK": "New York City", "MIA": "Miami", "AUM": "Austin, Minnesota"}
            
# airline, number, heading to, gate, time (decimal hours) 
flights = [("Southwest",145,"DCA",1,6.00),("United",31,"IAD",1,7.1),("United",302,"LHR",5,6.5),\
           ("Aeroflot",34,"SVO",5,9.00),("Southwest",146,"CDA",1,9.60), ("United",46,"LAX",5,6.5),\
           ("Southwest",23,"SBA",6,12.5),("United",2,"LAX",10,12.5),("Southwest",59,"LAX",11,14.5),\
           ("American", 1,"JFK",12,11.3),("USAirways", 8,"MIA",20,13.1),("United",2032,"MIA",21,15.1),\
           ("SpamAir",1,"AUM",42,14.4)]

flights.sort()
print "Flight    \tDestination\t\tGate\tTime"
print "-"*50
for f in flights:
    dest = airports[f[2]]
    dest += " "*(20 - len(dest))
    print f[0] + " " + str(f[1]) + "\t" + dest + "\t" + str(f[3]) + "\t" + str(f[4])


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

print "Flight    \tDestination\t\tGate\tTime"
print "-"*50
for f in time_ordered:
    dest = airports[f[2]]
    dest += " "*(20 - len(dest))
    print f[0] + " " + str(f[1]) + "\t" + dest + "\t" + str(f[3]) + "\t" + str(f[4])        

"""
Flight    	Destination	Gate	Time
--------------------------------------------------
Aeroflot 34	Moscow              	5	9.0
American 1	New York City       	12	11.3
Southwest 23	Santa Barbara       	6	12.5
Southwest 59	Los Angeles         	11	14.5
Southwest 145	Washington, D.C.    	1	6.0
Southwest 146	Chicago-Midway      	1	9.6
SpamAir 1	Austin, Minnesota   	42	14.4
USAirways 8	Miami               	20	13.1
United 2	Los Angeles         	10	12.5
United 31	Dulles              	1	7.1
United 46	Los Angeles         	5	6.5
United 302	London-Heathrow     	5	6.5
United 2032	Miami               	21	15.1
Flight    	Destination	Gate	Time
--------------------------------------------------
Southwest 145	Washington, D.C.    	1	6.0
United 302	London-Heathrow     	5	6.5
United 46	Los Angeles         	5	6.5
United 31	Dulles              	1	7.1
Aeroflot 34	Moscow              	5	9.0
Southwest 146	Chicago-Midway      	1	9.6
American 1	New York City       	12	11.3
United 2	Los Angeles         	10	12.5
Southwest 23	Santa Barbara       	6	12.5
USAirways 8	Miami               	20	13.1
SpamAir 1	Austin, Minnesota   	42	14.4
Southwest 59	Los Angeles         	11	14.5
United 2032	Miami               	21	15.1

"""

### created by Josh Bloom at UC Berkeley, 2012 (ucbpythonclass+bootcamp@gmail.com)